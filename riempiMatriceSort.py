from stampaLoopTmpPressione import returnDataAllSensors
import time
import numpy as np

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]     # Swap!
    return items

def insertion_sort(items):
    """ Implementation of insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items


# Creates a list containing 5 lists, each of 8 items, all set to 0
#w, h = 4, 60
#timeseries = [[0 for x in range(w)] for y in range(h)] 

#for i in range (0, 60):
#    print(i)
#    row = returnDataAllSensors()
#    timeseries[i][0]=row[0]
#    timeseries[i][1]=row[1]
#    timeseries[i][2]=row[2]
#    timeseries[i][3]=row[3]


timeseries = []

for i in range(0, 10):
    row = returnDataAllSensors()
    timeseries.append(row)

arrayTimeseries = np.array(timeseries)
temperature = arrayTimeseries[:,1].tolist()
print(temperature)
umidita = arrayTimeseries[:,2].tolist()
print(umidita)
print(bubble_sort(temperature))
print(insertion_sort(umidita))


