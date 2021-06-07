# smoke_planner_WRF-4km-PNW

Collection of Python and PyFerret scripts that process archived 4km PNW WRF output (gzipped, hourly, netcdf files with multiple variables and all x-y grid points
in a single file) into uncompressed netcdf files that contain all hours at a single x-y grid point.

## Prelimimnary notes

-The WRF archive in this case underwent a domain change in October 2011.  Files with the grid listed in the file name, for example the PyFerret script:

  `main346x265.jnl`

are meant for the original, pre 18 October 2011 grid.  Files without the horizontal grid listed are meant for the 18 October 2011 - 2020 period.

-Typically, these scripts are executed in Python from a command line.  For example:


## Step 1. Process the archived WRF model output data
  
