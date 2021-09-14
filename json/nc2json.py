import json
import sys
import re
import xarray
import numpy
import os
from ij2latlon import rlatlon
from ij2latlon import rland

## requires python 3.6+  for xarray

def nc2json(ii,jj):
  ii = str(ii)
  jj = str(jj)
  # root file name
  rn = 'i'+ii+'_j'+jj
  # netcdf data dir where the daily statistics file resides
  ddir = '/home/chiodi/FW/tool1/V5/data/working/test/'   
  # dir where json will reside
  odir = '/home/chiodi/FW/tool1/json/data/'
  # name of daily-statitics netcdf file generated from wrfdaily_tz.py; 
  fd = ddir+'wrf.daily.i'+ii+'.j'+jj+'.nc'
  # file containing variable names, (e.g. MH_MAX)  listed in the order they appear in the ascii data file.
  fl = 'var_list.txt'
  # get lat lon
  [lat,lon] = rlatlon(int(ii),int(jj))
  # open the netcdf file
  nc = xarray.open_dataset(fd)
  # create dictionary that will be dumped to json
  point = {}
  # some metadata
  point['start'] = '1-jan-2010'
  point['lat'] = lat
  point['lon'] = lon
  point['missing'] = None
  point['grid'] = 'UW WRF 4km'
  point['land'] = str(rland(int(ii),int(jj)))
  # now assign keys and vals in the 'data' dictionary.  the key names are read from var_list.txt  
  point['data'] = {}
  l = open(fl,'r')
  var = l.readlines()

  for v in var:    # cycles through variables listed in ascii file fl = var_list.txt
    nm = v.strip()
    mydict = nc[nm].to_dict()
    mylist = mydict['data']
    flat_list = list(numpy.concatenate(mylist).flat)            # next two lines flatten the dict from the netcdf file
    mylist_none = [None if x != x else x for x in flat_list]
    point['data'][nm] = mylist_none
  l.close()

  # dump to json, fo is the json file name
  fo = rn+'.json'
  dfo = odir+fo
  json.dump(point, open(dfo,'w'), sort_keys=False, indent = 2)
  # aws cp json file  
  cmd = '/home/chiodi/bin/aws/aws s3 cp '+dfo+' '+'s3://airfire-data-exports/smoke-planner/'+fo
  os.system(cmd)

   
# netcdf data dir where the daily statistics file resides
ddir = '/home/chiodi/FW/tool1/V5/data/working/test/'


# make the json and cp it to aws s3 bucket

for x in range(160,181):
    for y in range(220,241):
        nc2json(x,y)

