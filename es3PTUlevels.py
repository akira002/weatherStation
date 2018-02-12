from sense_hat import SenseHat, ACTION_RELEASED
sense = SenseHat()

maxtemp = 55
mintemp = -15
#fonte wikipedia, minpressure livello del mare con tornado
maxpressure = 1085
minpressure = 870
#non necessario, si puo'usare direttamente il valore
maxhumid = 100
minhumid = 0

#otto livelli di riempimento della matrice
r = (55, 0, 0)
w = (55, 55, 55)

zero = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
        ]


uno = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r
        ]

due = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]

tre = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]

quattro = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]


cinque = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]


sei = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]

sette = [
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]


otto = [
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r,
        r,r,r,r,r,r,r,r
        ]

def printLevelOnMatrix(perc):
    if perc == 0 :
        sense.set_pixels(zero)
    if perc > 0 and perc <= 12.5:
        sense.set_pixels(uno)
    if perc > 12.5 and perc <= 25:
        sense.set_pixels(due)
    if perc > 25 and perc <= 37.5:
        sense.set_pixels(tre)
    if perc > 37.5 and perc <= 50:
        sense.set_pixels(quattro)
    if perc > 50 and perc <= 62.5:
        sense.set_pixels(cinque)
    if perc > 62.5 and perc <= 75:
        sense.set_pixels(sei)
    if perc > 75 and perc <= 87.5:
        sense.set_pixels(sette)
    if perc > 87.5 and perc <= 100:
        sense.set_pixels(otto)


#Definisci le funzioni pressione, temperatura e umidita'
def pressure(event):
  if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("pressione")
      p=sense.get_pressure()
      print(p)
      ampiezzaScala = maxpressure - minpressure
      Pmin = p - minpressure #dovrebbe sempre essere positivo
      print(Pmin)
      Pperc = Pmin/ampiezzaScala*100
      print(Pperc)
      printLevelOnMatrix(Pperc)

def temperature(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("temperatura")
      t=sense.get_temperature()
      print(t)
      ampiezzaScala = maxtemp - mintemp
      Tmin = t - mintemp #dovrebbe sempre essere positivo
      print(Tmin)
      Tperc = Tmin/ampiezzaScala*100
      print(Tperc)
      printLevelOnMatrix(Tperc)

def humidity(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
        sense.show_message("umidita")
        h=sense.get_humidity()
        print(h)
        ampiezzaScala = maxhumid - minhumid
        Hmin = h - minhumid #dovrebbe sempre essere positivo
        print(Hmin)
        #superfluo perchél'umidita e' gia' in percentuale
        Hperc = Hmin/ampiezzaScala*100
        print(Hperc)
        printLevelOnMatrix(Hperc)

while True:
   sense.stick.direction_up = pressure
   sense.stick.direction_left = temperature
   sense.stick.direction_right = humidity
   sense.stick.direction_middle = sense.clear
