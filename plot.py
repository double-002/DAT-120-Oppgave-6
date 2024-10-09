import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from Fil1_Aapning import dato_tid1_dt , temperatur1
from data_les_MET import Lufttemp_MET , datetime_MET

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

plt.figure(figsize=(10, 5))
plt.plot(dato_tid1_dt, float_temperatur, label = "Temperatur", color = "blue")
plt.plot(datetime_MET, Lufttemp_MET, label = "Temperatur MET", color = "green")
plt.plot(valid_dates, valid_avg,  label = "Gjennomsnittstemperatur", color = "orange")

plt.ylim(8,24)

plt.ylabel("Temperatur i °C")
plt.legend()
plt.savefig("Temperatur_plot.png")
plt.show()