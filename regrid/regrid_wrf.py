# file regrid.py
# command line usage:  python regrid.py daylist hourlist variable_name_list  name_of_ferret_script (without the .jnl)
# depends on ferret .jnl files: rect_to_rect.jnl as well as the mapping parameters and output lat, lon info used therein

# source WRF repository directory location info
# read_dir  = '/home/chiodi/FW/data/'  # changed to being asigned in ferret .jnl file

# working directory info (w/ write permission)

# save_dir = '/home/chiodi/FW/data/regrid/'  # asigned in ferret .jnl file

# file naming info
post = '.nc'

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

# read filecontaining list of variable names
    vname = str(sys.argv[3])
    with open(vname) as f:
         vnames = f.readlines()

# save str name of .jnl ferret script that this shell with run
    fname = str(sys.argv[4])

    days  = [x.strip() for x in days]
    hours = [x.strip() for x in hours]
    variables = [x.strip() for x in vnames]
    lfn = 'logfile.'+dname+'txt'
    lfid = open(lfn,'w+')
    lfid.write('Python/PyFerret script logfile \n')
    lfid.write('Input files   '+dname+'      '+hname+'    '+vname+'\n') 
    lfid.write('Ferret script '+fname+'\n')
    now = datetime.datetime.now()
    lfid.write(str(now)+'\n')

# loop through days and hours and vars, regridding the 345x264 WRF output to the 405x282 grid
  
    for x in days:
        day  = x.strip()
        for y in hours:
            hour   = y.strip()
            for z in variables:
                var = z.strip()
                filenm = var+'.'+day+'.'+hour+post
                fc = 'go '+ fname +'.jnl ' + ' ' + var + ' ' + day + ' ' + hour 
                try:
                      pyferret.start(quiet=True,verify=False,journal=False,memsize=500)
                      print fc
                      pyferret.run(fc)
                except:
                      lfid.write('Trouble with  '+fc+'\n')

    et = datetime.datetime.now()
    lfid.write(str(et)+'\n')
    lfid.close()
