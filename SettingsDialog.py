# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from serial.tools import list_ports

from ui_settings import Ui_Frame

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        # В выпадающие списки добавляем все подключенные COM-порты
        self.ui.cbox_stepper_motor.addItems([port.device for port in list_ports.comports()])
        self.ui.cbox_dinamomert.addItems([port.device for port in list_ports.comports()])
