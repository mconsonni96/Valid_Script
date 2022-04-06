import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import scipy.stats as st

results = []

with open('ch2_CT.csv', newline='') as file_name:     #leggo il csv e raccolgo i dati in una lista di string    
	for row in csv.reader(file_name):
	    results.append(row[0])

data = list(map(int, results))                        #converto la lista di string in lista di int

total = np.sum(data)					#sommo tutti gli elementi della lista (valori della CT in counts)

for i in range(len(data)):
	data[i] = (data[i]/total)*2400;               #converto i valori counts in valori in ps

print(data)

DSP_time = 0

for x in range(239,286):                              #sommo i ps dei 48 tap di un singolo DSP
	DSP_time = DSP_time + data[x];

print(DSP_time)                                       #tempo di propagazione di un DSP
