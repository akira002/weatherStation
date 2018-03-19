from sense_hat import SenseHat
import os
sense = SenseHat()

def calibrateTemperature(temperatura):
    #Rilevo la temperatura del processore
    tmp = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = tmp.read()
    cputemp = cputemp.replace('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    cputemp = float(cputemp)
    #correggo la temperatura rilevata
    temperatura = temperatura - (cputemp - temperatura)/1.5
    return temperatura

# Definisco i colori rosso e verde
red = (255, 0, 0)
green = (0, 255, 0)

while True:

      # Effettuo la lettura delle grandezze da tutti e tre i sensori
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    #Effettuo la calibrazione della temperatura
    t = calibrateTemperature(t)
     # Arrotondo i valori alla prima cifra decimale
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    # Creo il messaggio
    # str() converte i valori in stringhe in modo che possano essere concatenati
    message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)

    if t > 18.3 and t < 26.7:
        bg = green
    else:
        bg = red
    # Mostro il messaggio a scorrimento
    sense.show_message(message, scroll_speed=0.05, back_colour=bg)
