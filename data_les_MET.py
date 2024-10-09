import datetime
#import matplotlib.pyplot as plt

def fil2data():
    tid_MET = list()
    Lufttemp_MET = list()
    Lufttrykk_Havniv_MET = list()

    with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file:
        for lines in file:
            splitline = lines.split(';')
            splitline[3] = splitline[3].replace(',','.')
            splitline[4] = splitline[4].replace(',','.')
            splitline[4] = splitline[4].replace('\n','')
            
            tid_MET.append(splitline[2])
            Lufttemp_MET.append(splitline[3])
            Lufttrykk_Havniv_MET.append(splitline[4])

    tid_MET = tid_MET[1:-1] #første og siste indeks i listene er ikke del av dataen
    Lufttemp_MET = Lufttemp_MET[1:-1]
    Lufttrykk_Havniv_MET = Lufttrykk_Havniv_MET[1:-1]

    datetime_MET = list()
    for i in range(len(tid_MET)):
        datetime_MET.append(datetime.datetime.strptime(tid_MET[i], '%d.%m.%Y %H:%M'))
        Lufttemp_MET[i] = float(Lufttemp_MET[i])
        Lufttrykk_Havniv_MET[i] = float(Lufttrykk_Havniv_MET[i])
        
    return datetime_MET, Lufttemp_MET, Lufttrykk_Havniv_MET

datetime_MET, Lufttemp_MET, Lufttrykk_Havniv_MET = fil2data()

#plt.subplot(2,1,1)
#plt.plot(a,b)
#plt.subplot(2,1,2)
#plt.plot(a,c)
#plt.show()