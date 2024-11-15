# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:37:11 2024

@author: kitti
"""

#fil1 = open('trykk_og_temperaturlogg_rune_time.csv', mode='r')

fil1 = open('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv', mode='r')

#sirdal_liste = [i for i in fil1 if "Sirdal" in i]
sauda_liste = [i for i in fil1 if "Sauda" in i]


with open("sauda_liste.txt", "w") as g:
    for i in sauda_liste:
        g.write(f"{i}\n")


fil1 = open('temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv', mode='r')

sirdal_liste = [i for i in fil1 if "Sirdal" in i]

with open("sirdal_liste.txt", "w") as f:
    for i in sirdal_liste:
        f.write(f"{i}\n")
        
print(sauda_liste)