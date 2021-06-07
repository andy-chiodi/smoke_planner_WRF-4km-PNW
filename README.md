# smoke_planner_WRF-4km-PNW

Collection of Python and PyFerret scripts that process archived 4km PNW WRF output (gzipped, hourly, netcdf files with multiple variables and all x-y grid points
in a single file) into uncompressed netcdf files that contain all hours at a single x-y grid point.

## Preliminary notes

-The WRF archive in this case underwent a domain change in October 2011.  Files with the grid listed in the file name, for example 
the PyFerret script `main346x265.jnl` is meant for the original, pre 18 October 2011 grid.  Files without the horizontal grid listed are meant for the 18 October 2011 - 2020 period.

-Typically, these scripts are executed in Python from a command line, wherein the PyFerret scripts are executed as a pseudo-python module.  For example: typing the following in a command line `python wrf.py daylist hourlist main.jnl` will run the script `main.jnl` over each day and hour listed in the daylist and hourlst files (see next step for more information)

## Step 1. Process the archived WRF model output data
Prerequesites

-The wrf output data files
-Python script `wrf.py`
-Pyferret scripts:
  -`main.jnl` [`main346x265.jnl`]   loops though list of days and hours, loading an uncompressed WRF data file and calling recipe.jnl, vi.jnl
  -`recipe.jnl` defines variables necessary for fire-weather (e.g. relative humidity, virtual potential temperature) based on saved-out WRF variables
  -`vi.jnl` [`vi_346x265.jnl`] calculates mixing height, transport wind and ventilation index based on variables provided by WRF or defined by `recipe.jnl`
  -`tc.jnl` a script needed to asign a datetime to each hour of processed data (enables time aggregation in a later step)
- Other files:
  - list_of_hours (text file with the names of the forecast hours you want to process on separate lines, such as
```
f12
f13
f14
``` 
  - list_of_days (e.g., file called *wrf_2010_days.list* with dates you want to process on each line, in the form ``` 2010010100 2010010200 2010010300```
