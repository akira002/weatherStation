import sys
import time
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from termometroDS import Termometro
from umidterr import UmidometroTerreno

sensor = BMP085.BMP085()
term = Termometro()
umid = UmidometroTerreno()

for i in range(0,60):
        umidita = Adafruit_DHT.read_retry(22,22)[0]
        temperatura1 = Adafruit_DHT.read_retry(22,22)[1]
        temperatura2 = sensor.read_temperature()
        temperatura3 = term.dammiTemperatura()
        pressione = sensor.read_pressure()/100
        umidterreno = umid.dammiUmidita()
        print('Temperatura1 = {0:0.01f} C*, Temperatura2 = {1:0.01f} C*, Temperatura3 = {2:0.0001f} C*, Pressione = {3:0.01f} hPa, Umidita = {4:0.01f} %, Umidita Terreno = {5:0.01f} %'.format(temperatura1, temperatura2, temperatura3, pressione, umidita, umidterreno))
        time.sleep(1)
