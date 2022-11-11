import xarray as xr
#nc Valores standard
import numpy as np
import matplotlib.pyplot as plt
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



    #Forcing data
    #standard data array dimension is 217 make sure to make arrays with that dimension
    #or if you are making ur own file make sure all forcing parameters have same dim
    #uncomment to edit
    #time expect input to be divisions of day so 1 unit would be 24h
    #f["time"]=np.array()
    #Short-wave input expected higher values at midday
    #f["sw"]=np.array()
    #Long-wave input expected higher values at midday
    #f["lw"]=np.array()
    #f["qlat"]=np.array()
    #f["qsens"]=np.array()
    #f["tx"]=np.array()
    #f["ty"]=np.array()
    #f["precip"]=np.array(

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


def graph(f,p):
    "Plots parameters of file to better understand the expected inputs"
    for i in f:
        f[i].plot()
        plt.title(i)
        plt.show()
        plt.close()

    for i in p:
        p[i].plot()
        plt.title(i)
        plt.show()
        plt.close()

forc=xr.open_dataset("input_data/"+"beaufort_met.nc")
prof=xr.open_dataset("input_data/"+"beaufort_profile.nc")
f,p=save(forc,prof)
graph(f,p)