
import netCDF4 as nc
import numpy as np
import xarray as xr
from datetime import datetime
fn = r'input_data/test.nc'
"""
ds = nc.Dataset(fn, 'w', format='NETCDF4')
time = ds.createDimension('time', None)
dtime = ds.createDimension('dtime', None) #data of days
sw = ds.createDimension('sw', None) #data of days
lw = ds.createDimension('lw', None) #data of days
qlat = ds.createDimension('qlat', None) #data of days
qsens = ds.createDimension('qsens', None) #data of days
tx = ds.createDimension('tx', None) #data of days
ty = ds.createDimension('ty', None) #data of days
precip = ds.createDimension('precip', None) #data of days

#lat = ds.createDimension('lat', 1)
#lon = ds.createDimension('lon', 1)

times = ds.createVariable('time', 'f4', ('time',))
sw = ds.createVariable('sw', 'f4', ('sw',))
lw = ds.createVariable('lw', 'f4', ('lw',))
qlat = ds.createVariable('qlat', 'f4', ('qlat',))
qsens = ds.createVariable('qsens', 'f4', ('qsens',))
tx = ds.createVariable('tx', 'f4', ('tx',))
ty = ds.createVariable('ty', 'f4', ('ty',))
precip = ds.createVariable('precip', 'f4', ('precip',))

value = ds.createVariable('value', 'f4', ('time', 'sw', 'lw',"qlat","qsens","tx","ty","precip"))
value.units = 'Unknown'
#lons = ds.createVariable('lon', 'f4', ('lon',))
#value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
#lats[:] = np.arange(40.0, 50.0, 1.0)
#lons[:] = np.arange(-110.0, -100.0, 1.0)
times[:] = np.arange(1,31.125,0.125)
#15 + 8 * np.random.randn(2, 2, 3)
sw[:]=np.zeros(np.shape(time))
lw[:]=np.zeros(np.shape(time))
qlat[:]=np.zeros(np.shape(time))
qsens[:]=np.zeros(np.shape(time))
tx[:]=np.zeros(np.shape(time))
ty[:]=np.zeros(np.shape(time))
precip[:]=np.zeros(np.shape(time))
sw[:]=np.zeros(np.shape(time))

ds.close()
dsc = nc.Dataset(fn, 'r', format='NETCDF4')
"""
time_v=np.arange(1,31.125,0.125)
qlat_v=np.zeros(np.shape(time_v))
qsens_v=np.zeros(np.shape(time_v))
lw_v=np.zeros(np.shape(time_v))
sw_v=np.zeros(np.shape(time_v))
tx_v=np.zeros(np.shape(time_v))
ty_v=np.zeros(np.shape(time_v))
precip_v=np.zeros(np.shape(time_v))

data_vars = {'qlat':(['time'], qlat_v, 
                {'units': 'W/m^2', 
                'long_name':'latent heat flux'}),

            'qsens':(["time"],qsens_v,
                 {'units': 'W/m^2', 
                'long_name':'Sensible heat flux'}),

            'lw':(["time"],lw_v,
                 {'units': 'W/m^2', 
                'long_name':'Long wave'}),
            'sw':(["time"],sw_v,
                 {'units': 'W/m^2', 
                'long_name':'Short wave'}),
            'tx':(["time"],tx_v,
                 {'units': 'N/m^2', 
                'long_name':'Short wave'}),
            'ty':(["time"],ty_v,
                 {'units': 'N/m^2', 
                'long_name':'Short wave'}),
            'precip':(["time"],precip_v,
                 {'units': 'm/s', 
                'long_name':'Percipitation'}),
                
                          
                          }
coords = {'time': (['time'],time_v ),'dtime':(['dtime'],[0])}  
attrs = {'creation_date':str(datetime.now()), 
         'author':'Student FCUL', 
         'email':'address@email.com'}  
df = xr.Dataset(data_vars, coords, attrs)
df.to_netcdf("input_data/myncforcing_test.nc")
#print(df)
#####################
#Profile

z_v=np.arange(0,1600,200)
lat_v=-53.513
qsens_v=np.zeros(np.shape(z_v))
s_v=np.zeros(np.shape(z_v))
t_v=np.zeros(np.shape(z_v))
oxy_v=np.zeros(np.shape(z_v))

data_vars = {'lat':([], lat_v, 
                {'units': 'W/m^2', 
                'long_name':'latent heat flux'}),

            's':(["z"],s_v,
                 {'units': 'W/m^2', 
                'long_name':'Sensible heat flux'}),

            't':(["z"],t_v,
                 {'units': 'W/m^2', 
                'long_name':'Long wave'}),
            'oxy':(["z"],oxy_v,
                 {'units': 'W/m^2', 
                'long_name':'O2'}),
                
                          
                          }
coords = {'z': (['z'],z_v )}  
attrs = {'creation_date':str(datetime.now()), 
         'author':'Student FCUL', 
         'email':'address@email.com'}  
dp = xr.Dataset(data_vars, coords, attrs)
dp.to_netcdf("input_data/myncprofile_test.nc")
#print(dp)