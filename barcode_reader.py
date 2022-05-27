import serial
import asyncio


class BarcodeReader:
    """Сканер штрих-кодов."""

    def __init__(
        self: "BarcodeReader",
        port: str = "/dev/ttyACM0",
        baudrate: int = 19200,
    ):
        self._port = port
        self._baudrate = baudrate
        self._code = ""
        self._ready = False

    @property
    def code(self: "BarcodeReader") -> str:
        """Последний прочитанный код."""
        code = self._code
        self._code = ""
        return code

    @property
    def ready(self: "BarcodeReader") -> bool:
        """Готов ли сканер к работе."""
        return self._ready

    async def run(self: "BarcodeReader") -> None:
        while True:
            try:
                with serial.Serial(
                    port=self._port,
                    baudrate=self._baudrate,
                    timeout=0,
                ) as ser:
                    self._ready = True
                    while True:
                        line = ser.readline()
                        if len(line) > 0:
                            self._code = line[:-2]
                        await asyncio.sleep(0.2)
            except serial.SerialException as e:
                print(e.strerror)
            self._ready = False
            await asyncio.sleep(5)
