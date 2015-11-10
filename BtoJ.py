import coords as C
def b2j(c):
    # reads a string "RA DEC" and returns a string "RA Dec"
    # both in hh:mm:ss.s +-dd:mm:ss.s
    x=C.Position(c,equinox='B1950')
    t=C.Position(x.j2000(),equinox='J2000').hmsdms()
    return t

#c="22:23:11.0870 -05:12:17.900"
#x=b2j(c)
#print c, "B1950"
#print x, "J2000"

lines=open("listb.txt","r")
for line in lines:
    x=line.split("=")
    name=x[1].split()[0]
    name=name[1:9] # remove quotes at start 
    ra=x[2].split()[0]
    dec=x[3].split()[0]
    c=ra+" "+dec
    t=b2j(c)
    print ("%-8s %s") %(name,t)
lines.close()
