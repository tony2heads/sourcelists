#!/usr/bin/env python
import string

lines=open("AT20GbrightSample.txt","r")
for line in lines:
    if line[0] != "#":    # Header data
        flux20=0.
        flux9=0.
        t=line.split()
        ra=t[1]
        dec=t[2]
        name=line[-26:-10]
        nn=name.strip()
        try:
            flux20=float(t[3])
        except:
            flux20=0.
        try:
            flux9=float(t[3])
        except:
            flux9=0.

        if flux20 > 0.0  and flux9 >5:
            print nn,ra,dec,flux20, flux9
lines.close()

        
