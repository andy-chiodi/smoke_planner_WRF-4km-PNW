# Creating daily netcdf files from hourly data with PyFerret

Contains Python and PyFerret scripts needed to calculate, for example, daytime, nighttime and 24-means from hourly data

## Note that whereas other python scripts in this repo will work in python 2.7, the time time zone (_tz)-aware files here need python >3.6 (e.g. 3.9)

With miniconda PyFerret install this environment is reached buy first entering:
```
bash
conda activate ferret
```

With PyFerret and python 3.9 enabled, example command line usage is then:
```
python wrfdaily_tz.py
```
As of 2 Sep, 2021, the i,j (latitude, longitude) range that wrfdaily_tz.py produces results over is hard-coded in wrfdaily_tz.py

`_tz` stands for time zone.  Python function roffset(), defined in xy2latlon.py is relied upon to determine a given location's offset in hours from UTC (standard time is used at present).  The daytime and nighttime results are thereby calculated relative to local standard time.

Presently, `daytime` is defined as 6 am to 6pm local standard.  `Nighttime` is defined as the remaining hours of the 24-hour period.

Resulting single xy-gridpoint, all time, netcdf files have the naming convention `wrf.daily.iXXX.jYYY.nc`, for example, `wrf.daily.i180.j220.nc` would contain the daily values for all `WRF` variables at the i=180, j=220 WRF-domain grid point.  Note that Gridmet-sourced data are included in such netcdf files even though the fm100, fm1000 and pr data were not calculated by the UW WRF model (they have been, however, regridded to the WRF curvilinear grid).

Hourly scalars (including wind speed) yield 4 daily variables: daytime average, nighttime average, 24-hour max, 24-hour min.

The wind vector (transport and 10m) is handled differently, and yeilds 5 daily variables: the first 4 are daytime and nighttime averages for both the zonal and meridional components. The fifth is standard deviation of wind direction during the daytime.
