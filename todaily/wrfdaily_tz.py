import pyferret
import datetime
from xy2latlon import roffset

lfn = 'wrfdaily_test_logfile.txt'
lfid = open(lfn,'w+')
now = datetime.datetime.now()
lfid.write(str(now)+'\n')

s = ' '
for i in range(160,181):            # ilon
    for j in range(220,241):        # jlat
       i1 = i-1;
       j1 = j-1;  # convert to Ferret index, which starts with 1, wheras python starts with 0
       [offset,lat,lon] = roffset(i1,j1)
       fc = 'go wrfdaily_tz.jnl'+s+str(i)+s+str(j) +s+ str(offset);
       print(fc)
       pyferret.start(quiet=True,verify=False,journal=False,memsize=500)  
       pyferret.run(fc)

et = datetime.datetime.now()
lfid.write(str(et)+'\n')
lfid.close()
