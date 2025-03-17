import lir_utils as lu
import serial
import hid

def get_value_from_sensors(dinamometr: serial.serialwin32.Serial, linear_encoder: hid.device) -> tuple[float, float]:
    dino_data = dinamometr.read_all()  # Считываем данные с динамометра
    line_data = -lu.read_linear_encoder(linear_encoder) # Считываем данные с линейки

    dino_data = dino_data.decode().split("\r\n")

    try:
        dino_data = float(dino_data[-1])
    except:
        dino_data = float(dino_data[-2])

    return dino_data, line_data