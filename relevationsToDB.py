import os
import MySQLdb as mdb
import datetime
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from termometroDS import Termometro
from umidterr import UmidometroTerreno

sensor = BMP085.BMP085()
term = Termometro()
umid = UmidometroTerreno()


databaseUsername="username" #L'username di mysql, solitamente root
databasePassword="password" #La password di mysql
databaseName="WordpressDB" #Il nome del database

def saveToDatabase(temperature, pressure, humidity, humidsoil):
        con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
        currentDate=datetime.datetime.now().date()
        hour = datetime.datetime.now().time()
        with con:
            cur=con.cursor()
            cur.execute("INSERT INTO relevations (temperature, pressure, humidity, humidsoil,dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s, %s, %s)",(temperature,pressure, humidity, humidsoil,currentDate, hour))
            print("Rilevazioni salvate sul database")
            return "true"


#controlla se la tabella gia' esiste o se dobbiamo crearne una
try:
        queryFile=open("wordpress/createTable.sql","r")

        con=mdb.connect("localhost", databaseUsername,databasePassword,databaseName)
        currentDate=datetime.datetime.now().date()

        with con:
            line=queryFile.readline()
            query=""
            while(line!=""):
                query+=line
                line=queryFile.readline()

            cur=con.cursor()
            cur.execute(query)

            #Rinomina il file, perche' non abbiamo bisogno di ricreare la tabella ogni volta che lo script viene eseguito
            queryFile.close()
            os.rename("wordpress/createTable.sql","wordpress/createTable.sql.bkp")


except IOError:
	pass #table has already been created


humidity = Adafruit_DHT.read_retry(22,22)[0]
temperature = term.dammiTemperatura()
pressure = sensor.read_pressure()/100
humidsoil = umid.dammiUmidita()
saveToDatabase(temperature, pressure, humidity, humidsoil)
