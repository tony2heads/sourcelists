#!/usr/bin/env python
from numpy import *
import string
# some setup

def solve(s1,s2,s3,s4,nu):
#least square fit of log10(S)= a[0]+a[1]log10(f) +a[2](log10(f))**2
    s=array([log10(s1),log10(s2),log10(s3),log10(s4)])
# need log10(freq) in array nu
    a=linalg.lstsq(nu,s)
    return a[0]

def flux(a,f):
# calculate flux at freq f given a from above
    s=a[0]+a[1]*log10(f)+a[2]*(log10(f))**2
    return power(10,s)
#

f1=log10(8600)
f2=log10(4800)
f3=log10(1400)
f4=log10(843)
# I ignore the 20GHz fluxes here
# the frequencies in MHz
nu=array([[1,f1,f1**2],[1,f2,f2**2],[1,f3,f3**2],[1,f4,f4**2]])

lines=open("AT20G-BSS_tab2.txt","r")
for line in lines:
    if len(line) >180 and line[9] == ":":    # source info
        t=line.split()
        name=line[157:173]
        ra=line[7:18]
        dec=line[20:32] 
#22GHz flux is line[33:40]
        x1=string.lstrip(line[52:58]) #8600 MHz flux
        x2=string.lstrip(line[71:77]) #4800 MHz flux
        x3=string.lstrip(line[90:96]) #1400 MHz flux
        x4=string.lstrip(line[109:115]) #843 MHz flux
#        print name,x1,x2,x3,x4
# check that the fluxes are not blank
        if x1 != "..." and x2 != "..." and x3 != "..." and x4 != "...":
            s1=float(x1)
            s2=float(x2)
            s3=float(x3)
            s4=float(x4)
# check that none are all positive and 1400MHz flux >1Jy
            if s1>0 and s2>0 and s3>1.0 and s4 >0:
                print name,s1,s2,s3,s4,
                a=solve(s1,s2,s3,s4,nu)
                print a
#                print 9*" ", flux(a,8600),flux(a,4800),flux(a,1400),flux(a,843)
lines.close()
