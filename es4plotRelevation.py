import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser

with open('rilevazioni2.csv', 'r') as f:
        data = list(reader(f))
        temp = [i[1] for i in data[1::]]
        time = [i[0] for i in data[1::]]
        
        plt.plot(time, temp)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig('test.png')
