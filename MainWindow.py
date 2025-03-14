# This Python file uses the following encoding: utf-8
import sys
import os
import datetime
import serial

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QColor

from SensorsWorker import SensorsWorker
from SettingsDialog import SettingsDialog
from ui_form import Ui_MainWindow
from QToggle import QToggle
import utils.lir_utils as lu
import utils.stepper_utils as su

from numpy import savetxt, vstack, array

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

# Cascadin Code
class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Флаг начала эксперимента
        self.flag_start = True

        # Предыдущее значение продольной деформации
        self.prev_long_deform = 0

        # Массивы для хранения показаний
        self.time_list = []
        self.linear_encoder_list = []
        self.dinamometr_list = []
        self.deformation_list = []
        self.deformation_flag_list = [] # 0 - прод 1 - попер 2 - обе

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

        # Связываем сигнал от кнопки установки нуля с функцией
        self.ui.pbutton_set_zero.pressed.connect(self.set_zero_on_line)
        # Связываем сигнал от кнопки запуска с функцией
        self.ui.pbutton_start_deform.pressed.connect(self.start_deformation)
        # Связываем сигнал от кнопки сохранения файла с функцией
        self.ui.pbutton_save_file.pressed.connect(self.save_file)

    def open_settings(self) -> None:
        '''Создание окна настроек подключения датчиков.'''
        self.settings_window = SettingsDialog()
        # Связываем события закрытия с функцией
        self.settings_window.finished.connect(self.on_settings_closed)
        self.settings_window.exec()

    def on_settings_closed(self) -> None:
        '''
        Функция вызывается, когда окно настройки подключения датчиков закрывается.
        Получаем COM порты, которые пользователь выбрал, и подключаемся к ним.
        '''
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

    def set_enabled_widgets(self) -> None:
        '''Делаем активными виджеты, после того, как успешно подключились к датчиками.'''
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
        self.ui.dsbox_deform_area.setEnabled(1)
        self.ui.pbutton_set_zero.setEnabled(1)
        self.ui.cmob_type_deform.setEnabled(1)
        self.ui.dsbox_long_deform.setEnabled(1)
        self.ui.cbox_units_long_deform.setEnabled(1)
        self.ui.dsbox_trans_deform.setEnabled(1)
        self.ui.cbox_units_trans_deform.setEnabled(1)
        self.ui.dsbox_dist_to_trans_deform.setEnabled(1)
        self.ui.pbutton_start_deform.setEnabled(1)
        self.ui.chbox_write_file.setEnabled(1)

    def start_stepper_motor(self) -> None:
        '''Запустить шаговый двигатель по кнопке.'''
        speed = int(self.ui.sbox_speed.value() / 0.25)
        direction = int(not self.ui.toggle_direct.isChecked())
        count = int(1000 * self.ui.dsbox_distance.value() / 0.25)

        su.start(speed, direction, count, self.stepper_motor)

    def stop_stepper_motor(self) -> None:
        '''Остановить шаговый двигатель по кнопке.'''
        su.stop(self.stepper_motor)

    def update_global_log(self, data: list) -> None:
        '''Добавить в виджет глобального лога: время и показания датчиков.'''
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        self.ui.tedit_global_log.append(formatted_time + "\t" + str(data[0]) + "\t" + str(data[1]))
        # Если есть разрешение записи в файл, то сохраняется значение текущие
        if (self.ui.chbox_write_file.isChecked):
            # Время
            self.time_list.append(formatted_time)
            # Показания линейки
            self.linear_encoder_list.append(data[1])
            # Показания динамометра
            self.dinamometr_list.append(data[0])
            # Тип деформации
            self.deformation_flag_list.append(self.ui.cmob_type_deform.currentIndex())
            # Сохраняем всегда полную деформацию
            match self.ui.cmob_type_deform.currentIndex():
                case 0:
                    _, eps = self._compute_long_deform()
                case 1:
                    _, eps = self._compute_trans_deform()
                case 2:
                    _, eps_long = self._compute_long_deform()
                    _, eps_trans = self._compute_trans_deform()
                    eps = eps_long + eps_trans
            self.deformation_list.append(eps)


    def set_zero_on_line(self) -> None:
        '''Выставить относительный ноль на линейном энкодере.'''
        lu.set_zero_linear_encoder(self.linear_encoder)

    def _compute_trans_deform(self) -> float:
        '''Расчёт необходимого поперечного смещения для того, чтобы достигнуть нужной деформации.'''
        # Полная длина линии в мм
        full_length = self.ui.dsbox_deform_area.value() * 1e3
        # Часть от нулевой точки до точки поперечного растяжения в мм
        near_length = self.ui.dsbox_dist_to_trans_deform.value() * 1e3
        # Часть от точки поперечного растяжения до конечной точки в мм
        far_length = full_length - near_length
        # Удлинение в некоторых епсилонах далее переведём
        eps = self.ui.dsbox_trans_deform.value()

        if not self.ui.cbox_units_trans_deform.currentIndex():
            # Перевод микро эпсилинов в мили эпсилоны
            eps *= 1e-3
        else:
            # Перевод процентных эпсилинов в мили эпсилоны
            eps *= 10
        # Вычисляем попоречное смещение для линии
        trans_deform = (((full_length ** 2 * (1 + eps) ** 2 - far_length ** 2 + near_length ** 2) / \
             (2 * full_length * (1 + eps))) ** 2 - near_length ** 2) ** 0.5

        return trans_deform, eps * 1e3

    def _compute_long_deform(self) -> int:
        '''Расчёт необходимого количества шагов двигателя для достижения нужной деформации.'''
        # Полная длина линии в мм
        full_length = self.ui.dsbox_deform_area.value() * 1e3
        # Удлинение в некоторых эпсилонах далее переведём
        eps = self.ui.dsbox_long_deform.value()

        match self.ui.cbox_units_long_deform.currentIndex():
            case 0:
                eps *= 1e-3
            case 1:
                eps *= 10
            case 2:
                return int(eps * 4), 1000 * eps / full_length

        return int(full_length * eps) * 4, eps * 1e3


    def start_deformation(self) -> None:
        '''Запустить деформирование оптического волокна.'''
        # Если первый запуск, то очищаем все массивы
        if self.flag_start:
            self.flag_start = False
            self.time_list = []
            self.linear_encoder_list = []
            self.dinamometr_list = []
            self.deformation_list = []
            self.deformation_flag_list = []
            self.prev_long_deform = 0


        eps_trans = 0
        eps_long = 0
        match self.ui.cmob_type_deform.currentIndex():
            case 0:
                steps, eps_long = self._compute_long_deform()
            case 1:
                trans_deform, eps_trans = self._compute_trans_deform()
                self.ui.label_leng_trans_out.setText(str(trans_deform))
            case 2:
                trans_deform, eps_trans = self._compute_trans_deform()
                self.ui.label_leng_trans_out.setText(str(trans_deform))
                steps, eps_long = self._compute_long_deform()
        eps_full = eps_trans + eps_long
        self.ui.label_total_deform_out.setText(str(eps_full))
        
        print(int(steps / 4), self.prev_long_deform)
        if (int(steps / 4) > self.prev_long_deform):
            su.start(300, 0, abs(int(steps / 4) - self.prev_long_deform) * 4, self.stepper_motor)
            print(f"Шагнул к двигателю на {abs(int(steps / 4) - self.prev_long_deform) * 4}")
        else:
            su.start(300, 1, abs(int(steps / 4) - self.prev_long_deform) * 4, self.stepper_motor)
            print(f"Шагнул от двигателя на {abs(int(steps / 4) - self.prev_long_deform) * 4}")

        self.prev_long_deform = int(steps / 4)

    def save_file(self) -> None:
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", os.getcwd(), "Файл с разделителем запятая (*.csv);;Все файлы (*)")
        if file_path:
            # Выключаем запись в файл
            self.ui.chbox_write_file.setChecked(False)
            # Выставляем флаг, что следующий запуск будет новый эксперимент
            self.flag_start = True

            savetxt(
                file_path,
                vstack((
                    array(self.time_list, dtype=str),
                    array(self.linear_encoder_list, dtype=float),
                    array(self.dinamometr_list, dtype=float),
                    array(self.deformation_list, dtype=float),
                    array(self.deformation_flag_list, dtype=float)
                )).T,
                delimiter=';',
                fmt='%s',
                header = "Time;Linear Encoder;Dinamometr;Deformation;Deformation type;"
            )




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
