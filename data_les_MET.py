import datetime

def fil2data()
    tid_MI = list()
    Lufttemp_MET = list()
    Lufttrykk_Havniv_MET = list()

    with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file:
        for lines in file:
            splitline = lines.split(';')
            splitline[4] = splitline[4].replace('\n','')
            
            tid_MI.append(splitline[2])
            Lufttemp_MET.append(splitline[3])
            Lufttrykk_Havniv_MET.append(splitline[4])

    tid_MI = tid_MI[1:-1] #første og siste indeks i listene er ikke del av dataen
    datetime_MET = list()
    for i in range(len(tid_MI)):
        datetime_MET.append(datetime.datetime.strptime(tid_MI[i], '%d.%m.%Y %H:%M'))
    Lufttemp_MET = Lufttemp_MET[1:-1]
    Lufttrykk_Havniv_MET = Lufttrykk_Havniv_MET[1:-1]

    return datetime_MET, Lufttemp_MET, Lufttrykk_Havniv_MET