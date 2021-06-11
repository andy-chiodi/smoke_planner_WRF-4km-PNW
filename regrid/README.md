# Regridding 

Collection of Python and PyFerret scripts and associated data files that regrids pre-Oct 2011 4km PNW WRF netcdf data files (created by scripts in the smoke_planner_WRF-4km-PNW directory) to the 405x282 grid domain used after Oct 2011.

## Regrid from the 345x264 to 405x282 UW WRF grid
Prerequesites

- The 345x264 netcdf data files (see scripts in overlying directory)
- Python script `regrid_wrf.py`.  example linux command line usage `python regrid_wrf.py days.txt hours.txt variables.txt PyFerret_Script`
  here, *PyFerret_Script* is likely the top-level script curv_to_curv.jnl
  `regrid_wrf.py` loops though the lists of days, hours iand variables in the *days.txt*,  *hours.txt* and *variables.txt* files and runs
  the PyFerret script it is given (e.g. curve_to_curve.jnl) for each hour, day and variable listed.  The regridding is a 2-step process: 
  first the original 345x264 curvilinear grid is mapped to a rectilinear grid, then remapped to the new 405x282 grid.
  
- Pyferret scripts:
  - `curv_to_curve.jnl` defines source (`indir`) and output directories (`outdir`) and regrids the pre-Oct 2011 345x264 data to present 405x282 domain

- Regridding data files
  - `map.345x264to0.0333x0.05.nc`  mapping coordinates pre-computed by Ferret script CURV_TO_RECT_MAP.   
  - `wrf.latlon.405x282.nc`  defines the new grid

- Other files:
  - *list_of_hours*  Text file with the names of the forecast hours you want to process on separate lines, such as
```
f12
f13
f14
``` 
an example file *hours.list* is provided in the overlying directory

  - *list_of_days*  Text file with dates you want to process on each line, for example
```

2010010100
2010010200
2010010300
```
an example file *wrf_2018_days.list* is provided in the overlying directory

  - *list_of_variables*  Text files with variables to be processed on each lines, for example
```

mh
tw
utwe
vtwe
vi
w10
u10e
v10e
temp2
rh2
pbl
```
