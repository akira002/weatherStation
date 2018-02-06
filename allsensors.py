#from termometroDS import Termometro
#term = Termometro()
#term.aggiornaPath('/Users/alessandro/Desktop/Tesi/code/w1_slave2')
#print(term.dammiTemperatura())
#print(term.dammiMin())

import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from termometroDS import Termometro

sensor = BMP085.BMP085()
term = Termometro()
print(term.dammiTemperatura())

for i in range(0,60):
        umidita = Adafruit_DHT.read_retry(22,22)[0]
        temperatura1 = Adafruit_DHT.read_retry(22,22)[1]
        temperatura2 = sensor.read_temperature()
        temperatura3 = term.dammiTemperatura()
        pressione = sensor.read_pressure()
        #necessaria spiegazione della format di python
        print('Temperatura1 = {0:0.01f} C*, Temperatura2 = {1:0.01f} C*, Temperatura3 = {0:0.0001f} C*, Pressione = {2:0.01f} Pa, Umidita = {3:0.01f} %'.format(temperatura1, temperatura2, temperatura3, pressione, umidita))
        time.sleep(1)
