# Aggregating netcdf with PyFerret 

PyFerret scripts to aggregate the hourly netcdf files, first to monthly netcdf, and then to yearly netcdf files on a variable-by-variable basis

## Files

- do_vn.jnl this is a shell that runs `agg.vn.yr.jnl` for the years listed by line in `do_vn.jnl`.  Example use in Ferret is: `go do_vn utwe`, where `utwe` could be any of the supported variables names (e.g. mh, vi, tw, temp2, etc.)  
- agg.vn.yr.jnl is the Ferret script that aggregates a year's worth of hourly netcdf files into monthly netcdf files.  Example usage in Ferret: `go agg.vn.yr.jnl utwe 2010`, where utwe, again, could be any supported variable name and 2010 any of the years we have data for.  `agg.vn.yr.jnl` calls `agg.jnl`
- agg.jnl creates a list of hourly ~.nc files in the specified data directory for a given variable name, year and month and passes this list to the Ferret function `TSERIES`, which does the aggregation
