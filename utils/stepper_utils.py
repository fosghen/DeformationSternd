import serial

def _send_massage(speed: int,
                 direction: int,
                 count: int,
                 ser: serial.serialwin32.Serial) -> None:
    hi_speed_byte = (speed >> 8) & 0xff
    low_speed_byte = speed & 0xff
    hi_count_byte = (count >> 16) & 0xff
    med_count_byte = (count >> 8) & 0xff
    low_count_byte = count & 0xff
    
    send_massage = [0xde, hi_speed_byte, low_speed_byte, direction + 1, 1, hi_count_byte, med_count_byte, low_count_byte, 0xad]
    
    if ser.write(bytearray(send_massage)) == 9:
        print("Команда отправлена")
        
def start(speed: int,
          direction: int,
          count: int,
          ser: serial.serialwin32.Serial) -> None:
    '''
    1шг(count)=0,25мкм
    direction 0 - едет к шаговому двигателю, 1 - едет от шагового двигателя
    '''
    _send_massage(speed,
                  direction,
                  count,
                  ser)

def stop(ser: serial.serialwin32.Serial) -> None:
    _send_massage(1,
                  0,
                  0,
                  ser)