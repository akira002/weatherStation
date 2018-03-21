import sys
import time

import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

def printDataForSeconds(sec):
    for i in range(0,sec):
        umidita = Adafruit_DHT.read_retry(22,22)[0]
        temperatura1 = Adafruit_DHT.read_retry(22,22)[1]
        temperatura2 = sensor.read_temperature()
        pressione = sensor.read_pressure()
        print('Temperatura1 = {0:0.01f} C*, Temperatura2 = {1:0.01f} C*, Pressione = {2:0.01f} Pa, Umidita = {3:0.01f} %'.format(temperatura1, temperatura2, pressione, umidita))

def returnDataAllSensors():
        temperatura1 = Adafruit_DHT.read_retry(22,22)[1]
        temperatura2 = sensor.read_temperature()
        umidita = Adafruit_DHT.read_retry(22,22)[0]
        pressione = sensor.read_pressure()
        return (temperatura1, temperatura2, umidita, float(pressione)/100)
