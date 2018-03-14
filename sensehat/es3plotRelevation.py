import matplotlib.pyplot as plt
from csv import reader

with open('rilevazioni.csv', 'r') as f:
        data = list(reader(f))
        temp = [i[1] for i in data[1::]]
        time = [i[0] for i in data[1::]]

        #plt.plot(time, temp)
        xn = range(len(time))
        plt.plot(xn, temp)
        plt.tight_layout()
        plt.xticks(xn, time)
        plt.xticks(rotation=90)
        plt.savefig('test.png')
