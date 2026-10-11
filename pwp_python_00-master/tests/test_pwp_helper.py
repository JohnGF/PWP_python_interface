import pytest
import numpy as np
import sys
import os
import xarray as xr

# Add parent directory to path to import PWP_helper
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import PWP_helper as phf

def test_set_params():
    # Test setting parameters
    lat = 45.0
    params = phf.set_params(lat, dt=3.0, dz=1.0)
    
    assert params['lat'] == lat
    assert params['dt'] == 3.0 * 3600.0 # converted to seconds
    assert params['dz'] == 1.0
    assert 'f' in params
    assert 'cpw' in params
    assert 'g' in params
    
def test_prep_data():
    # Create simple mock xarray datasets
    time_val = np.array([0.0, 0.25, 0.5])
    met_ds = xr.Dataset({
        'time': (['time'], time_val),
        'sw': (['time'], np.array([100.0, 150.0, 0.0])),
        'lw': (['time'], np.array([-50.0, -50.0, -50.0])),
        'qlat': (['time'], np.array([-20.0, -20.0, -20.0])),
        'qsens': (['time'], np.array([-10.0, -10.0, -10.0])),
        'tx': (['time'], np.array([0.1, 0.1, 0.1])),
        'ty': (['time'], np.array([0.0, 0.0, 0.0])),
        'precip': (['time'], np.array([0.0, 0.0, 0.0]))
    })
    
    z_val = np.array([0.0, 10.0, 20.0])
    prof_ds = xr.Dataset({
        'z': (['z'], z_val),
        't': (['z'], np.array([20.0, 19.0, 18.0])),
        's': (['z'], np.array([35.0, 35.0, 35.0])),
        'd': (['z'], np.array([1024.0, 1025.0, 1026.0])),
        'lat': ([], 45.0)
    })
    
    params = phf.set_params(45.0, dt=3.0, dz=1.0, max_depth=20.0)
    
    # prep_data returns forcing, pwp_out, params
    forcing, pwp_out, params_out = phf.prep_data(met_ds, prof_ds, params)
    
    assert 'time' in forcing
    assert 'temp' in pwp_out
    assert 'sal' in pwp_out
    
    # Check depth interpolation
    assert len(pwp_out['z']) == 21 # 0 to 19 meters
    
def test_custom_div_cmap():
    # Test colormap creation
    cmap = phf.custom_div_cmap(numcolors=11, name='test_cmap')
    assert cmap.name == 'test_cmap'
    assert cmap.N == 11
