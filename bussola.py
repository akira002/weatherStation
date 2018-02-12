from sense_hat import SenseHat
import time

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
    else:
        if angolo < 90:
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
        else:
            if angolo < 135:
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
            else: 
                if angolo < 180:
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
                else: 
                    if angolo < 225:
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
                    else:
                        if angolo < 270:
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
                        else:
                            if angolo < 315:
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
                            else:
                                if angolo < 360:
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

while (1):
    compass = sense.get_compass()
    print ("Nord ", compass)
    disegnaRetta(compass)
    time.sleep(0.5)
