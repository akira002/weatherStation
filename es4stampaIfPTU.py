# -*- coding: utf-8 -*-
import sys
import time

import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

umidita = Adafruit_DHT.read_retry(22,22)[0]
temperatura1 = Adafruit_DHT.read_retry(22,22)[1]
temperatura2 = sensor.read_temperature()
#Come fare aumentare la pressione atmosferica?
pressione = sensor.read_pressure()
if umidita > 50:
	print("è umido")
else:
	print("è secco")
if temperatura1 > 25:
	print("è caldo")
else:
	print("è freddo")
if pressione > 1000:
	print("c'è alta pressione")
else:
	print("c'è bassa pressione")
