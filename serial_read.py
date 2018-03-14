#competenze acquisite: porta seriale, codifica UTF-8, operazioni su stringhe python
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
        read_serial=ser.readline()
        msg = read_serial.decode('utf-8')
        msg = msg[0:len(msg)-1]
        print(msg)
