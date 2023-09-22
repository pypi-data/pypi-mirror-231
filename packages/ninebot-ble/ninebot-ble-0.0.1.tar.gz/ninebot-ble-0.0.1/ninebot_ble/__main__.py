import asyncio
import logging
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from ninebot_ble import NinebotBleSensor, BmsIdx, CtrlIdx, iter_register, NinebotClient, get_register_desc
from home_assistant_bluetooth import BluetoothServiceInfo
import time
from typing import Any

import argparse


logger = logging.getLogger(__name__)


async def find_scooter() -> tuple[BLEDevice, AdvertisementData]:
    """Scans the network for a ninebot scooter."""
    scan_queue: asyncio.Queue[tuple[BLEDevice, AdvertisementData]] = asyncio.Queue(100)

    async def _on_scan_found(dev: BLEDevice, adv: AdvertisementData) -> None:
        logger.debug("scan: %s | %s", dev, adv)
        await scan_queue.put((dev, adv))

    async def scan() -> tuple[BLEDevice, AdvertisementData] | None:
        async with BleakScanner(scanning_mode="active", detection_callback=_on_scan_found):
            deadline = time.time() + 30
            while time.time() < deadline:
                try:
                    dev, adv = scan_queue.get_nowait()
                    # TODO: Find a better way of finding a ninebot scooter!
                    if dev.name is not None and "nbscooter" in dev.name.lower():
                        return dev, adv
                except asyncio.QueueEmpty:
                    await asyncio.sleep(0.1)
        return None

    result = await scan()
    if result is None:
        raise RuntimeError("Unable to find scooter")
    return result


def dump_reg(name: str, val: Any, unit: str) -> None:
    print(f"{name:<40}: {val} {unit}")


async def main() -> None:
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
    logging.getLogger("bleak.backends.bluezdbus.manager").level = logging.WARNING
    logging.getLogger("bleak.backends.bluezdbus.client").level = logging.WARNING

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", help="read all register indices")
    parser.add_argument("--sensor-run", action="store_true", help="start and dump sensor")

    arg_mapping: dict[str, BmsIdx | CtrlIdx] = {}
    for idx in iter_register(CtrlIdx, BmsIdx):
        arg = "_".join(str(idx).lower().split())
        arg_mapping[arg] = idx
        parser.add_argument("--" + arg, action="store_true", help=f"read {str(idx).lower()}")

    args = parser.parse_args()

    device, advertisement = await find_scooter()

    if not args.sensor_run:
        client = NinebotClient()
        try:
            await client.connect(device)
            if args.all:
                for idx in iter_register(CtrlIdx, BmsIdx):
                    val = await client.read_reg(idx)
                    desc = get_register_desc(idx)
                    dump_reg(str(idx), val, desc.unit or "")
            else:
                for idx_arg, idx in arg_mapping.items():
                    if args.__dict__.get(idx_arg):
                        val = await client.read_reg(idx)
                        desc = get_register_desc(idx)
                        dump_reg(str(idx), val, desc.unit or "")
        finally:
            await client.disconnect()
        return

    nb = NinebotBleSensor()
    try:
        nb.update(BluetoothServiceInfo.from_advertisement(device, advertisement, "Unknown"))
        update = await nb.async_poll(device)
        print("Title:       ", update.title)
        print("Name:        ", update.devices[None].name)
        print("Model:       ", update.devices[None].model)
        print("Manufacturer:", update.devices[None].manufacturer)
        print("SW version:  ", update.devices[None].sw_version)
        print("HW version:  ", update.devices[None].hw_version)
        print("-" * 100)
        for dk, dv in update.entity_values.items():
            unit = str(update.entity_descriptions[dk].native_unit_of_measurement)
            if not unit:
                unit = ""
            print(f"{dv.name:<40}: {dv.native_value} {unit}")
    finally:
        await nb.disconnect()


def entrypoint() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    entrypoint()
