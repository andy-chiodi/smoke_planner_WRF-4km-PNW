# converts input lat, lon to neareast X,Y direction indices by using np.unravel_indices based on minimization

import numpy as np
from scipy.io import netcdf

def rlatlon(i,j):
    f = netcdf.netcdf_file('wrf.latlon.nc','r')  # read in prepared lats and lons of 405x282 WRF grid (for post Oct 18 2011 files)
    wrflon=f.variables['LON']
    wrflat=f.variables['LAT']
    # subtract 1 to return answer in FERRET index convention (first index=1), rather than python (first index value = 0)
    j = j-1
    i = i-1
    lat = round(wrflat[j,i],4)
    lon = round(wrflon[j,i],4)
    return lat,lon 
    f.close()

def rland(i,j):
    f = netcdf.netcdf_file('wrf.landmask.nc','r')  # read in landmask from wrfout
    wrfland=f.variables['LANDMASK']
    # subtract 1 to return answer in FERRET index convention (first index=1), rather than python (first index value = 0)
    j = j-1
    i = i-1
    land = wrfland[j,i]
    return land
    f.close()

