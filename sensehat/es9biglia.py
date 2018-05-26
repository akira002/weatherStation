from sense_hat import SenseHat
import random
import time
sense = SenseHat()

red = (255, 0, 0)
white = (255,255,255)

x=4
y=3
#il gioco continua all'infinito
while(1):
    # genero casualmente le coordinate del pixel corrispondente alla buca
    xtarget = random.randint(0,7)
    ytarget = random.randint(0,7)
    #prevengo che la buca venga generata sotto la pallina
    while (xtarget==x and ytarget==y):
        xtarget = random.randint(0,7)
        ytarget = random.randint(0,7)
        #concetto while: finchè non ho raggiunto l'obiettivo
    while (x!=xtarget or y!=ytarget):
        sense.clear()
        #setto il pixel corrispondente alla buca
        sense.set_pixel(xtarget, ytarget, red)
        # setto il pixel corrispondente alla biglia
        sense.set_pixel(x, y, white)
        o = sense.get_accelerometer_raw()
        pitch = o["x"]
        roll = o["y"]
        if (pitch > 0.4 and x < 7):
            x = x+1
        if (pitch < -0.4 and x > 0):
            x = x-1
        if (roll > 0.4 and y < 7):
            y = y+1
        if (roll < -0.4 and y > 0):
            y = y-1
        time.sleep(1)
    sense.show_message("Hai Vinto!")
