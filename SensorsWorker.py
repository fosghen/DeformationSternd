from PySide6.QtCore import QThread, Signal
import time
import serial, hid
import utils.lir_utils as lu
# This Python file uses the following encoding: utf-8


class SensorsWorker(QThread):
    data_received = Signal(list)  # Сигнал для передачи данных в основной поток

    def __init__(
        self,
        dinanometr: serial.serialwin32.Serial,
        linear_encoder: hid.device
        ):
        super().__init__()
        self.dinamometr = dinanometr # Интерфейс для получения данных с динамометра
        self.linear_encoder = linear_encoder # Интерфейс для получения данных с линейки

        self.running = True # Флаг остановки потока

    def run(self) -> None:
        while self.running:
            time.sleep(0.5)
            try:
                dino_data = self.dinamometr.read_all()  # Считываем данные с динамометра
                line_data = lu.read_linear_encoder(self.linear_encoder) # Считываем данные с линейки

                dino_data = dino_data.decode().split("\r\n")

                try:
                    dino_data = float(dino_data[-1])
                except:
                    dino_data = float(dino_data[-2])

                if dino_data:
                    self.data_received.emit([dino_data, line_data])  # Отправляем данные в основной поток
            except serial.SerialException as e:
                self.data_received.emit(f"Ошибка связи: {e}")
                break

    def stop(self) -> None:
        self.running = False  # Останавливаем поток
