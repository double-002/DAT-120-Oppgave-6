import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from Fil1_Aapning import dato_tid1_dt , temperatur1
from data_les_MET import Lufttemp_MET

temp_avg = list()
def temperature_average(temp, n):
    for i in range(len(temp)- n +1):
        window = temp[i:i+n]
        window_average = sum(window) / n
        temp_avg.append(window_average)

temp_avg = temperature_average(Lufttemp_MET, 30)


plt.plot(temperatur1,dato_tid1_dt, label = "Temperatur", color = "blue")
plt.plot(Lufttemp_MET,dato_tid1_dt, label = "Temperatur MET", color = "green")
plt.plot(temp_avg,dato_tid1_dt, label = "Gjennomsnittstemperatur", color = "orange")
plt.axis(0o6-11, 0o6-14, 8, 24)
plt.ylabel("Temperatur i °C")
plt.legend()
plt.savefig("Temperatur_plot.png")
plt.show()