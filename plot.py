import matplotlib.pyplot as plt
import numpy as np

temp_1 = []
temp_2 = []
datetime = []
temp_avg = []

def temperature_average(temp, n):
    for i in range(len(temp)- n +1):
        window = temp[i:i+n]
        window_average = sum(window) / n
        temp_avg.append(window_average)

plt.plot(temp_1,datetime, label = "Temperatur 1")
plt.plot(temp_2,datetime, label = "Temperatur 2")
plt.plot(temp_avg,datetime, label = "Gjennomsnittstemperatur")

plt.ylabel("Temperatur i °C")
plt.legend()
plt.show