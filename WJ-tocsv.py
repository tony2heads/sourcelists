#!/usr/bin/env python
file=open("WallPeacock2Jy.csv","r")
for line in file:
    name=line[5:27]
    ra=line[36:46]
    ranew=ra[0:2]+":"+ra[3:5]+":"+ra[6:]
    dec=line[48:57]
    decnew=dec[0:3]+":"+dec[4:6]+":"+dec[7:]
    so=line[59:65]
    z=line[74:82]
    mag=line[88:93]
    #print name+","+ranew,",",decnew+","+so+","+z+","+mag
    print ("%s,%s,%s,%s,%s,%s") %(name,ranew,decnew,so,z,mag)
