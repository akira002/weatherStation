import time
import RPi.GPIO as GPIO
class LED:
    #GPIO = 18
    def __init__(self, x, y):
        self.GPIO = x
        self.intervallo = y

    def dammiGPIOAttuale(self):
        print(self.GPIO)

    def dammiIntervalloAttuale(self):
        print(self.intervallo)

    def settaGPIO(self, x):
        self.GPIO = x

    def settaIntervallo(self, y):
        self.intervallo = y

    def accendi(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO, GPIO.OUT)
        print("accendo il LED")
        GPIO.output(self.GPIO,True)

    def spegni(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO, GPIO.OUT)
        print("spengo il LED")
        GPIO.output(self.GPIO,False)

    def lampeggia(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO, GPIO.OUT)
        print("accendo il LED")
        GPIO.output(self.GPIO,True)
        time.sleep(self.intervallo)
        print("spengo il LED")
        GPIO.output(self.GPIO, False)

    def lampeggiaPerSecondi(self, durata):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.GPIO, GPIO.OUT)
        print("accendo il LED")
        GPIO.output(self.GPIO,True)
        time.sleep(durata)
        print("spengo il LED")
        GPIO.output(self.GPIO, False)

