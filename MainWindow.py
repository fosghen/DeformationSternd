# This Python file uses the following encoding: utf-8
import sys
import os
import datetime
import serial
from  time import sleep

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PySide6.QtGui import QColor

from SensorsWorker import SensorsWorker
from SettingsDialog import SettingsDialog
from ui_form import Ui_MainWindow
from QToggle import QToggle
import utils.lir_utils as lu
import utils.stepper_utils as su
from utils.common_utils import get_value_from_sensors
from PyQtGraphWidget import PyQtGraphWidget

from numpy import savetxt, vstack, array, pi

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
        # Флаг выставления нуля
        self.flag_setting_zero = False
        # Количество подряд неподвижных частей (надо переделать жтот коментарий)
        self.it = 0

        # Предыдущее значение продольной деформации
        self.prev_long_deform = 0
        # Предыдущее значение линейного энкодера
        self.prev_linear_encoder = 0

        # Массивы для хранения показаний
        self.time_list = []
        self.linear_encoder_list = []
        self.dinamometr_list = []
        self.deformation_list = []
        self.deformation_flag_list = [] # 0 - прод 1 - попер 2 - обе

        # Аттрибуты для хранения текущих показаний
        self.length_current = 0
        self.force_current = 0

        # Создаём объекты для COM-портов
        self.dinamometr = None
        self.stepper_motor = None
        self.linear_encoder = None

        # Создаём объект для считывания данных с датчика
        self.worker = None

        # Создаём объект для окона графиков
        self.graph = None

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
        self.ui.dsbox_distance.setRange(0.0001, 400)
        self.ui.dsbox_distance.setValue(5)

        # Связываем сигнал вызова настроек с соответствующей функцией
        if self.ui.connection_settings:
            self.ui.connection_settings.triggered.connect(self.open_settings)

        # Связываем сигналы вызовов графиков со своими функциями
        if self.ui.graph:
            self.ui.graph.triggered.connect(self.open_graph)

        # Связываем сигналы от кнопок в модуле подвижки с функциями
        self.ui.pbutton_start.pressed.connect(self.start_stepper_motor)
        self.ui.pbutton_stop.pressed.connect(self.stop_stepper_motor)

        # Связываем сигнал от кнопки установки нуля с функцией
        self.ui.pbutton_set_zero.pressed.connect(self.set_zero_on_line)
        # Связываем сигнал от кнопки запуска с функцией
        self.ui.pbutton_start_deform.pressed.connect(self.start_deformation)
        # Связываем сигнал от кнопки сохранения файла с функцией
        self.ui.pbutton_save_file.pressed.connect(self.save_file)

        # Связываем сигналы от изменения в полях модуля расчётных данных
        self.ui.dsbox_final_diam.valueChanged.connect(self.compute_rel_narrow)
        self.ui.dsbox_final_length.valueChanged.connect(self.compute_rel_elong)

        # Делаем заголовок для глобального лона
        self.ui.tedit_global_log.append("Время\tДинамометр\tЛинейка")

    def open_settings(self) -> None:
        '''Создание окна настроек подключения датчиков.'''
        self.settings_window = SettingsDialog()
        # Связываем события закрытия с функцией
        self.settings_window.ui.pbutton_connect.pressed.connect(self.com_connect)
        self.settings_window.ui.pbutton_disconnect.pressed.connect(self.com_disconnect)
        # self.settings_window.finished.connect(self.on_settings_closed)
        self.settings_window.exec()

    def open_graph(self) -> None:
        '''Создание окна с графикома деформации и силы'''
        self.graph = PyQtGraphWidget()
        self.graph.show()

    def com_disconnect(self) -> None:
        if self.worker != None:
            self.worker.stop()
            del self.worker
            self.worker = None


        if self.stepper_motor != None:
            print("шаговый двиг выкл")
            self.stepper_motor.close()
            self.stepper_motor = None

        if self.dinamometr != None:
            print("динамом выкл")
            self.dinamometr.close()
            self.dinamometr = None

        if self.linear_encoder != None:
            self.linear_encoder.close()
            self.linear_encoder = None



    def com_connect(self) -> None:
        '''
        Функция вызывается, когда окно настройки подключения датчиков закрывается.
        Получаем COM порты, которые пользователь выбрал, и подключаемся к ним.
        '''
        # Подключаемся к шаговому двигателю
        if self.stepper_motor != None:
            if not self.stepper_motor.is_open:
                self.stepper_motor.open()

        if self.stepper_motor == None:
            print("шаговый двиг вкл")
            self.stepper_motor = serial.Serial(
                    self.settings_window.ui.cbox_stepper_motor.currentText(),
                    9600,
                    timeout=1
                    )
            if (not self.stepper_motor):
                print("Не смог подключиться к двигателю")
                return

        if self.dinamometr != None:
            if not self.dinamometr.is_open:
                self.dinamometr.open()

        # Подключаемся к динамометру
        if self.dinamometr == None:
            print("динамом вкл")
            self.dinamometr = serial.Serial(
                    self.settings_window.ui.cbox_dinamomert.currentText(),
                    9600,
                    timeout=1
                    )
            if (not self.dinamometr):
                print("Не смог подключиться к динамометру")
                return

        # Подключаемся к линейке
        if self.linear_encoder == None:
            self.linear_encoder = lu.connect(
                    0xdead,
                    0xffff)
            lu.start_setup(self.linear_encoder)

            if (not self.linear_encoder):
                print("Не смог подключиться к линейному энкодеру")
                return

        self.set_enabled_widgets()

        if self.worker == None:
            # Передаём воркеру интерфейсы общения
            self.worker = SensorsWorker(self.dinamometr, self.linear_encoder)
            # Связываем сигнал от воркера с тем, что нужно вывести данные в глобальный лог
            self.worker.data_received.connect(self.update_global_log)
            # Запускаем
            self.worker.start()
        self.worker.running = True
        self.worker.start()



    def set_enabled_widgets(self) -> None:
        '''Делаем активными виджеты, после того, как успешно подключились к датчиками.'''
        frames = [
                self.ui.sens_el_frame,         # Модуль чувствительного элемента
                self.ui.module_surv_dev_frame, # Модуль испытуемого устройства опроса
                self.ui.module_move_frame,     # Модуль подвижки
                self.ui.experiment_frame,      # Модуль деформации
                self.ui.calculation_data_frame # Модуль расчётных данных
            ]

        for frame in frames:
            for widget in frame.findChildren(QWidget):
                widget.setEnabled(True)


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

        self.force_current, self.length_current = data
        if self.flag_setting_zero and (abs(self.length_current - self.prev_linear_encoder) < 0.2):
            self.it += 1 
            if self.it == 5:
                self.it = 0
                lu.set_zero_linear_encoder(self.linear_encoder)
                self.flag_setting_zero = False

        self.prev_linear_encoder = self.length_current

        # Если есть разрешение записи в файл, то сохраняется значение текущие
        if (self.ui.chbox_write_file.isChecked()):
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

        if self.graph != None:
            self.graph.update(self.time_list, self.linear_encoder_list, self.dinamometr_list)


    def set_zero_on_line(self) -> None:
        '''Выставить относительный ноль на линейном энкодере.'''

        if self.ui.dsbox_sagging.value() < 1e-3:
            lu.set_zero_linear_encoder(self.linear_encoder)
            return

        self.find_zero_position()

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
            # Перевод микро эпсилонов в мили эпсилоны
            eps *= 1e-3
        else:
            # Перевод процентных эпсилонов в мили эпсилоны
            eps *= 10
        # Вычисляем попоречное смещение для линии
        trans_deform = (((full_length ** 2 * (1 + eps) ** 2 - far_length ** 2 + near_length ** 2) / \
             (2 * full_length * (1 + eps))) ** 2 - near_length ** 2) ** 0.5

        return trans_deform / 1e3, eps * 1e3

    def _compute_long_deform(self) -> int:
        '''Расчёт необходимого количества шагов двигателя для достижения нужной деформации.'''
        # Полная длина линии в мм
        full_length = self.ui.dsbox_deform_area.value() * 1e3
        # Удлинение в некоторых эпсилонах далее переведём
        eps = self.ui.dsbox_long_deform.value()
        # Пересчитываем продольную деформацию в зависимотси от единиц измерений
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

        # Определяем количество шагов
        steps = 0
        # Определяем общую деформацию
        eps_trans = 0
        eps_long = 0
        match self.ui.cmob_type_deform.currentIndex():
            # В случае только продольной, общая деформация равна продольной
            case 0:
                steps, eps_long = self._compute_long_deform()
            # В случае только поперечной, общая деформация равна поперечной
            case 1:
                trans_deform, eps_trans = self._compute_trans_deform()
                # Выводим в поле, насколько нужно сместить поперечный вал
                self.ui.label_leng_trans_out.setText(str(trans_deform))
            # В случае только продольной поперечной, общая деформация равна сумме продольной и поперечной
            case 2:
                trans_deform, eps_trans = self._compute_trans_deform()
                # Выводим в поле, насколько нужно сместить поперечный вал
                self.ui.label_leng_trans_out.setText(str(trans_deform))
                steps, eps_long = self._compute_long_deform()
        eps_full = eps_trans + eps_long
        self.ui.label_total_deform_out.setText(str(eps_full))
        
        # Определяем максмальные допустимые усилие и деформацию, если они нулевые, то ограничений нет
        max_deform = self.ui.dsbox_max_deform.value() if (self.ui.dsbox_max_deform.value() >= 1e-3) else 1e6
        max_force = self.ui.dsbox_max_force.value() if (self.ui.dsbox_max_force.value() >= 1e-3) else 1e6

        # Если текущая сила или деформация превыщает, то мы ничего не делаем
        if (max_force > self.force_current) and (max_deform > eps_full * 1e-4):
            # А если делаем, то сравниваемся с предылущим значением и уже на основе этого вычисляем
            # направление и количество шагов
            if (int(steps / 4) > self.prev_long_deform):
                su.start(300, 0, abs(int(steps / 4) - self.prev_long_deform) * 4, self.stepper_motor)
                print(f"Шагнул к двигателю на {abs(int(steps / 4) - self.prev_long_deform) * 4}")
            else:
                su.start(300, 1, abs(int(steps / 4) - self.prev_long_deform) * 4, self.stepper_motor)
                print(f"Шагнул от двигателя на {abs(int(steps / 4) - self.prev_long_deform) * 4}")

            self.prev_long_deform = int(steps / 4)

    def save_file(self) -> None:
        '''Сохранить эксперимент в текстовый файл'''
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", os.getcwd(), "Файл с разделителем запятая (*.csv);;Все файлы (*)")
        if file_path:
            # Выключаем запись в файл
            self.ui.chbox_write_file.setChecked(False)
            # Выставляем флаг, что следующий запуск будет новый эксперимент
            self.flag_start = True
            # Сохраняем текстовый файл в формате csv
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
                header = self.create_header(),
                comments=''
            )

    def create_header(self) -> str:
        '''Создать заголовок для файла сохранения'''
        ce_data = {
                "Вид ЧЭ": self.ui.ledit_type_se.text(),
                "Схема подключения": self.ui.ledit_sens_el.text(),
                "Начальный диаметр сечения ЧЭ": f"{self.ui.dsbox_diam_start.value()} мм",
                "Модуль Юнга, E": f"{self.ui.dsbox_mod_young.value()} Па",
                "Максимальная деформация": f"{self.ui.dsbox_max_deform.value()} %",
                "Максимальное усилие": f"{self.ui.dsbox_max_force.value()} Н",
                "Усилие исключающее провисание": f"{self.ui.dsbox_sagging.value()} Н",
                "Придел упругой деформации": f"{self.ui.dsbox_deform_lim.value()} Н",
                "Заметки": self.ui.ledit_notes.text()
            }

        uo_data = {
            "Тип УО": self.ui.ledit_type_uo.text(),
            "Наименование УО": self.ui.ledit_name_uo.text(),
            "Заводской №": self.ui.ledit_fac_no.text(),
            "Вид ОВ": self.ui.ledit_type_of.text(),
            "Измеряемая дистанция": f"{self.ui.dsbox_meas_dist.value()} мм",
            "Пространственное разрешение": f"{self.ui.dsbox_spat_res.value()} м",
            "№ канала изм.": self.ui.sbox_chan_no.value(),
            "Диапазон измеряемой деформации": self.ui.ledit_diap_meas_def.text(),
            "Оптическое расстояние": f"{self.ui.dsbox_opt_dist.value()} м"
        }

        # Формируем заголовок
        header_sections = [
            "========Описание ЧЭ========",
            *[f"{key}: {value}" for key, value in ce_data.items()],
            "========Описание УО========",
            *[f"{key}: {value}" for key, value in uo_data.items()],
            "========Измеряемые параметры========",
            "Time;Linear Encoder;Dinamometr;Deformation;Deformation type;"
        ]

        return "\n".join(header_sections)

    def find_zero_position(self) -> None:
        '''Поиск позиции преднатяга, выставление нулевой точки'''
        # 1. Определение стартовых значений
        f_0, x_0 = self.force_current, self.length_current
        # 2. Смещение на 1000 шагов к двигателю
        su.start(500, 0, 1000, self.stepper_motor)
        # Ждём пока двигаель поработает и всё успокоится
        sleep(3)

        # 3. Определение новых значений
        f_1, x_1 = get_value_from_sensors(self.dinamometr, self.linear_encoder)
        print(x_0, x_1, f_0, f_1)

        # 4. Вычисление новой координаты
        x_2 = (x_1 - x_0) * (self.ui.dsbox_sagging.value() - f_0) / (f_1 - f_0)
        print(x_2)
        # 5. Отправляем работать шаговый двигатель
        su.start(500, int(x_2 < 0), int(abs(4 * x_2)), self.stepper_motor)
        self.flag_setting_zero = True
        sleep(0.5)

    def compute_rel_elong(self, final_lenght: float) -> None:
        start_lenght = self.ui.dsbox_deform_area.value()
        if start_lenght > 0:
            delta = 100 * (final_lenght - start_lenght) / start_lenght
            self.ui.label_output_rel_elong.setText(str(delta))
        else:
            self.ui.label_output_rel_elong.setText("Деформируемый участок, ΔL = 0!")

    def compute_rel_narrow(self, final_diam: float) -> None:
        start_diam = self.ui.dsbox_diam_start.value()
        if final_diam > 0:
            psi = 100 * ((start_diam / final_diam) ** 2 - 1)
            self.ui.label_output_rel_narrow.setText(str(psi))

            E = self.compute_module_elasty(final_diam)
            self.ui.label_output_module_elast.setText(str(E))

        else:
            self.ui.label_output_rel_narrow.setText("Конечный диаметр ЧЭ = 0!")

    def compute_module_elasty(self, final_diam: float) -> float | str:
        if self.length_current == 0:
            return "Относительное удлинение нулевое"

        return self.force_current * self.ui.dsbox_deform_area.value() / self.length_current / (pi * final_diam ** 2 / 4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
