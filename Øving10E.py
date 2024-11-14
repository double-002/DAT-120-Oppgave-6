from data_les_MET import datetime_MET, Lufttemp_MET , Lufttrykk_Havniv_MET
from plot import trykk1_float, datetime_new, float_temperatur

#Trykk
trykkdata_MET = dict.fromkeys(datetime_MET)
trykkdata_Rune = dict.fromkeys(datetime_new)
l = -1
j = -1
for i in trykkdata_MET:
    l = l+1
    trykkdata_MET[i] = Lufttrykk_Havniv_MET[l]

for i in trykkdata_Rune:
    j = j+1 
    trykkdata_Rune[i] = trykk1_float[j]

#Temp
tempdata_MET = dict.fromkeys(datetime_MET)
tempdata_Rune = dict.fromkeys(datetime_new)
p = -1 
o = -1
for i in tempdata_MET:
    p = p+1 
    tempdata_MET[i] = Lufttemp_MET[p]

for i in tempdata_Rune:
    o = o+1
    tempdata_Rune[i] = float_temperatur[o]

#Trykk
avg_trykk_dict = dict()
for i in trykkdata_Rune:
    MET_trykk = trykkdata_MET.get(i)
    Rune_trykk = trykkdata_Rune.get(i)
    if MET_trykk != None:
        deltatrykk = Rune_trykk-MET_trykk
        avg_trykk_dict.setdefault(i, deltatrykk)

trykk_maxima = float('-inf')
trykk_minima = float('inf')
trykksnitt = 0        
for i in avg_trykk_dict:
    trykksnitt = avg_trykk_dict.get(i)+trykksnitt
    if trykk_maxima <= avg_trykk_dict.get(i):
        trykk_maxima = avg_trykk_dict.get(i)
        tid_maxima_trykk = i 
        
    if trykk_minima >= avg_trykk_dict.get(i):
        trykk_minima = avg_trykk_dict.get(i)
        tid_minima_trykk = i 

trykksnitt = trykksnitt / len(avg_trykk_dict)

#Temp
avg_temperatur_dict = dict()
for i in tempdata_Rune:
    MET_temp = tempdata_MET.get(i)
    Rune_temp = tempdata_Rune.get(i)
    if MET_temp != None:
        deltatemp = Rune_temp-MET_temp
        avg_temperatur_dict.setdefault(i, deltatemp)
        
temp_maxima = float('-inf')
temp_minima = float('inf')
tempsnitt = 0
for i in avg_temperatur_dict:
    tempsnitt = avg_temperatur_dict.get(i)+tempsnitt
    if temp_maxima <= avg_temperatur_dict.get(i):
        temp_maxima = avg_temperatur_dict.get(i)
        tid_maxima_temp = i 
        
    if temp_minima >= avg_temperatur_dict.get(i):
        temp_minima = avg_temperatur_dict.get(i)
        tid_minima_temp = i 

tempsnitt = tempsnitt / len(avg_temperatur_dict)



#trykk
print("Trykk: gjennomsnittet er:", trykksnitt, ",maksimal forksjell er:", tid_maxima_trykk, round(trykk_maxima, 2), ",minimal forskjell er:", tid_minima_trykk, round(trykk_minima, 2))
#temp
print("Temp: gjennomsnittet er:", tempsnitt, ",maksimal forksjell er:", tid_maxima_temp, round(temp_maxima, 2), ",minimal forskjell er:", tid_minima_temp, round(temp_minima, 2))
        
    