#!/usr/bin/env python
from numpy import *
# some setup

def solve(s1,s2,s3,nu):
#least square fit of log10(S)= a[0]+a[1]log10(f) +a[2](log10(f))**2
    s=array([log10(s1),log10(s2),log10(s3)])
# need log10(freq) in array nu
    a=linalg.lstsq(nu,s)
    return a[0]

def flux(a,f):
# calculate flux at freq f given a from above
    s=a[0]+a[1]*log10(f)+a[2]*(log10(f))**2
    return power(10,s)
#

f1=log10(1410)
f2=log10(2700)
f3=log10(5000)
#
# the frequencies in MHz
nu=array([[1,f1,f1**2],[1,f2,f2**2],[1,f3,f3**2]])

lines=open("StrongPKS.txt","r")
for line in lines:
    if line[0] == "B":    # source info
        t=line.split()
        name=t[0]
        s1=float(t[-3])
        s2=float(t[-2])
        s3=float(t[-1])
        print name,s1,s2,s3,
        a=solve(s1,s2,s3,nu)
        print a
#        print 9*" ", flux(a,1410),flux(a,2700),flux(a,5000)

