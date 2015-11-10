#!/usr/bin/env python
#!/usr/bin/env python
from numpy import *
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

f1=log10(1700)
f2=log10(8400)
f3=log10(22000)
f4=log10(43000)
# Ignoring the 7mm flux density
#
# the frequencies in MHz
nu=array([[1,f1,f1**2],[1,f2,f2**2],[1,f3,f3**2],[1,f4,f4**2]])

lines=open("ATNF-Ku.txt","r")
for line in lines:
    if line[0] != "#":    # Header data
        t=line.split()
        name=t[0]
        ra= t[1]
        dec=t[2]
        x1=t[3] #1700 MHz flux
        x2=t[4] #8400 MHz flux
        x3=t[5] #22GHz flux
        x4=t[6] #43GHz flux
# check that the fluxes are not blank
        if x1 != " "*len(x1) and x2 != " "*len(x2) and x3 != " "*len(x3) and x4 != " "*len(x4): 
            s1=float(x1)
            s2=float(x2)
            s3=float(x3)
            s4=float(x4)
# check that all are positive
            if s1>0 and s2>0 and s3>0 and s4 >0:
                a=solve(s1,s2,s3,s4,nu)
                print "%s, radec gaincal, %s,%s,(1700 43000" %(name,ra,dec),
                print "%5.3f %5.3f %5.3f)" %(a[0],a[1],a[2])
               # print 9*" ", flux(a,1700),flux(a,8400),flux(a,22000),flux(a,43000)
lines.close()
