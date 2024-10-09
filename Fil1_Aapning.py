import datetime as dt


#startverdi = 0
sluttverdi = 45700


#startverdi_str = str(startverdi)
sluttverdi_str = str(sluttverdi+10)
    
def fil1data(sluttverdi_str):
    
    tid_fra_start1 = list()
    dato_tid1_str = list()
    dato_tid1_dt = list()
    trykk_bar1 = list()
    abs_trykk1 = list()
    temperatur1 = list() 
    tid_str = list()
    
    fil1 = open('trykk_og_temperaturlogg_rune_time.csv', mode='r')
    
    for linjer in fil1:
        split = linjer.split(';')
        split[4] = split[4].replace('\n', '')
        dato_tid1_str.append(split[0])
        tid_fra_start1.append(split[1])
        trykk_bar1.append(split[2])
        abs_trykk1.append(split[3])
        temperatur1.append(split[4])
            
        if split[1] == sluttverdi_str: 
            tid_fra_start1.pop(0)
            trykk_bar1.pop(0)
            abs_trykk1.pop(0)
            temperatur1.pop(0)
            dato_tid1_str.pop(0)
            
            for i in range(len(tid_fra_start1)):
                sek_int = int(tid_fra_start1[i])
                sekund = sek_int%60
                tid_str.append(dato_tid1_str[i]+':'+str(sekund))
            
            for x in range(len(tid_str)):
                dato_tid1_dt.append(dt.datetime.strptime(tid_str[x], "%m.%d.%Y %H:%M:%S"))
                                 
            fil1.close()
            
            return tid_fra_start1, dato_tid1_str, dato_tid1_dt, trykk_bar1, abs_trykk1, temperatur1

tid_fra_start1, dato_tid1_str, dato_tid1_dt, trykk_bar1, abs_trykk1, temperatur1 = fil1data(sluttverdi_str)




