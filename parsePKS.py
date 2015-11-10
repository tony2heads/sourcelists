#!/usr/bin/env python
file = open("pkscat90.txt")
for line in file:
    name= line[:10]
#    rah=line[10:12]
#    ram=line[13:15]
#    ras=line[16:20]
    RA=line[10:12]+":"+line[13:15]+":"+line[16:22]
#    dd=line[23:26]
#    dm=line[27:29]
#    ds=line[30:35]
    DEC=line[23:26]+":"+line[27:29]+":"+line[30:35]
    print name,RA,DEC,"J2000",line[168:175]

