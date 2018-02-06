from sense_hat import SenseHat
sense = SenseHat()

maxtemp = 55
mintemp = -15
#fonte wikipedia, minpressure livello del mare con tornado
maxpressure = 1085
minpressure = 870
#non necessario, si può usare direttamente il valore
maxhumid = 100
minhumid = 0

#otto livelli di riempimento della matrice
r = (255, 0, 0)
w = (255, 255, 255)

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


#Definisci le funzioni pressione, temperatura e umidita'
def pressure(event):
  if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick è rilasciato
      sense.show_message("pressione")
      p=sense.get_pressure()
      print(p)
      ampiezzaScala = maxpressure - minpressure
      Pmin = p - minpressure #dovrebbe sempre essere positivo
      print(Pmin)
      Pperc = Pmin/ampiezzaScala*100
      print(Pperc)
      #più elegante con uno switch, ma forse i ragazzi non lo conoscono
      if Pperc == 0 :
        sense.set_pixels(zero)
      if Pperc > 0 and Pperc <= 12.5:
        sense.set_pixels(uno)
      if Pperc > 12.5 and Pperc <= 25:
        sense.set_pixels(due)
      if Pperc > 25 and Pperc <= 37.5:
        sense.set_pixels(tre)
      if Pperc > 37.5 and Pperc <= 50:
        sense.set_pixels(quattro)
      if Pperc > 50 and Pperc <= 62.5:
        sense.set_pixels(cinque)
      if Pperc > 62.5 and Pperc <= 75:
        sense.set_pixels(sei)
      if Pperc > 75 and Pperc <= 87.5:
        sense.set_pixels(sette)
      if Pperc > 87.5 and Pperc <= 100:
        sense.set_pixels(otto)

def temperature(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick è rilasciato
      sense.show_message("temperatura")
      t=sense.get_temperature()
      print(t)
      ampiezzaScala = maxtemp - mintemp
      Tmin = t - mintemp #dovrebbe sempre essere positivo
      print(Tmin)
      Tperc = Tmin/ampiezzaScala*100
      print(Tperc)
      #più elegante con uno switch, ma forse i ragazzi non lo conoscono
      if Tperc == 0 :
      sense.set_pixels(zero)
      if Tperc > 0 and Tperc <= 12.5:
        sense.set_pixels(uno)
      if Tperc > 12.5 and Tperc <= 25:
        sense.set_pixels(due)
      if Tperc > 25 and Tperc <= 37.5:
        sense.set_pixels(tre)
      if Tperc > 37.5 and Tperc <= 50:
        sense.set_pixels(quattro)
      if Tperc > 50 and Tperc <= 62.5:
        sense.set_pixels(cinque)
      if Tperc > 62.5 and Tperc <= 75:
        sense.set_pixels(sei)
      if Tperc > 75 and Tperc <= 87.5:
        sense.set_pixels(sette)
      if Tperc > 87.5 and Tperc <= 100:
        sense.set_pixels(otto)


def humidity(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick è rilasciato
        sense.show_message("umidita")
        h=sense.get_humidity()
        print(h)
        ampiezzaScala = maxhumid - minhumid
        Hmin = h - minhumid #dovrebbe sempre essere positivo
        print(Hmin)
        Hperc = Hmin/ampiezzaScala*100
        print(Hperc)
        #più elegante con uno switch, ma forse i ragazzi non lo conoscono
        if Hperc == 0 :
            sense.set_pixels(zero)
        if Hperc > 0 and Hperc <= 12.5:
            sense.set_pixels(uno)
        if Hperc > 12.5 and Hperc <= 25:
            sense.set_pixels(due)
        if Hperc > 25 and Hperc <= 37.5:
            sense.set_pixels(tre)
        if Hperc > 37.5 and Hperc <= 50:
            sense.set_pixels(quattro)
        if Hperc > 50 and Hperc <= 62.5:
            sense.set_pixels(cinque)
        if Hperc > 62.5 and Hperc <= 75:
            sense.set_pixels(sei)
        if Hperc > 75 and Hperc <= 87.5:
            sense.set_pixels(sette)
        if Hperc > 87.5 and Hperc <= 100:
            sense.set_pixels(otto)


while True:
   sense.stick.direction_up = pressure
   sense.stick.direction_left = temperature
   sense.stick.direction_right = humidity
   sense.stick.direction_middle = sense.clear
