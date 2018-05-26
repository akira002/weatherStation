# Importa le librerie necessarie
import RPi.GPIO as GPIO
import time

# Seleziona la modalita' di GPIO
GPIO.setmode(GPIO.BCM)

#Disabilita i warnings
GPIO.setwarnings(False)

# Inserisci il numero della GPIO a cui il LED è collegato
LED = 18

# Seleziona il pin di GPIO del LED come un output
GPIO.setup(LED, GPIO.OUT)

print("accendo il LED")
# Accendi il pin di GPIO
GPIO.output(LED,True)

# Aspetta 5 secondi
time.sleep(5)

print("spengo il LED")
# Spegni il pin di GPIO
GPIO.output(LED,False)
