import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from Fil1_Aapning import dato_tid1_dt , temperatur1 , trykk_bar1 , abs_trykk1
from data_les_MET import datetime_MET, Lufttemp_MET , Lufttrykk_Havniv_MET

temp_avg = []

def comma_to_dot(comma):
    return [float(value.replace(',', '.')) for value in comma]

float_temperatur = comma_to_dot(temperatur1)


def temperature_average(temp, n):
    running_avg = []
    for i in range(len(temp)):
        if i < n - 1:
            running_avg.append(None)
        else:
            avg = sum(temp[i - n + 1:i + 1]) / n
            running_avg.append(avg)
    return running_avg

temp_avg = temperature_average(float_temperatur, 30)







valid_indices = [i for i in range(len(temp_avg)) if temp_avg[i] is not None]
valid_dates = [dato_tid1_dt[i] for i in valid_indices]
valid_avg = [temp_avg[i] for i in valid_indices]

plt.subplot(2,1,1)
#plt.figure(figsize=(10, 5))
plt.plot(dato_tid1_dt, float_temperatur, label = "Temperatur", color = "blue")
plt.plot(datetime_MET, Lufttemp_MET, label = "Temperatur MET", color = "green")
plt.plot(valid_dates, valid_avg,  label = "Gjennomsnittstemperatur", color = "orange")
plt.plot(dato_tid1_dt[1130:4572:3441], float_temperatur[1130:4572:3441], label = "Temperaturfall", color = "purple")
plt.savefig("Full_plot.png")

#plt.ylim(8,24)

plt.ylabel("Temperatur i °C")
plt.legend()

datetime_new = []
trykk_bar1_new = []

for i in range(len(trykk_bar1)):
    if trykk_bar1[i] != '':
        datetime_new.append(dato_tid1_dt[i])
        trykk_bar1_new.append(trykk_bar1[i])

Met_trykk =[tall/10 for tall in Lufttrykk_Havniv_MET]


trykk1_float = comma_to_dot(trykk_bar1_new)
abstrykk_float = comma_to_dot(abs_trykk1)

plt.subplot(2,1,2)
plt.plot(dato_tid1_dt, abstrykk_float, label='Absolutt trykk')
plt.plot(datetime_new,trykk1_float, label='Barometrisk Trykk')
plt.plot(datetime_MET,Met_trykk, label='Absolutt trykk MET')

plt.legend()
plt.show()