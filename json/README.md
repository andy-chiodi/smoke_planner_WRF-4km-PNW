# Python scripts and other necessary files to create json data files for smoke planner application

## Description

This runs from command line as
'python nc2json.py'

Files needed: the netcdf file of daily statistics (e.g., '/other_directory/i180_j220.nc'), './wrf.landmask.nc', './wrf.latlon.nc', var_list.txt, ij2latlon.py, nc2json.py

The i,j range nc2json.py runs over is hard-coded in nc2json.py.  Netcdf files herein allow WRF lat,lon and landmask (1.0=land, 0.0=water) info to go into the json files.  The script will iterate on variables listed in 'var_list.txt'.

nc2json.py makes use of xarray to read the netcdf files.  So, appropriately up-to-date python version is needed (xarray instruction list a 24-month support window; xarray is not available to my knowledge for, say, python 2.7)
