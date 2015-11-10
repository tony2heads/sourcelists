#!/usr/bin/env python
from math import *
import sys
import os

dateline=os.popen("date +%Y")
line=dateline.readline()
year=int(line[0:4])


inpar = len(sys.argv)
if inpar > 1:
    freq =sys.argv[1]
else:
    freq=input('Freq/MHz: ')
freq=float(freq)
f=log10(freq)
#
def flux(source):
    source[4]=source[1]+source[2]*f+source[3]*f*f
    print "%-12s = %6.2fJY, %s" %(source[0],10**source[4],source[5])

source=["3C48", 2.465,-0.004,-0.1251,0,"QSO 1.5x1.5"]
flux(source)
#
source=["3C123", 2.525, 0.246,-0.1638,0,"GAL 23x5"]
flux(source)
#
source=["3C147", 2.806,-0.140,-0.1031,0, "QSO 1x1"]
flux(source)
#
source=["3C161", 1.250, 0.726,-0.2286,0, "GAL 3x3"]
flux(source)
#
source=["3C218 Hyd A", 4.729,-1.025, 0.0130,0, "GAL 47x15"]
flux(source)
#
source=["3C227", 6.757,-2.801, 0.2969,0, "GAL 200x50"]
flux(source)
#
source=["3C249.1", 2.537,-0.565,-0.0404,0, "QSO 15x15"]
flux(source)
#
source=["Virgo A", 4.484,-0.603,-0.0280,0, "GAL 200"]
flux(source)
#
source=["3C286",0.956,0.584,-0.1664,0, "QSO 1.5x1.5"]
flux(source)
#
source=["3C295", 1.490, 0.756, -0.2545 , 0, "GAL 5x1"]
flux(source)
#
source=["3C309.1",2.617,-0.437,-0.0373,0, "QSO 1.5x1.5"]
flux(source)
#
source=["3C348 Her A",3.852,-0.361,-0.1053,0, "GAL 170x25"]
flux(source)
#
source=["3C353",3.148,-0.157,-0.0911,0, "GAL 210x60"]
flux(source)
#
if freq >= 4750.0:
    source=["Cygnus A",8.360,-1.565,0,0,"GAL 170x45"]
    flux(source)
#
if freq >= 10550.0:
    source=["NGC7027",1.322,-0.134,0,0, "PN 7x10"]
    flux(source)
#
