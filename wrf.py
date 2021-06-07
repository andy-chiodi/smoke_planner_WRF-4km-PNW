# file wrf.py
# command line usage:  python wrf.py daylist hourlist
# depends on ferret .jnl files: recipe.jnl, vi.jnl, tc.jnl (time) as well as the variable-specific
# ferret script that saves to netcdf, e.g. main.jnl (for mixing, trans. wind, vent. index and 10m wspd)
# other opitions: wdir (10m wind direction) 

# source WRF repository directory location info (no write permission)
source  = '/storage/Met/PNW/4km/WRF/'

# working directory info (w/ write permission)

working = '/home/chiodi/FW/data/'

# file naming info
pre = 'wrfout_d3.'
post = '.0000.gz'



#----------------------------------------------------------------------------


if __name__ == '__main__':    
    import sys
    import pyferret
    import gzip
    import shutil
    import os
    import datetime

# read file containing list of days
    dname = str(sys.argv[1])
    with open(dname) as f:
         days = f.readlines()

# read filecontaining list of hours
    hname = str(sys.argv[2])
    with open(hname) as f:
         hours = f.readlines()

# save str name of .jnl ferret script that this shell will run
    fname = str(sys.argv[3])

    days  = [x.strip() for x in days]
    hours = [x.strip() for x in hours]

    lfn = 'logfile.'+dname+'txt'
    lfid = open(lfn,'w+')
    lfid.write('Python/PyFerret script logfile \n')
    lfid.write('Input files   '+dname+'      '+hname+'\n') 
    now = datetime.datetime.now()
    lfid.write(str(now)+'\n')


# loop through days and hours and:  1. open and read gzipped source PNW wrf data  2. copy wrf data to working directory  3. run main.jnl for each hour of each day in list

    for x in days:
        day  = x.strip()
        for y in hours:
            hour = y.strip()
            fn = pre+day+'.'+hour+post
            gzd = source+day+'/'+fn
            unc = working+fn.strip('.gz')
            try:
               with gzip.open(gzd, 'rb') as f_in:
                    with open(unc, 'wb') as f_out:
                      shutil.copyfileobj(f_in, f_out)
                      pyferret.start(quiet=True,verify=False,journal=False,memsize=500)
                      fc = 'go '+ fname +'.jnl ' + ' ' + unc + ' ' + day+'.'+hour
                      print fc
                      pyferret.run(fc)
                      try:
			  os.remove(unc)
		      except OSError:
			  pass

            except:
               lfid.write('Could not find '+gzd+'\n')

    et = datetime.datetime.now()
    lfid.write(str(et)+'\n')
    lfid.close()

