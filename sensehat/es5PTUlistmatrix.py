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

r = (55, 0, 0)
w = (55, 55, 55)

def generateMatrix(numeroBarre):
    mat = []
    #faccio le barre vuote
    for i in range(0,8-numeroBarre):
        line = []
        for j in range(0,8):
            line.append(w)
        mat.append(line)
    #faccio le barre piene
    for i in range(8-numeroBarre+1,9):
        line = []
        for j in range(0,8):
            line.append(r)
        mat.append(line)
    return mat

def matrixToList(matrice):
    lst = []
    for i in range(0,8):
        for j in range(0,8):
            lst.append(matrice[i][j])
    return lst

def printLevelOnMatrix(perc):
    if perc == 0 :
        setMatrixLed(0)
    if perc > 0 and perc <= 12.5:
        setMatrixLed(1)
    if perc > 12.5 and perc <= 25:
        setMatrixLed(2)
    if perc > 25 and perc <= 37.5:
        setMatrixLed(3)
    if perc > 37.5 and perc <= 50:
        setMatrixLed(4)
    if perc > 50 and perc <= 62.5:
        setMatrixLed(5)
    if perc > 62.5 and perc <= 75:
        setMatrixLed(6)
    if perc > 75 and perc <= 87.5:
        setMatrixLed(7)
    if perc > 87.5 and perc <= 100:
        setMatrixLed(8)

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
