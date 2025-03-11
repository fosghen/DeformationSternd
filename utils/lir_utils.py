import hid
import serial

modules_id = \
        {"sys": 0,
         "sensor": 1,
         "rs485": 2,
         "io": 3,
         "virtual_io": 4,
         "func_sig": 5,
         "positioner": 6,
         "gmachine": 7,
         "telemetry": 8,
         "zone": 9,
         "ethernet": 10,
         "gui": 11,
         "math": 12,
         "manage": 13,
         "radio": 14}


standard_commands = {
    "get_module_info": 0x00,            # Запрос информации о модуле
    "get_submodule_num": 0x01,          # Запрос количества подмодулей
    "get_submodule_info": 0x02,         # Запрос информации о подмодуле
    "get_module_state": 0x03,           # Запрос текущего состояния модуля
    "set_module_state": 0x04,           # Установить состояние модуля
    "get_module_mode": 0x05,            # Запрос текущего режима модуля
    "set_module_mode": 0x06,            # Установить режим работы модуля
    "get_module_setup": 0x07,           # Запрос текущих настроек модуля
    "set_module_setup": 0x08,           # Установить настройки модуля
    "get_submodule_setup": 0x09,        # Запрос текущих настроек активного подмодуля
    "set_submodule_setup": 0x0A,        # Установить настройки активного подмодуля
    "save_setup_to_nvram": 0x0B,        # Сохранить настройки модуля и подмодуля в энергонезависимую память
    "load_setup_from_nvram": 0x0C,      # Загрузить настройки модуля и подмодуля из энергонезависимой памяти
    "get_list_conlict_modules": 0x0D    # Запрос списка конфликтующих модулей
}


extended_standard_commands = {
    "get_module_count": 0x14,           # Запрос количества модулей в устройстве
    "get_device_id": 0x15,              # Запрос идентификатора устройства
    "get_hardware_version": 0x16,       # Запрос аппаратной версии устройства
    "get_software_version": 0x17,       # Запрос программной версии устройства
    "get_serial_number": 0x18,          # Запрос серийного номера устройства
    "save_system_setup": 0x19,          # Сохранить настройки всей системы
    "load_system_setup": 0x1A,          # Загрузить настройки всей системы
    "get_system_setup_status": 0x1B,    # Запрос состояния настроек всех модулей устройства
    "get_system_modules_state": 0x1C,   # Запрос состояния всех модулей устройства
    "set_marker": 0x1D,                 # Установить маркер
    "get_coordinate_buffer": 0x1E,      # Запрос содержимого буфера координат
    "get_device_modification": 0x1F,    # Запрос модификации устройства
    "enter_firmware_update_mode": 0x70  # Перевод устройства в режим обновления прошивки
}


sensor_commands = {
    # Команды датчика
    "update_sensor_reading": 0x14,        # Обновить показания датчика
    "get_sensor_reading": 0x15,           # Запрос показаний датчика
    "set_current_coordinate_system": 0x16, # Установить текущую систему отсчета
    "get_current_coordinate_system": 0x17, # Запрос текущей системы отсчета
    "set_sensor_offset": 0x18,            # Установить смещение по датчику
    "set_manual_offset": 0x19,            # Установить смещение вручную
    "get_sensor_offset": 0x1A,            # Запрос текущего смещения
    "get_error_count": 0x1B,              # Запрос количества ошибок датчика
    "reset_error_counter": 0x1C,          # Сбросить счетчик ошибок датчика
    "get_last_error_status": 0x1D,        # Запрос последней ошибки датчика
    "save_current_position": 0x1E,        # Сохранить текущую позицию для восстановления
    "restore_saved_position": 0x1F,       # Восстановить сохраненную позицию
    "init_correction_process": 0x32,      # Инициализация процесса коррекции
    "get_correction_point": 0x33,         # Получить информацию о точке коррекции
    "get_correction_point_count": 0x34,   # Запрос количества точек в таблице коррекции
    "add_correction_point": 0x35,         # Добавить точку коррекции
    "save_correction_table": 0x36,        # Сохранить таблицу коррекции
    "abort_correction_process": 0x37,     # Прервать процесс коррекции
    "delete_correction_point": 0x38,      # Удалить точку коррекции
    "edit_correction_point": 0x39,        # Отредактировать точку коррекции
    "add_manual_correction_point": 0x3A,  # Добавить вручную точку коррекции
    "get_correction_field_size": 0x3B,    # Запрос размера поля данных коррекции
    
    # Команды подмодуля инкрементного датчика
    "start_reference_mark_search": 0x3C,  # Начать поиск референтной метки
    "reset_reference_mark_capture": 0x3D, # Сбросить захват референтной метки
    "cancel_reference_mark_search": 0x3E, # Отменить поиск референтной метки
    "reset_counter": 0x3F,                # Обнулить показания счетчика
    
    # Команды подмодуля SSI
    "reset_turn_counter": 0x3C,           # Обнулить счетчик оборотов (SSI)
    
    # Команды подмодуля BISS C
    "reset_turn_counter_bissc": 0x3C,     # Обнулить счетчик оборотов (BISS-C)
    "write_registers_to_memory": 0x3E,    # Запись регистров EDS в память устройства
    "read_registers_from_memory": 0x3F,   # Чтение регистров EDS из памяти устройства
    "start_register_sync": 0x40           # Запуск синхронизации значений регистров EDS
}

io_commands = {
    # Команды портов входов/выходов
    "set_outputs": 0x14,                  # Установка выходов
    "get_outputs": 0x15,                  # Получение сосостяния выходов
    "get_inputs": 0x16,                   # Получить состояние входов
    "set_single_output": 0x17,            # Установить один выход
    "get_num_io": 0x18,                   # Запросить количество входов/выходов
}


def connect(vid: int,
            pid: int) -> hid.device:
    """
    Подключение к устройству LIR.

    vid: vendor_id in hex.
    pid: product_id in hex.
    Эту информацию можно найти в диспетчере устройств.
    """
    device = hid.device()
    device.open(vid,
                pid)
    device.set_nonblocking(True)

    return device


def send_buffer(dev: hid.device,
                buffer: list):
    if len(buffer) > 255:
        print("Буфер слишком большой")
        return

    dev.write(buffer)


def read_buffer(dev: hid.device,
                timeout: int) -> list:
    buffer = dev.read(255,
                      timeout)

    return buffer


def create_massage(buffer: list,
                   module: int,
                   command: int,
                   data: int | list | None):
    if isinstance(data, int):
        if 255 < len(buffer) + 4:
            print("Переполнение буфера")
            return
        buffer.extend([4, module, command, data])

    elif isinstance(data, list):
        if 255 < len(buffer) + len(data):
            print("Переполнение буфера")
            return
        buffer.extend([len(data) + 3, module, command])

        for data_tmp in data:
            buffer.extend([data_tmp])

    else:
        if 255 < len(buffer) + 3:
            print("Переполнение буфера")
            return
        buffer.extend([3, module, command])

    buffer[1] += 1


def create_buffer() -> list:
    buffer = [0, 0]
    return buffer


def decode_buff(buffer: list) -> None:
    num_bytes = [0, buffer[1]]
    for i in range(buffer[0] - 1):
        num_bytes.append(num_bytes[-1] + buffer[num_bytes[-1] + 1])

    for i in range(len(num_bytes) - 1):
        massage = buffer[num_bytes[i] + 1: num_bytes[i + 1] + 1]

        print("Размер ответа:", massage[0])
        print("Ответ от блока:", massage[1])
        print("Ответ на команду:", massage[2])

        if len(massage[3:]) == 1:
            if massage[3] == 0xF0:
                print("Всё ОК")

            elif massage[3] == 0x0F:
                print("Ошибка")

            else:
                print("Данные ответа:", massage[3:])

        else:
            print("Данные ответа:", massage[3:])

        print()


def start_setup(dev: hid.device) -> None:
    buffer = create_buffer()

    create_massage(buffer,
                   modules_id["sensor"],
                   standard_commands["set_module_state"],
                   0)

    create_massage(buffer,
                   modules_id["io"],
                   standard_commands["set_module_state"],
                   0)

    create_massage(buffer,
                   modules_id["sensor"],
                   standard_commands["get_module_state"],
                   None)

    create_massage(buffer,
                   modules_id["sensor"],
                   sensor_commands["set_current_coordinate_system"],
                   3)

    create_massage(buffer,
                   modules_id["sensor"],
                   sensor_commands["update_sensor_reading"],
                   None)

    send_buffer(dev, buffer)
    buffer_out = read_buffer(dev, 20)

    decode_buff(buffer_out)

def decode_linear_buff(buffer: list) -> float:
    num_bytes = [0, buffer[1]]
    for i in range(buffer[0] - 1):
        num_bytes.append(num_bytes[-1] + buffer[num_bytes[-1] + 1])

    for i in range(len(num_bytes) - 1):
        massage = buffer[num_bytes[i] + 1: num_bytes[i + 1] + 1]

        coords_full = 0x00000000

        for i in range(8):
            coords_full |= massage[3:][i] << 8 * i
        
        if (coords_full - 0xffffffffffffffff) > -430 * 10000:
            coords_full = coords_full - 0xffffffffffffffff
        
        # print("Показания датчика: ", coords_full / 10, " мкм")

    return coords_full / 10


def read_linear_encoder(dev: hid.device) -> float:
    buffer = create_buffer()

    create_massage(buffer,
                   modules_id["sensor"],
                   sensor_commands["get_sensor_reading"],
                   3)

    send_buffer(dev, buffer)
    buffer_out = read_buffer(dev, 20)

    return decode_linear_buff(buffer_out)

def set_zero_linear_encoder(dev: hid.device) -> None:
    buffer = create_buffer()

    create_massage(buffer,
                   modules_id["sensor"],
                   sensor_commands["reset_counter"],
                   None)
    send_buffer(dev, buffer)
    buffer_out = read_buffer(dev, 20)
    decode_buff(buffer_out)


def run_step_motor(dev: hid.device,
                   dir: int,
                   div: int) -> None:
    buffer = create_buffer()
    create_massage(buffer,
                   modules_id["virtual_io"],
                   standard_commands["get_module_setup"],
                   None)

    send_buffer(dev, buffer)
    setup_vio = read_buffer(dev, 20)
    setup_vio[100] = div
    setup_vio[132] = 0b00000010 & dir << dir
    buffer = create_buffer()
    create_massage(buffer,
                   modules_id["virtual_io"],
                   standard_commands["set_module_setup"],
                   setup_vio[4: 172 + 4])
    send_buffer(dev, buffer)
    decode_buff(read_buffer(dev, 20))

    buffer = create_buffer()
    create_massage(buffer,
                   modules_id["func_sig"],
                   standard_commands["get_module_setup"],
                   None)

    send_buffer(dev, buffer)
    setup_func_sig = read_buffer(dev, 20)
    setup_func_sig[129 + 0] = 1 # Вкл
    setup_func_sig[129 + 1] = 3 # Таймер
    setup_func_sig[129 + 2] = 0 # Тригер 0
    setup_func_sig[129 + 3] = 0 # Номер таймера
    setup_func_sig[129 + 4] = 0 # Выходы 1
    setup_func_sig[129 + 5] = 2 # Третий выход

    buffer = create_buffer()
    create_massage(buffer,
                   modules_id["func_sig"],
                   standard_commands["set_module_setup"],
                   setup_func_sig[4: 149 + 4])
    send_buffer(dev,
                buffer)
    decode_buff(read_buffer(dev, 20))

    
def init_serial() -> serial.serialwin32.Serial:
    ser = serial.Serial('COM15', 9600, timeout=0,)
    return ser    


def get_force(ser: serial.serialwin32.Serial) -> float:
    data = ser.read_all()
    data_splited = data.decode("UTF-8").split("\r\n")
    for elem in data_splited:
        if len(elem) == 8:
            return str_to_float(elem)
        
def str_to_float(data: str) -> float:
    if data.split(" ")[0] == '-' and data.split(" ")[-1] != '':
        return -float(data.split(" ")[1])
    else:
        if data.split(" ")[-1] != '':
            return float(data.split(" ")[-1])
    return 0

# Пример настройки виртуальных портов
setup_vio = [#---- Настройки входов
        0, 0, 0, 0, # №1 # Инвертировать вход
        0, 0, 0, 0, # Установить вход в “1”
        #---------
        0, 0, 0, 0, # №2
        0, 0, 0, 0,
        #---------
        0, 0, 0, 0, # №3
        0, 0, 0, 0,
        #----------
        0, 0, 0, 0, # №4
        0, 0, 0, 0,
        #---- Настройки логических входов
        0,          # №1
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №2
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №3
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №4
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №5
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №6
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №7
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #----------
        0,          # №8
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        #---- Настройки таймеров
        1, 0, 0, 0, # №1
        0,
        0, 0, 0,
        #----------
        0, 0, 0, 0, # №2
        0,
        0, 0, 0,
        #----------
        0, 0, 0, 0, # №3
        0,
        0, 0, 0,
        #----------
        0, 0, 0, 0, # №4
        0,
        0, 0, 0,
        #---- Настройки выходов
        0, 0, 0, 0, # №1
        #----------
        0, 0, 0, 0, # №2
        #----------
        0, 0, 0, 0, # №3
        #---- Настройки логических выходов
        0,          # №1
        1,
        0,
        0,
        #----------
        0,          # №2
        1,
        0,
        0,
        #----------
        0,          # №3
        1,
        0,
        0,
        #----------
        0,          # №4
        1,
        0,
        0,
        #----------
        0,          # №5
        1,
        0,
        0,
        #----------
        0,          # №6
        1,
        0,
        0,
        #----------
        0,          # №7
        1,
        0,
        0,
        #----------
        0,          # №8
        1,
        0,
        0]


setup_func_sig = [# ---- Настройки входных сигналов
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    # ---- Настройки выходных сигналов
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    0, 0, 0,
                    # --- -Настройки сигналов байпаса
                    1, 3, 0, 0, 0, 2,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0]
