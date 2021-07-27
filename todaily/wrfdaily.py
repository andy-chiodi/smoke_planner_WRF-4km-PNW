import pyferret
import datetime

lfn = 'wrfdaily_logfile.txt'
lfid = open(lfn,'w+')
now = datetime.datetime.now()
lfid.write(str(now)+'\n')

s = ' '
for i in range(160,181):
    for j in range(220,241):
       fc = 'go wrfdaily.jnl'+s+str(i)+s+str(j);
       print(fc)
       pyferret.start(quiet=True,verify=False,journal=False,memsize=500)  
       pyferret.run(fc)

et = datetime.datetime.now()
lfid.write(str(et)+'\n')
lfid.close()
