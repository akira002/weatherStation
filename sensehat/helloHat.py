from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
blu = (0,0,55)
rosso = (100, 0, 0)
#sense.show_message("Hello World",0.05,text_colour=rosso, back_colour=blu)
rand1 = (randint(0,255), randint(0,255), randint(0,255))
rand2 = (randint(0,255), randint(0,255), randint(0,255))
sense.show_letter("A", text_colour=rand1, back_colour=rand2)
sleep(0.5)
sense.show_letter("L", text_colour=rand2, back_colour=rand1)
sleep(0.5)
sense.clear()
