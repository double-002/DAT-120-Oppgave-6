import datetime

tid_MI = list()
Lufttemp_MI = list()
Lufttrykk_Havniv_MI = list()

with open('temperatur_trykk_met_samme_rune_time_datasett.csv', mode='r') as file:
    for lines in file:
        splitline = lines.split(';')
        splitline[4] = splitline[4].replace('\n','')
        
        tid_MI.append(splitline[2])
        Lufttemp_MI.append(splitline[3])
        Lufttrykk_Havniv_MI.append(splitline[4])

tid_MI = tid_MI[1:-1] #første og siste indeks i listene er ikke del av dataen
datetime_MI = list()
for i in range(len(tid_MI)):
    datetime_MI.append(datetime.datetime.strptime(tid_MI[i], '%d.%m.%Y %H:%M'))
Lufttemp_MI = Lufttemp_MI[1:-1]
Lufttrykk_Havniv_MI = Lufttrykk_Havniv_MI[1:-1]