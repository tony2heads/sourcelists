#!/usr/bin/env python
import string

#lines=open("wmap_ptsrc_catalog_p4_7yr_v4.txt","r")
lines=open("wmap_ptsrc_catalog_9yr_v5p1.txt","r")
for line in lines:
    if line[0] != "#" and len(line) >90:    # Header data
        t=line.split()
        ra=t[0]
        dec=t[1]
        # next glat,glong
        flux=t[4]
        #name=line[89:103]
        name=line[94:109]
        if float(flux) >3:
            rahms=ra[0:2]+":"+ra[2:4]+":"+ra[4:]
            if dec.isdigit():
                # no negative sign
                dms=" "+dec[0:2]+":"+dec[2:4]+":"+dec[4:]
            else:
                 dms=dec[0:3]+":"+dec[3:5]+":"+dec[5:]
            print name,rahms,dms,flux
