import asyncio

from barcode_reader import BarcodeReader


async def main_run(reader: BarcodeReader) -> None:
    while True:
        code = reader.code
        if code is not None and len(code) > 0:
            print(code)
        if not reader.ready:
            print("printer not ready !!!")
        await asyncio.sleep(0.5)


async def main() -> None:
    reader = BarcodeReader(
        port="/dev/ttyACM0",
        baudrate=19200,
    )
    await asyncio.gather(main_run(reader), reader.run())


if __name__ == "__main__":
    asyncio.run(main(), debug=True)
