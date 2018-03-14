import time
from sense_hat import SenseHat
sense = SenseHat()

with open('rilevazioni.csv','w') as file:
    while True:

          # Effettua le rilevazioni con tutti e tre i sensori
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        # Arrotonda i valori alla prima cifra decimale
        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

          #Ottengo un timestamp
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    # str() converte i valori numerici in stringhe, in modo che possano essere concatenati
        line =  date + ", "+str(t)+", "+str(p)+", "+str(h)
        file.write(line)
        file.write('\n')
        time.sleep(1)
