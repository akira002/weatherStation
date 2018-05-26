from sense_hat import SenseHat
import time
#spiegare l'if
#matrici con nomi anonimi, esercizio sull'if in cui devono testarle
sense = SenseHat()
def disegnaRetta(angolo):
    r = (255, 0, 0)
    b = (0, 0, 255)
    w = (0, 0, 0)
    if angolo < 45:
        output=[w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                b,b,b,b,r,r,r,r,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w
                ]
        sense.set_pixels(output)
    elif angolo < 90:
             output=[w,w,w,w,w,w,w,r,
                w,w,w,w,w,w,r,w,
                w,w,w,w,w,r,w,w,
                w,w,w,w,r,w,w,w,
                w,w,w,b,w,w,w,w,
                w,w,b,w,w,w,w,w,
                w,b,w,w,w,w,w,w,
                b,w,w,w,w,w,w,w
                ]
             sense.set_pixels(output)
    elif angolo < 135:
            output=[w,w,w,r,w,w,w,w,
                w,w,w,r,w,w,w,w,
                w,w,w,r,w,w,w,w,
                w,w,w,r,w,w,w,w,
                w,w,w,b,w,w,w,w,
                w,w,w,b,w,w,w,w,
                w,w,w,b,w,w,w,w,
                w,w,w,b,w,w,w,w
                ]
            sense.set_pixels(output)
    elif angolo < 180:
            output=[r,w,w,w,w,w,w,w,
            w,r,w,w,w,w,w,w,
            w,w,r,w,w,w,w,w,
            w,w,w,r,w,w,w,w,
            w,w,w,w,b,w,w,w,
            w,w,w,w,w,b,w,w,
            w,w,w,w,w,w,b,w,
            w,w,w,w,w,w,w,b
            ]
            sense.set_pixels(output)
    elif angolo < 225:
            output=[w,w,w,w,w,w,w,w,
                    w,w,w,w,w,w,w,w,
                    w,w,w,w,w,w,w,w,
                    r,r,r,r,b,b,b,b,
                    w,w,w,w,w,w,w,w,
                    w,w,w,w,w,w,w,w,
                    w,w,w,w,w,w,w,w,
                    w,w,w,w,w,w,w,w
                    ]
            sense.set_pixels(output)
    elif angolo < 270:
            output=[w,w,w,w,w,w,w,b,
            w,w,w,w,w,w,b,w,
            w,w,w,w,w,b,w,w,
            w,w,w,w,b,w,w,w,
            w,w,w,r,w,w,w,w,
            w,w,r,w,w,w,w,w,
            w,r,w,w,w,w,w,w,
            r,w,w,w,w,w,w,w
            ]
            sense.set_pixels(output)
    elif angolo < 315:
            output=[w,w,w,b,w,w,w,w,
            w,w,w,b,w,w,w,w,
            w,w,w,b,w,w,w,w,
            w,w,w,b,w,w,w,w,
            w,w,w,r,w,w,w,w,
            w,w,w,r,w,w,w,w,
            w,w,w,r,w,w,w,w,
            w,w,w,r,w,w,w,w
            ]
            sense.set_pixels(output)
    #TODO va bene anche un else?
    elif angolo < 360:
            output=[b,w,w,w,w,w,w,w,
                    w,b,w,w,w,w,w,w,
                    w,w,b,w,w,w,w,w,
                    w,w,w,b,w,w,w,w,
                    w,w,w,w,r,w,w,w,
                    w,w,w,w,w,r,w,w,
                    w,w,w,w,w,w,r,w,
                    w,w,w,w,w,w,w,r
                    ]
            sense.set_pixels(output)

while True:
    compass = sense.get_compass()
    print ("Nord ", compass)
    disegnaRetta(compass)
    time.sleep(0.1)
