# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:46:03 2024

@author: kitti
"""

import matplotlib.pyplot as plt
from Fil1_Aapning import dato_tid1_dt , temperatur1 , trykk_bar1 , abs_trykk1


def comma_to_dot(comma):
    return [float(value.replace(',', '.')) for value in comma]

abs_trykk_new = []
trykk_bar1_new = []
datetime_new = []

for i in range(len(trykk_bar1)):
    if trykk_bar1[i] != '':
        abs_trykk_new.append(abs_trykk1[i])
        trykk_bar1_new.append(trykk_bar1[i])
        datetime_new.append(dato_tid1_dt[i])
        

trykk1_float = comma_to_dot(trykk_bar1_new)
abs_trykk_float = comma_to_dot(abs_trykk_new)
#datetime_float = comma_to_dot(datetime_new)
#print(trykk1_float)

differanse_liste = [a - b for a, b in zip(trykk1_float,abs_trykk_float)]
#print(differanse_liste)

def trykk_gjennomsnitt(trykk, n):
    running_avg = []
    for i in range(len(trykk)):
        if i < n - 1:
            running_avg.append(None)
        else:
            avg = sum(trykk[i - n + 1:i + 1]) / n
            running_avg.append(avg)
    return running_avg


trykk_avg = trykk_gjennomsnitt(differanse_liste, 10)
#print(trykk_avg)
#temp_avg = temperature_average(float_temperatur, 30)

plt.plot(datetime_new, trykk_avg, label = "Differansen")
plt.show()