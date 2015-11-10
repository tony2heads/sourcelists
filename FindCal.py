#!/usr/bin/env python
# coding: utf-8

# # Search for calibrators
# ## Needs
# * CSV file with calibrators
# * Source to match with
# * math, ephem, operator

import ephem
import math
import operator
from optparse import OptionParser

parser=OptionParser()
parser.set_defaults(horizon="10:00:00")
parser.set_defaults(filename="/home/tony/Desktop/SouthAfrica/SourceLists/Good.csv")
parser.set_defaults(nrcals="3")
parser.set_defaults(sourcename="test")

parser.add_option("-f","--file",dest="filename",\
 help="CSV file with calibrators")
parser.add_option("-H","--horizon",dest="horizon",\
 help="Min elevation in dd:mm:ss format")
parser.add_option("-n","--name",dest="sourcename",\
 help="Name of source")
parser.add_option("-r","--RA",dest="ra", help="RA of souce (J2000) hh:mm:ss")
parser.add_option("-d","--dec",dest="dec",\
 help="declination of source(J2000) +/-dd:mm:ss")
parser.add_option("-c","--ncals",dest="nrcals",help="Number of calibrators")

(options,args) =parser.parse_args()
filename=options.filename
ra=options.ra
dec=options.dec
horizon=options.horizon
sourcename=options.sourcename
name=sourcename.replace(" ","_")
nc=int(options.nrcals)

# Setup KAT site
kat = ephem.Observer()
kat.lat = '-30.71317'
kat.long = '21.44389'
kat.elevation = 1038
kat.temp=25
kat.pressure=890
kat.date = ephem.now()
kat.horizon=horizon

testsource=ephem.FixedBody()
testsource.name=name
testsource._ra=ra
testsource._dec=dec
testsource.compute(kat)
# Get sources
csvline=name+", radec target, "+ra+", "+dec+"\n"


sources=open(filename)
slist=[]
for s in sources:
    #print s
    slist.append(s)

seps=[]
names=[]
sourcedic={}

for cal in slist:
    parts=cal.split(',')
    #print parts[0:1]
    if parts[0][0] != "#":
        #print parts[0],parts[2],parts[3]
        calp=ephem.FixedBody()
        calp.name=parts[0]
        calp._ra=parts[2]   # J2000 position
        calp._dec=parts[3]  #J2000 position
        calp.compute(kat) 
        #print calp.name, ephem.separation(calp,testsource)
        names.append(calp.name)
        seps.append(math.degrees(ephem.separation(calp,testsource)))
        sourcedic[calp.name] = parts[2]+","+parts[3]


# In[90]:


sps=dict(zip(names,seps))


x=sorted(sps.items(), key=operator.itemgetter(1))


print testsource.name, testsource.a_ra, testsource.a_dec
print "Calibrator Sep/deg"
for n,s in x:
    print ("%-12s %4.1f") %(n,s)


"""
# for debugging
for n in range(2):
    calname=x[n][0]
    line=calname+", radec gaincal,"+sourcedic[calname]
    print line
"""
"""
best=x[0][0]
bestline=best+", radec gaincal,"+sourcedic[best]
good=x[1][0]
nextline=good+", radec gaincal,"+sourcedic[good]
"""


outfile=open(name+".csv","w")
for n in range(nc):
    calname=x[n][0]
    line=calname+", radec gaincal,"+sourcedic[calname]
    outfile.write(line)
# written calibrators, now target
outfile.write(csvline)
outfile.close()
sources.close()
