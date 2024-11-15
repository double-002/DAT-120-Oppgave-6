# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:33:45 2024

@author: kitti
"""
import datetime
   
 
    
def sirdal():
    
    dato_tid = list()
    sirdal_temp = list()
    sirdal_trykk = list()
    date_time2 = list()
      
  
    with open("sirdal_liste.txt", "r", encoding="utf-8") as fil:


        for linje in fil:
            linje = linje.strip()
        
            if not linje:
                continue

            deler = linje.split(";")

            dato_tid.append(deler[2])
            sirdal_temp.append(deler[3])
            sirdal_trykk.append(deler[4])


        for i in range(len(dato_tid)):
            date_time2.append(datetime.datetime.strptime(dato_tid[i], '%d.%m.%Y %H:%M'))

                    
    return date_time2, sirdal_temp, sirdal_trykk

date_time2, sirdal_temp, sirdal_trykk = sirdal()

def sauda():
    
    sauda_temp = list()
    sauda_trykk = list()
    
    
    with open("sauda_liste.txt", "r", encoding="utf-8") as fil1:
    
   
        for linje in fil1:
            linje = linje.strip()
            
            if not linje:
                continue
            
            deler = linje.split(";")
            
            sauda_temp.append(deler[3])
            sauda_trykk.append(deler[4])
        


    return sauda_temp, sauda_trykk

sauda_temp, sauda_trykk = sauda()



