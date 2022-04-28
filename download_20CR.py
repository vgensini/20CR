import numpy as np
import os

for yr in np.arange(1836,2016,1):
	if yr <= 1980:
		dirlab = 'SI'
	else:
		dirlab = 'MO'

	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/prs{dirlab}/hgt.{yr}.nc" -O /home/scratch/20CR_v3/hgt.{yr}.nc'
	os.system(filename)
	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/prs{dirlab}/uwnd.{yr}.nc" -O /home/scratch/20CR_v3/uwnd.{yr}.nc'
	os.system(filename)
	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/ntatFlx{dirlab}/ulwrf.ntat.{yr}.nc" -O /home/scratch/20CR_v3/olr.{yr}.nc'
	os.system(filename)
	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/sfc{dirlab}/pres.sfc.{yr}.nc" -O /home/scratch/20CR_v3/psfc.{yr}.nc'
	os.system(filename)
	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/2m{dirlab}/air.2m.{yr}.nc" -O /home/scratch/20CR_v3/t2m.{yr}.nc'
	os.system(filename)
	filename = f'wget -nc "https://psl.noaa.gov/thredds/fileServer/Datasets/20thC_ReanV3/Dailies/sfc{dirlab}/skt.{yr}.nc" -O /home/scratch/20CR_v3/skint.{yr}.nc'
	os.system(filename)
