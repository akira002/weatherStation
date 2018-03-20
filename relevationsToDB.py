import os
import glob
import sys
import re
import time
import subprocess
import MySQLdb as mdb 
import datetime
import sys
import time
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
from termometroDS import Termometro
from umidterr import UmidometroTerreno

sensor = BMP085.BMP085()
term = Termometro()
umid = UmidometroTerreno()
 

databaseUsername="username" #YOUR MYSQL USERNAME, USUALLY ROOT
databasePassword="password" #YOUR MYSQL PASSWORD 
databaseName="WordpressDB" #do not change unless you named the Wordpress database with some other name

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-therm')
 
#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

def saveToDatabase(temperature, pressure, humidity, humidsoil):

        con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
        currentDate=datetime.datetime.now().date()
        #now=datetime.datetime.now()
        #midnight=datetime.datetime.combine(now.date(),datetime.time())
        #minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$
        #hour=time.strftime("%H:%M:%S", time.gmtime())
        hour = datetime.datetime.now().time()
        #print(datetime.datetime.now())
        with con:
            cur=con.cursor()

            cur.execute("INSERT INTO relevations (temperature, pressure, humidity, humidsoil,dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s, %s, %s)",(temperature,pressure, humidity, humidsoil,currentDate, hour))

            print("Saved relevations")
            return "true"


#check if table is created or if we need to create one
try:
        queryFile=open("createTable.sql","r")

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

            #now rename the file, because we do not need to recreate the table everytime this script is run
            queryFile.close()
            os.rename("createTable.sql","createTable.sql.bkp")


except IOError:
	pass #table has already been created


humidity = Adafruit_DHT.read_retry(22,22)[0]
temperature = term.dammiTemperatura()
pressure = sensor.read_pressure()/100
humidsoil = umid.dammiUmidita()
saveToDatabase(temperature, pressure, humidity, humidsoil)


