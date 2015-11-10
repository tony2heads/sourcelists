#!/usr/bin/env python
from ephem import *
intime="2000/1/1 12:00:00" #epoch 2000
KAT=Observer()
KAT.long,KAT.lat='21.388','-30.7148' # positive East,North
KAT.date=intime
KAT.epoch=intime
# print KAT.epoch
KAT.elev=1000.0          #metres above MSL
KAT.temp=20              # temperature in C
KAT.pressure=900         # pressure in mbar set to zero to ignore refraction
KAT.horizon=degrees('00:00:00')        # minimum elevation
lines=open("masers.txt","r")
for line in lines:
    x=line.split("=")
    name=x[1].split()[0]
    name=name[1:-1] # remove quotes at start and end
    ra=x[2].split()[0]
    dec=x[3].split()[0]
#    print name,ra,dec
    dbline=name+",f|J,"+ra+","+dec+",,1950"
#    print "     ",dbline
    p=readdb(dbline)
    p.compute(KAT)
    print p.name, p.ra ,",", p.dec,",(0.0 0.0 0.0 0.0 0.0)"
lines.close()
