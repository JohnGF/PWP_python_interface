import xarray as xr
#nc Valores standard
import numpy as np
def save():
    """
    Uncomment and change np.array
    tips: \n f=60*, ordinary frequency, the number of oscillations (cycles) that occur each second of time.\nYou can use np.sin(2*np.pi*f*t+phase)*peak_irradiance to mimic solar cicle
    
            The model expects positive heat flux values to represent ocean warming. The time
            data field should contain a 1-D array representing fraction of day. For example, 
            for 6 hourly data, met_data['time'] should contain a number series that increases
            in steps of 0.25, such as np.array([1.0, 1.25, 1.75, 2.0, 2.25...]).
    Need to make sure dimensions match
    on this file vector have dimesions 217 [0,216]
    Common np commands
    np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
    Return evenly spaced numbers over a specified interval.
    numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    Return evenly spaced values within a given interval.


    """

    f=xr.open_dataset("input_data/"+"beaufort_met.nc")
    p=xr.open_dataset("input_data/"+"beaufort_profile.nc")
    
    #f["time"]=np.array([1,1.125,1.25 ... 28])| np.arange(1,28.125,0.125)
    #exemple
    #f["time"]=np.array()
    #f["sw"]=np.array()
    #f["lw"]=np.array()
    #f["qlat"]=np.array()
    #f["qsens"]=np.array()
    #f["tx"]=np.array()
    #f["ty"]=np.array()
    #f["precip"]=np.array()


    #p["z"]=np.array()
    #p["t"]=np.array()
    #p["s"]=np.array()
    #p["d"]=np.array()
    #p["lat"]=np.array()

    #uncomment to save
    #f.to_netcdf("input_data/myncforcing.nc")
    #p.to_netcdf("input_data/myncprofile.nc")

save()