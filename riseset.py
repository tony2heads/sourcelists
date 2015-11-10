#!/usr/bin/env python
from optparse import OptionParser
from time import *
from ephem import *
#
today=strftime("%Y/%m/%d")
#
parser=OptionParser()
#
parser.set_defaults(ut="00:00:00")
parser.set_defaults(date=today)
parser.set_defaults(elev="10:00:00")
#
parser.add_option("-f", "--file",dest="filename",               
                  help="give input FILE")
parser.add_option("-d", "--date", dest="date",
                  help="Give a date in format yyyy/mm/dd")
parser.add_option("-t", "--time",dest="ut",
                  help="Give a UT date in format hh:mm")
parser.add_option("-e", "--elevation",dest="elev",
                  help ="give elevationb in dd:mm:ss")
(options, args) = parser.parse_args()
#
intime=options.date+" "+options.ut
infile=options.filename
elevation=options.elev
#
#intime=raw_input("Give time in YYYY/MM/DD hh:mm ")
if infile == None:
   infile=raw_input("Filename with sources: ")
#
#
KAT=Observer()
KAT.long,KAT.lat='21:24:38.46','-30:43:17.34' # positive East,North
KAT.date=intime
KAT.epoch=intime
# print KAT.epoch
KAT.elev=1038            #metres above MSL
KAT.temp=20              # temperature in C
KAT.pressure=892         # pressure in mbar set to zero to ignore refraction
KAT.horizon=degrees(elevation)        # minimum elevation
dd=KAT.date.tuple()
print "Date %d/%d/%d %02d:%02d  LST %s"\
      %(dd[0],dd[1],dd[2],dd[3],dd[4],KAT.sidereal_time())
print "Source"+18*" "+"Position"+10*" "+"Rise"+5*" "+"Transit"+6*" "+"Set"
#
sun=Sun()
sun.compute(KAT)
#print "Sun  Alt",  sun.alt, "Az", sun.az
print "Sun          %12s %12s %-9s %-9s %-9s " \
      %(sun.ra,sun.dec,str(KAT.next_rising(sun))[-8:],str(KAT.next_transit(sun))[-8:],str(KAT.next_setting(sun))[-8:])
#
moon=Moon()
moon.compute(KAT)
#print "Moon Alt", moon.alt,"Az", moon.az

print "Moon          %-12s%12s %-9s %-9s %-9s " \
            % (moon.ra,moon.dec,str(KAT.next_rising(moon))[-8:],str(KAT.next_transit(moon))[-8:],str(KAT.next_setting(moon))[-8:])
print 
#
#
inp=open(infile)
for line in inp:
  if line[0] != "#":
    s=line.split(",") # split the line into strings
    source=s[0]
# next item is 'radec...'    
    ra=s[2]
    dec=s[3]
    dbline='"'+source+",f|J|Q,"+ra+","+dec+",,2000"+'"'
#    print dbline
    p=readdb(dbline)
#    p=FixedBody()
#    p._ra,p._dec=ra,dec
#    p._epoch='2000'
    p.compute(KAT)
    if p.neverup == True:
       print "%-11s %12s %12s           Never Rises           " %(source,p.ra,p.dec),
    if p.circumpolar == True:
       tra=str(KAT.next_transit(p))[-8:]
       print "%-11s %12s %12s          %9s  Circumpolar "  %(source,p.ra,p.dec,tra)
    if p.neverup == False and p.circumpolar == False:  # Source rises and sets
#      print source, p.ra, p.dec, p.alt, p.az,
      ris=str(KAT.next_rising(p))[-8:]
      tra=str(KAT.next_transit(p))[-8:]
      set=str(KAT.next_setting(p))[-8:]
      print "%-12s %12s %12s %-9s %-9s %-9s   " % (source,p.ra,p.dec,ris,tra,set)
#    for n in range(3,len(s)):    #comments at the end of the input line
#         print s[n],
#    print ""
inp.close()
