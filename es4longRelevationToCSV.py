import time
from sense_hat import SenseHat
sense = SenseHat()

with open('rilevazioni.csv','w') as file:
    while True:

          # Take readings from all three sensors
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        # Round the values to one decimal place
        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

          #get time stamp
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    # str() converts the value to a string so it can be concatenated
        line =  date + ", "+str(h)
        print(h)
        file.write(line)
        file.write('\n')
        time.sleep(1)
