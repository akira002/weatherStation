from sense_hat import SenseHat, ACTION_RELEASED
sense = SenseHat()

r = (55, 0, 0)
w = (55, 55, 55)

#i vari font delle diverse cifre sulla matrice di led 3x8 (per lasciare spazio)
empty = [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w                                                                 ]

zero = [
        r,r,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,r,r,w
        ]


uno = [
        r,r,w,w,
        w,r,w,w,
        w,r,w,w,
        w,r,w,w,
        w,r,w,w,
        w,r,w,w,
        w,r,w,w,
        r,r,r,w
        ]

due = [
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,w,r,w,
        r,r,r,w,
        r,w,w,w,
        r,w,w,w,
        r,r,r,w
        ]

tre = [
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,w,r,w,
        r,r,r,w
        ]

quattro = [
        w,w,r,w,
        w,r,w,w,
        r,w,w,w,
        r,w,r,w,
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,w,r,w
        ]


cinque = [
        r,r,r,w,
        r,w,w,w,
        r,w,w,w,
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,w,r,w,
        r,r,r,w
        ]


sei = [
        r,r,r,w,
        r,w,w,w,
        r,w,w,w,
        r,r,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,r,r,w
        ]


sette = [
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,r,w,w,
        r,w,w,w,
        r,w,w,w,
        r,w,w,w,
        r,w,w,w
        ]


otto = [
        r,r,r,w,
        r,w,r,w,
        r,w,r,w,
        r,r,r,w,
        r,w,r,w,
        r,w,r,w,
        r,w,r,w,
        r,r,r,w
        ]

nove = [
        r,r,r,w,
        r,w,r,w,
        r,w,r,w,
        r,r,r,w,
        w,w,r,w,
        w,w,r,w,
        w,w,r,w,
        r,r,r,w
        ]

def displayDigits(decimal, unity):
    output = empty
    for i in range(0,8):
        for j in range(0, 4):
            if decimal == 0:
                output[i*8+j]= zero[i*4+j]
            if decimal == 1:
                output[i*8+j]= uno[i*4+j]
            if decimal == 2:
                output[i*8+j]= due[i*4+j]
            if decimal == 3:
                output[i*8+j]= tre[i*4+j]
            if decimal == 4:
                output[i*8+j]= quattro[i*4+j]
            if decimal == 5:
                output[i*8+j]= cinque[i*4+j]
            if decimal == 6:
                output[i*8+j]= sei[i*4+j]
            if decimal == 7:
                output[i*8+j]= sette[i*4+j]
            if decimal == 8:
                output[i*8+j]= otto[i*4+j]
            if decimal == 9:
                output[i*8+j]= nove[i*4+j]
    for i in range(0,8):
        for j in range(4, 8):
            if unity == 0:
                output[i*8+j]= zero[i*4+j-4]
            if unity == 1:
                output[i*8+j]= uno[i*4+j-4]
            if unity == 2:
                output[i*8+j]= due[i*4+j-4]
            if unity == 3:
                output[i*8+j]= tre[i*4+j-4]
            if unity == 4:
                output[i*8+j]= quattro[i*4+j-4]
            if unity == 5:
                output[i*8+j]= cinque[i*4+j-4]
            if unity == 6:
                output[i*8+j]= sei[i*4+j-4]
            if unity == 7:
                output[i*8+j]= sette[i*4+j-4]
            if unity == 8:
                output[i*8+j]= otto[i*4+j-4]
            if unity == 9:
                output[i*8+j]= nove[i*4+j-4]

    sense.set_pixels(output)

#Definisci le funzioni pressione, temperatura e umidita'
def pressure(event):
  if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("pressione", scroll_speed=0.03)
      p=sense.get_pressure()
      print(p)
      p = round(p)
      sense.show_message(str(p), text_colour = r)

def temperature(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("temperatura", scroll_speed=0.03)
      t=sense.get_temperature()
      t = round(t)
      decimal = round((t-t%10)/10)
      unity = round(t%10)
      print(t)
      displayDigits(decimal, unity)

def humidity(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
        sense.show_message("umidita", scroll_speed = 0.03)
        h=sense.get_humidity()
        h = round(h)
        decimal = round((h-h%10)/10)
        unity = round(h%10)
        print(h)
        displayDigits(decimal, unity)

while True:
   sense.stick.direction_up = pressure
   sense.stick.direction_left = temperature
   sense.stick.direction_right = humidity
   sense.stick.direction_middle = sense.clear