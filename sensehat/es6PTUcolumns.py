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
g = (0, 55, 0)
b = (0, 0, 55)
w = (55, 55, 55)
mat = []

#creo la matrice con tutti i led spenti
for i in range(8):
    line = []
    for j in range(8):
        line.append(w)
    mat.append(line)


def generateMatrixP(numeroBarreP):
    #faccio le barre vuote per la pressione
    for i in range(0,8-numeroBarreP):
        for j in range(0,2):
            mat[i][j]=w
    #faccio le barre piene per la pressione
    for i in range(8-numeroBarreP+1,8):
        for j in range(0,2):
            mat[i][j]=r
    return mat

def generateMatrixT(numeroBarreT):
     #faccio le barre vuote per la temperatura 
    for i in range(0,8-numeroBarreT):
        for j in range(2,5):
            mat[i][j]=w
    #faccio le barre piene per la temperatura
    for i in range(8-numeroBarreT+1,8):
        for j in range(2,5):
            mat[i][j]=g
    return mat

def generateMatrixU(numeroBarreU):
     #faccio le barre vuote per l'umidita
    for i in range(0,8-numeroBarreU):
        for j in range(5,8):
            mat[i][j]=w
    #faccio le barre piene per l'umidita
    for i in range(8-numeroBarreU+1,8):
        for j in range(5,8):
            mat[i][j]=b
    return mat

def matrixToList(matrice):
    lst = []
    for i in range(0,8):
        for j in range(0,8):
            lst.append(matrice[i][j])
    return lst

def percToOctave(perc):
    if perc == 0:
        return 0
    if perc > 0 and perc <= 12.5:
        return 1
    if perc > 12.5 and perc <= 25:
        return 2
    if perc > 25 and perc <= 37.5:
        return 3
    if perc > 37.5 and perc <= 50:
        return 4
    if perc > 50 and perc <= 62.5:
        return 5
    if perc > 62.5 and perc <= 75:
        return 6
    if perc > 75 and perc <= 87.5:
        return 7    
    if perc > 87.5 and perc <= 100:
        return 8

#Definisci le funzioni pressione, temperatura e umidita'
def pressure(event):
  if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("pressione", text_colour=r, scroll_speed=0.01)
      p=sense.get_pressure()
      print(p)
      ampiezzaScala = maxpressure - minpressure
      Pmin = p - minpressure #dovrebbe sempre essere positivo
      print(Pmin)
      Pperc = Pmin/ampiezzaScala*100
      print(Pperc)
      Poctave = percToOctave(Pperc)
      mat = generateMatrixP(Poctave)
      lst = matrixToList(mat)
      sense.set_pixels(lst)

def temperature(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
      sense.show_message("temperatura", text_colour=g, scroll_speed=0.01)
      t=sense.get_temperature()
      print(t)
      ampiezzaScala = maxtemp - mintemp
      Tmin = t - mintemp #dovrebbe sempre essere positivo
      print(Tmin)
      Tperc = Tmin/ampiezzaScala*100
      print(Tperc)
      Toctave = percToOctave(Tperc)
      mat = generateMatrixT(Toctave)
      lst = matrixToList(mat)
      sense.set_pixels(lst)  

def humidity(event):
    if event.action != ACTION_RELEASED: #altrimenti viene eseguito anche quando il joystick e' rilasciato
        sense.show_message("umidita", text_colour=b, scroll_speed=0.01)
        h=sense.get_humidity()
        print(h)
        ampiezzaScala = maxhumid - minhumid
        Hmin = h - minhumid #dovrebbe sempre essere positivo
        print(Hmin)
        #superfluo perchél'umidita e' gia' in percentuale
        Hperc = Hmin/ampiezzaScala*100
        print(Hperc)
        Hoctave = percToOctave(Hperc)
        mat = generateMatrixU(Hoctave)
        lst = matrixToList(mat)
        sense.set_pixels(lst)

while True:
   sense.stick.direction_up = pressure
   sense.stick.direction_left = temperature
   sense.stick.direction_right = humidity
   sense.stick.direction_middle = sense.clear
