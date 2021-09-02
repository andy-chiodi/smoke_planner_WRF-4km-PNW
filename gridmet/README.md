# Ferret for Gridmet

Contains Ferret scripts and reference netcdf file needed to acquire and process daily averages of fuel moisture (100hr & 1000hr) and precipitation from the Gridmet data set. 

In this case, Ferret uses OpenDap to access the data and regrids the source data from its native rectilinear 4km-resolution grid to the PNW WRF 4km grid (Lambert Conformal), before saving the result as a netcdf file.

Basic usage in Ferret is:

```
go getregridmet_fm100.jnl 2018
go getregridmet_fm1000.jnl 2018 
go getregridmet_pr.jnl 2018
```
The example above would create files fm100.2018.nc, fm1000.2018.nc and pr.2018.nc in the directory in which Ferret is started and the script is run.  Substituting, `2019` or `2020` for `2018` would do the same for year 2019, 2020, etc.

Prerequisite here is that the wrf.latlon.405x282.nc file is in the same directory as the Ferret script is run in.
