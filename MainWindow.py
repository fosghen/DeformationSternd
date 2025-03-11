# This Python file uses the following encoding: utf-8
import sys
import datetime
import serial

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QColor

from SensorsWorker import SensorsWorker
from SettingsDialog import SettingsDialog
from ui_form import Ui_MainWindow
from QToggle import QToggle
import utils.lir_utils as lu
import utils.stepper_utils as su

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создаём объекты для COM-портов
        self.dinamometr = None
        self.stepper_motor = None
        self.linear_encoder = None

        # Создаём объект для считывания данных с датчика
        self.worker = None

        # Создаём переключатель для изменения направления движения двигателя
        self.ui.customCheckBox = QToggle(
                            checkedText="К двигателю",
                            uncheckedText="От двигателя",
                            checkedColor=QColor(0, 176, 255),
                            uncheckedColor=QColor(0, 176, 255),
                            parent = self
                            )
        self.ui.toggle_direct.deleteLater()
        self.ui.toggle_direct = self.ui.customCheckBox
        self.ui.gridLayout_3.addWidget(self.ui.toggle_direct, 2, 1, 1, 1)
        self.ui.toggle_direct.setDisabled(1)

        # Устанавливаем значения максимальное, минимальное и начальное значения скорости двигателя
        self.ui.sbox_speed.setRange(1, 312)
        self.ui.sbox_speed.setValue(1000)

        # Устанавливаем значения максимальное, минимальное и начальное значения сдвига
        self.ui.dsbox_distance.setRange(1, 400)
        self.ui.dsbox_distance.setValue(5)

        # Связываем сигнал с вызова настроек с соответствующей функцией
        if self.ui.connection_settings:
            self.ui.connection_settings.triggered.connect(self.open_settings)

        # Связываем сигналы от кнопок в модуле подвижки с функциями
        self.ui.pbutton_start.pressed.connect(self.start_stepper_motor)
        self.ui.pbutton_stop.pressed.connect(self.stop_stepper_motor)


    # Вызаваем окно настроек
    def open_settings(self):
        self.settings_window = SettingsDialog()
        # Связываем события закрытия с функцией
        self.settings_window.finished.connect(self.on_settings_closed)
        self.settings_window.exec()

    # Получаем COM порты, которые пользователь выбрал
    def on_settings_closed(self):
        # Подключаемся к шаговому двигателю
        self.stepper_motor = serial.Serial(
                self.settings_window.ui.cbox_stepper_motor.currentText(),
                9600,
                timeout=1
                )
        if (not self.stepper_motor):
            print("Не смог подключиться к двигателю")
            return

        # Подключаемся к динамометру
        self.dinamometr = serial.Serial(
                self.settings_window.ui.cbox_dinamomert.currentText(),
                9600,
                timeout=1
                )
        if (not self.dinamometr):
            print("Не смог подключиться к динамометру")
            return

        # Подключаемся к линейке
        self.linear_encoder = lu.connect(
                0xdead,
                0xffff)
        lu.start_setup(self.linear_encoder)

        if (not self.linear_encoder):
            print("Не смог подключиться к линейному энкодеру")
            return

        self.set_enabled_widgets()

        # Передаём воркеру интерфейсы общения
        self.worker = SensorsWorker(self.dinamometr, self.linear_encoder)
        # Связываем сигнал от воркера с тем, что нужно вывести данные в глобальный лог
        self.worker.data_received.connect(self.update_global_log)
        # Запускаем
        self.worker.running = True
        self.worker.start()
        # Делаем заголовок для глобального лона
        self.ui.tedit_global_log.append("Время\tДинамометр\tЛинейка")

    def set_enabled_widgets(self):
        # # Модуль чувствительного элемента
        # self.ui.ledit_type_se.setEnabled(1)
        # self.ui.ledit_sens_el.setEnabled(1)
        # self.ui.dsbox_diam_start.setEnabled(1)
        # self.ui.dsbox_mod_young.setEnabled(1)
        # self.ui.dsbox_max_deform.setEnabled(1)
        # self.ui.dsbox_max_force.setEnabled(1)
        # self.ui.dsbox_deform_lim.setEnabled(1)
        # self.ui.dsbox_sagging.setEnabled(1)
        # self.ui.ledit_notes.setEnabled(1)

        # # Модуль испытуемого устройства опроса
        # self.ui.ledit_type_uo.setEnabled(1)
        # self.ui.ledit_name_uo.setEnabled(1)
        # self.ui.ledit_fac_no.setEnabled(1)
        # self.ui.ledit_tipe_of.setEnabled(1)
        # self.ui.dsbox_meas_dist.setEnabled(1)
        # self.ui.dsbox_spat_res.setEnabled(1)
        # self.ui.sbox_chan_no.setEnabled(1)
        # self.ui.ledit_diap_meas_def.setEnabled(1)
        # self.ui.dsbox_opt_dist.setEnabled(1)

        # Модуль подвижки
        self.ui.sbox_speed.setEnabled(1)
        self.ui.toggle_direct.setEnabled(1)
        self.ui.dsbox_distance.setEnabled(1)
        self.ui.pbutton_start.setEnabled(1)
        self.ui.pbutton_stop.setEnabled(1)

        # # Модуль деформации
        # self.ui.dsbox_deform_area.setEnabled(1)
        # self.ui.pbutton_set_zero.setEnabled(1)
        # self.ui.cmob_type_deform.setEnabled(1)
        # self.ui.dsbox_long_deform.setEnabled(1)
        # self.ui.cbox_units_long_deform.setEnabled(1)
        # self.ui.dsbox_trans_deform.setEnabled(1)
        # self.ui.cbox_units_trans_deform.setEnabled(1)
        # self.ui.dsbox_dist_to_trans_deform.setEnabled(1)
        # self.ui.pbutton_start_deform.setEnabled(1)
        # self.ui.chbox_write_file.setEnabled(1)

    def start_stepper_motor(self):
        speed = int(self.ui.sbox_speed.value() / 0.25)
        direction = int(not self.ui.toggle_direct.isChecked())
        count = int(1000 * self.ui.dsbox_distance.value() / 0.25)

        su.start(speed, direction, count, self.stepper_motor)

    def stop_stepper_motor(self):
        su.stop(self.stepper_motor)

    def update_global_log(self, data: list):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        self.ui.tedit_global_log.append(formatted_time + "\t" + str(data[0]) + "\t" + str(data[1]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
