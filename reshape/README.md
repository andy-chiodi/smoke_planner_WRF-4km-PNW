# Reshaping netcdf files with Ferret 

Ferret (or PyFerret) scripts to reshape the aggregated WRF data to files with all times for a single X,Y (lat,lon) grid point

## Files

- reshape_var_ijrange.jnl  Example usage in Ferret:  `go reshape_var_ijrange.jnl utwe`, where `utwe` could be any of the supported variable names

This script saves out the all_time-single_XY files for the specified variable in the directory and over the i,j range hard-coded in this script

- reshape_var_yr_ijrange_sub.jnl  Called by `reshape_var_ijrange.jnl`  
