# Reshaping netcdf files with Ferret 

Ferret (or PyFerret) scripts to reshape the aggregated WRF data to files with all times for a single X,Y (lat,lon) grid point

## Files

- reshape_var_ijrange.jnl  Example usage in Ferret:  `go reshape_var_ijrange.jnl utwe`, where `utwe` could be any of the supported variable names

This script saves out the all_time-single_XY files for the specified variable in the directory and over the i,j range hard-coded in this script

- reshape_var_yr_ijrange_sub.jnl  Called by `reshape_var_ijrange.jnl`

Alternatively, in Ferret `go reshape_vars_yr_ijrange.jnl  YEAR`, where `YEAR` is, e.g. 2019, or 2020, will reshape all supported variables for the given year (tested a ~10 minute run time)

Variables as of 2 Sep 2021 number 14 (3 gridmet, 11 WRF): fm1000, fm100, pr, mh, pbl, tw, utwe, vtwe, u10e, v10e, w10, rh2, temp2 
