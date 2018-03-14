import RPi.GPIO as GPIO ## Importo la libreria GPIO
import time ## Importo la libreria time, permette l'uso di 'sleep'

#Usa la numerazione della board per i pin
GPIO.setmode(GPIO.BCM)

#Definisce una funzione chiamata Lampeggio
def Lampeggio(pin,numVolte,intervallo):
    GPIO.setup(pin, GPIO.OUT)
    #Esegue il ciclo numVolte volte
    for i in range(0,numVolte):
        print("Iterazione " + str(i+1))
        #Accende il pin desiderato
        GPIO.output(pin,True)
        #Attesa di intervallo secondi
        time.sleep(intervallo)
        #Spegne il pin desiderato
        GPIO.output(pin,False)
        #Attesa di intervallo secondi
        time.sleep(intervallo)
    print("Fatto") 
    GPIO.cleanup()

iterazioni = input("Inserisci il numero di lampeggi: ")
durata = input("Inserisci la durata in secondi di ogni lampeggio: ")
pin = input("inserisci il numero del pin al quale hai collegato il led: ")

Lampeggio(int(pin),int(iterazioni),float(durata))

