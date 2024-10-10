import matplotlib.pyplot as plt
from Fil1_Aapning import dato_tid1_dt , temperatur1 , trykk_bar1 , abs_trykk1
from data_les_MET import datetime_MET, Lufttemp_MET , Lufttrykk_Havniv_MET

def comma_to_dot(comma):
    return [float(value.replace(',', '.')) for value in comma]

datetime_new = []
trykk_bar1_new = []

for i in range(len(trykk_bar1)):
    if trykk_bar1[i] != '':
        datetime_new.append(dato_tid1_dt[i])
        trykk_bar1_new.append(trykk_bar1[i])


trykk1_float = comma_to_dot(trykk_bar1_new)
abstrykk_float = comma_to_dot(abs_trykk1)

print(abstrykk_float)

#plt.plot(datetime_new,trykk1_float, label='Trykk 1')
#plt.plot(datetime_MET,Lufttrykk_Havniv_MET, label='MET')
#plt.plot(dato_tid1_dt, abstrykk_float, label='abs trykk')
#plt.legend()
#plt.show()