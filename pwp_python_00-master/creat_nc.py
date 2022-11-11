import xarray as xr
import netCDF4 as nc
#nc Valores standard
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
from datetime import datetime
# '\033[1m' + 'Python' + '\033[0m'
def save(f,p):
    """
   
    Uncomment and change np.array.
    
    tips: f=60*, ordinary frequency, the number of oscillations (cycles) that occur each second of time.
    
    You can use np.sin(2*np.pi*f*t+phase)*peak_irradiance to mimic solar cicle
    
    The model expects positive heat flux values to represent ocean warming. The time
    data field should contain a 1-D array representing fraction of day. For example, 
    for 6 hourly data, met_data['time'] should contain a number series that increases
    in steps of 0.25, such as np.array([1.0, 1.25, 1.75, 2.0, 2.25...]).
    Need to make sure dimensions match
    on this file vector have dimesions 217 [0,216]
    
    Common np commands:
    
    numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    Return evenly spaced numbers over a specified interval.
    
    numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    Return evenly spaced values within a given interval.
    

    """
    #example
    
    #f["time"]=np.array([1,1.125,1.25 ... 28]) || np.arange(1,28.125,0.125)||
    #np.linspace(1,28,217)
    print(f["time"])#shows the array stored in key "time" you can do the same for other paramenters

    #you can use use np.random.rand to make a random matrix with values between [0,1]
    #np.random.rand(dimarray_i,dimarray_j) and then you can multiply and then add it to your parameter to simulate fluctuations on readinfs
    
    #Forcing data
    #standard data array dimension is 217 make sure to make arrays with that dimension
    #or if you are making ur own file make sure all forcing parameters have same dim
    #uncomment to edit
    #time expect input to be divisions of day so 1 unit would be 24h
    
    #f["time"]=np.arange(1,31.125,0.125)
    #Short-wave input expected higher values at midday
    #f["sw"]=np.zeros(np.shape(f["time"]))+100
    #Long-wave input expected higher values at midday
    #f["lw"]=np.zeros(np.shape(f["time"]))
    #f["qlat"]=np.zeros(np.shape(f["time"]))
    #f["qsens"]=np.zeros(np.shape(f["time"]))
    #f["tx"]=np.zeros(np.shape(f["time"]))
    #f["ty"]=np.zeros(np.shape(f["time"]))
    #f["precip"]=np.zeros(np.shape(f["time"]))

    #Profile data
    #standard data array dimension is 11000 make sure to make arrays with that dimension
    #or if you are making ur own file make sure all profile parameters have same dim exept lat(wich can be one value)
    #p["z"]=np.array()
    #p["t"]=np.array()
    #p["s"]=np.array()
    #p["d"]=np.array()
    #p["lat"]=np.array()

    
    f.to_netcdf("input_data/myncforcing.nc")
    p.to_netcdf("input_data/myncprofile.nc")
    return f,p
def creat_future_2():
    #example
    #ncf_new=ncf.Dataset()
    np.random.seed(0)

    time = np.arange(1,31.125,0.125)
    #15 + 8 * np.random.randn(2, 2, 3)
    sw=np.zeros(np.shape(time))+100
    lw=np.zeros(np.shape(time))
    qlat=np.zeros(np.shape(time))
    qsens=np.zeros(np.shape(time))
    tx=np.zeros(np.shape(time))
    ty=np.zeros(np.shape(time))
    precip=np.zeros(np.shape(time))

    lon = [[-99.83, -99.32], [-99.79, -99.23]]

    lat = [[42.25, 42.21], [42.63, 42.59]]

    #time = pd.date_range("2014-09-06", periods=3)


    da = xr.DataArray(
        data=[sw,lw,qlat,qsens],

        dims=["x", "y", "time"],

        coords=dict(

        time=time,
        )

    ,

    attrs=dict(

        description="Ambient temperature.",

        units="degC",
    ),
    )
    
    return da
def creat_future_1():

    fn = r'input_data/test.nc'
    ds = nc.Dataset(fn, 'w', format='NETCDF4')
    time = ds.createDimension('time', None)
    dtime = ds.createDimension('dtime', None) #data of days

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
    return ds
def creat():
    time_v=np.arange(1,31.125,0.125)
    qlat_v=np.zeros(np.shape(time_v))
    qsens_v=np.zeros(np.shape(time_v))
    lw_v=np.zeros(np.shape(time_v))
    sw_v=np.zeros(np.shape(time_v))+100
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

    #print(df)
    #####################
    #Profile

    z_v=np.arange(0,1600,200)
    lat_v=-53.513
    qsens_v=np.zeros(np.shape(z_v))
    s_v=np.zeros(np.shape(z_v))+20
    t_v=np.zeros(np.shape(z_v))+25
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
    df.to_netcdf("input_data/myncforcing_test.nc")
    dp.to_netcdf("input_data/myncprofile_test.nc")


    return df,dp
def graph(f,p):
    "Plots parameters of file to better understand the expected inputs"
    for i in f:
        f[i].plot()
        plt.title(i)
        #plt.gca().invert_yaxis()
        plt.show()
        plt.close()

    for i in p:
        
        if i=="s" or i=="t" or i=="oxy":

            p[i].plot(y="z")
            plt.plot
            plt.title(i)
            plt.gca().invert_yaxis()
            plt.show()
            plt.close()

        else:
            p[i].plot()
            plt.title(i)
            #plt.gca().invert_yaxis()
            plt.show()
            plt.close()
#files can be found PL1-20220930\pwp_python_00-master\input_data
forc=xr.open_dataset("input_data/"+"SO_met_100day.nc")
prof=xr.open_dataset("input_data/"+"SO_profile1.nc")
#f,p=save(forc,prof)
f,p=creat()
#graph(f,p)
