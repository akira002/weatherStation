from es5stampaLoopPTU import returnDataAllSensors
import time
import numpy as np

#Implementazione del bubble sort
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]     # Swap!
    return items

#Implementazione dell'insertion sort
def insertion_sort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items

timeseries = []

for i in range(0, 10):
    row = returnDataAllSensors()
    timeseries.append(row)
    time.sleep(1)

arrayTimeseries = np.array(timeseries)
#la temperatura e' la seconda colonna della matrice timeseries
temperature = arrayTimeseries[:,1].tolist()
print(temperature)
#l'umidita' e' la terza colonna della matrice timeseries
umidita = arrayTimeseries[:,2].tolist()
print(umidita)
print(bubble_sort(temperature))
print(insertion_sort(umidita))
