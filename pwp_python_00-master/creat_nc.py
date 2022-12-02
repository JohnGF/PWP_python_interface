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
    #f["sw"]=f["sw"]+100
    #Long-wave input expected higher values at midday
    #f["lw"]=f["lw"]
    #f["qlat"]=["qlat"]
    #f["qsens"]=["qsens"]
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
def copy_nc(fc,pc):
    # You can chagne this values variables are instaciating with 0 filling parameters
    time_v=fc["time"].values
    qlat_v=fc["qlat"].values
    qsens_v=fc["qsens"].values
    lw_v=fc["lw"].values
    sw_v=fc["sw"].values
    tx_v=fc["tx"].values*0
    ty_v=fc["ty"].values*0
    precip_v=fc["precip"].values+np.average(fc["precip"].values)*0.05#aumento 5%
    #
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
                    'long_name':'Wind stress x'}),
                'ty':(["time"],ty_v,
                    {'units': 'N/m^2', 
                    'long_name':'Wind stress y'}),
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
    # You can chagne this values variables are instaciating with 0 filling parameters
    z_v=pc["z"].values
    lat_v=-53.513
    s_v=pc["s"].values
    t_v=pc["t"].values
    d_v=pc["d"].values
    oxy_v=np.zeros(np.shape(z_v))
    #

    data_vars = {'lat':([], lat_v, 
                    {'units': 'W/m^2', 
                    'long_name':'latitude'}),

                's':(["z"],s_v,
                    {'units': 'W/m^2', 
                    'long_name':'Salinity'}),

                't':(["z"],t_v,
                    {'units': 'W/m^2', 
                    'long_name':'Temperature'}),
                'd':(["z"],d_v,
                    {'units': 'W/m^2', 
                    'long_name':'Density'}),
                'oxy':(["z"],oxy_v,
                    {'units': 'W/m^2', 
                    'long_name':'O2'}),
                    
                            
                            }
    coords = {'z': (['z'],z_v )}  
    attrs = {'creation_date':str(datetime.now()), 
            'author':'Student FCUL', 
            'email':'address@email.com'} #you can put your email here to brand your nc file
    dp = xr.Dataset(data_vars, coords, attrs)
    #you can change this names to create new files or you can rename in file explorer as to not overwrite
    
    df.to_netcdf("input_data/copy_test.nc")
    dp.to_netcdf("input_data/copy_prof_test.nc")
    #If you change it dont forget to change name in the run_me.py file to your new name file

    return df,dp
def creat():
    #check average of variables of real data
    # You can chagne this values variables are instaciating with 0 filling parameters
    time_v=np.arange(1,3.125,0.125)
    qlat_v=np.zeros(np.shape(time_v))
    qsens_v=np.zeros(np.shape(time_v))
    lw_v=np.zeros(np.shape(time_v))
    sw_v=np.zeros(np.shape(time_v))+100#this one is filled with the value 100
    #qlat_v=[100*(np.sin(2*x*np.pi)) for x in time_v]
    #qsens_v=[40*(np.sin(2*x*np.pi+np.pi)) for x in time_v]
    #lw_v=[-100*abs(np.sin(x*np.pi)) for x in time_v]
    #sw_v=[400*abs(np.sin(x*np.pi)) for x in time_v]
    
    tx_v=np.zeros(np.shape(time_v))+0.01
    ty_v=np.zeros(np.shape(time_v))+0.05
    precip_v=np.zeros(np.shape(time_v))+1.2e-06
    #
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
                    'long_name':'Wind stress x'}),
                'ty':(["time"],ty_v,
                    {'units': 'N/m^2', 
                    'long_name':'Wind stress y'}),
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
    # You can chagne this values variables are instaciating with 0 filling parameters
    z_v=np.arange(0,1600,200)
    lat_v=-53.513
    qsens_v=np.zeros(np.shape(z_v))
    s_v=np.zeros(np.shape(z_v))+20 
    t_v=np.zeros(np.shape(z_v))+25
    d_v=np.zeros(np.shape(z_v))+25

    oxy_v=np.zeros(np.shape(z_v))
    #

    data_vars = {'lat':([], lat_v, 
                    {'units': 'W/m^2', 
                    'long_name':'latitude'}),

                's':(["z"],s_v,
                    {'units': 'W/m^2', 
                    'long_name':'Salinity'}),

                't':(["z"],t_v,
                    {'units': 'W/m^2', 
                    'long_name':'Temperature'}),
                'd':(["z"],d_v,
                    {'units': 'W/m^2', 
                    'long_name':'Density'}),
                'oxy':(["z"],oxy_v,
                    {'units': 'W/m^2', 
                    'long_name':'O2'}),
                    
                            
                            }
    coords = {'z': (['z'],z_v )}  
    attrs = {'creation_date':str(datetime.now()), 
            'author':'Student FCUL', 
            'email':'address@email.com'} #you can put your email here to brand your nc file
    dp = xr.Dataset(data_vars, coords, attrs)
    #you can change this names to create new files or you can rename in file explorer as to not overwrite
    
    df.to_netcdf("input_data/myncforcing_test.nc")
    dp.to_netcdf("input_data/myncprofile_test.nc")
    #If you change it dont forget to change name in the run_me.py file to your new name file

    return df,dp

def graph(f,p):
    """
    Plots parameters of file
    Can be used to better understand the expected inputs if used on pre-made files
    """
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
            plt.gca().invert_yaxis()#inver axis has to start zero on top
            plt.show()
            plt.close()

        else:
            p[i].plot()
            plt.title(i)
            #plt.gca().invert_yaxis()
            plt.show()
            plt.close()
#files can be found PL1-20220930\pwp_python_00-master\input_data
#change names to files to edit
forc=xr.open_dataset("input_data/"+"beaufort_met.nc")
prof=xr.open_dataset("input_data/"+"beaufort_profile.nc")
#fc,pc=save(forc,prof)
#f,p=copy_nc(forc,prof)
f,p=creat()
graph(f,p)
