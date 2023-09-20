from abc import ABC, abstractmethod

import xarray as xr
import pandas as pd
import numpy as np
import time
import os
from nco import Nco


from .aux_funcs import get_date_list, get_url_info, get_near_coord, create_dataframe

def NORA3_ts(self, save_csv = False):
    """
    Extract times series of  the nearest gird point (lon,lat) from
    nora3 wave hindcast and save it as netcdf.
    height: default is 10, only applied for wind 
    """
    nco = Nco()
    self.variable.append('longitude') # keep info of regular lon
    self.variable.append('latitude')  # keep info of regular lat
    date_list = get_date_list(product=self.product, start_date=self.start_time, end_date=self.end_time)        

    tempfile = [None] *len(date_list)
    # Create directory
    dirName = 'temp'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

    # extract point and create temp files
    for i in range(len(date_list)):
        x_coor_str, y_coor_str, infile = get_url_info(product=self.product, date=date_list[i])
        tempfile[i] = 'temp/temp'+date_list.strftime('%Y%m%d')[i]+'.nc'
             
        if i==0:
            x_coor, y_coor, lon_near, lat_near = get_near_coord(infile=infile, lon=self.lon, lat=self.lat, product=self.product)        

        if self.product == 'NORAC_wave':
            opt = ['-O -v '+",".join(self.variable)+' -d '+x_coor_str+','+str(x_coor)]
        else:
            opt = ['-O -v '+",".join(self.variable)+' -d '+x_coor_str+','+str(x_coor.values[0])+' -d '+y_coor_str+','+str(y_coor.values[0])]




        for x in range(0, 6):  # try 6 times
            try:
                nco.ncks(input=infile , output=tempfile[i], options=opt)
            except:
                print('......Retry'+str(x)+'.....')
                time.sleep(10)  # wait for 10 seconds before re-trying
            else:
                break

    if os.path.exists(self.datafile):
        os.remove(self.datafile)
        print(self.datafile, 'already exists, so it will be deleted and create a new....')
    else:
        pass# print("....")
    
    #merge temp files
    ds = xr.open_mfdataset(paths=tempfile)    
    
    #Save in csv format    
    df = create_dataframe(product=self.product,ds=ds, lon_near=lon_near, lat_near=lat_near, outfile=self.datafile, variable=self.variable[:2],save_csv=save_csv, height=self.height)    

    #remove temp files
    for i in range(len(date_list)):
        os.remove(tempfile[i])
    
    return df


def NORA3_combined_ts(self, save_csv = True):
    self.variable = ['hs','tp','tm1','tm2','tmp','Pdir','thq', 'hs_sea','tp_sea','thq_sea' ,'hs_swell','tp_swell','thq_swell']
    self.product = 'NORA3_wave_sub'
    df_wave = NORA3_ts(self, save_csv=True)
    with open(self.datafile) as f:
        top_header_wave = f.readline()
    os.remove(self.datafile)
    self.variable = ['wind_speed','wind_direction']
    self.product = 'NORA3_wind_sub' 
    df_wind = NORA3_ts(self, save_csv=True)
    with open(self.datafile) as f:
        top_header_wind = f.readline()
    os.remove(self.datafile)
    
    # merge dataframes
    df = df_wind.join(df_wave)

    if save_csv == True:
        df.to_csv(self.datafile, index_label='time')
        top_header =  top_header_wave + top_header_wind + '\n'  
        with open(self.datafile, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(top_header.rstrip('\r\n') + '\n' + content)
    
    print('Data saved at: ' +self.datafile)

    return df


