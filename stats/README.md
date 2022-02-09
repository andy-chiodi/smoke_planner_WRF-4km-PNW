# Python scripts and PyFerret scripts necessary to create json stats files for smoke planner application

## Description

This runs from command line as 
`python make_statsjson.py`
on black, one needs to first: 
`bash`
`conda activate ferret`
if not already in a >3.6 python environment with pyerret activated

Files needed: the netcdf file of daily statistics (e.g., `/other_directory/wrf.daily.i90_j1.nc`), `./wrf.landmask.nc`, `./wrf.latlon.nc`, var_list.txt, wind_vector_list.txt, ij2latlon.py, and ferret scripts, calcstats.jnl  calcstats_vector.jnl, make_percentiles_month.jnl  make_windrose.jnl  make_windrose_month.jnl 

The i,j range make_statsjson.py runs over is hard-coded in make_statsjson.py. The script will iterate scalar/percentile calculations on variables listed in `var_list.txt` and vector/wind rose-stat calculations on the variables listed in wind_vector_list.txt, assuming wind vector info exists for 'nighttime' and 'daytime'

I suggest using python >3.6 to preserve variable order in python dict -> json dump.

dir hardcoded in calcstats.jnl and calcstats_vector.jnl would need to be changed to fit local system if ported to another computer (presently running on black in /home/chiodi/...)
