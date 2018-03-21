#competenze acquisite: porta seriale, codifica UTF-8, operazioni su stringhe python
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
while True:
        read_serial=ser.readline()
        msg = read_serial.decode('ascii')
        #rimuovo l'ultimo carattere, che è un \n per evitare la doppia andata a capo
        msg = msg[0:len(msg)-1]
        print(msg)
