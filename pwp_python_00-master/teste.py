#run( param_kwds{})
import PWP as pwp
import PWP_helper as pwph
import numpy as np
import seawater as sw
def user_params(dt=3,advance=False,earth=True ):
    advance=input("Modo advance [y/n]")
    params = {}
    lat=input("Latitude")
    params['dt'] = 3600.0*dt
    params['dt_d'] = params['dt']/86400.

    params['lat'] = lat
    params['f'] = sw.f(lat)
    
    params['max_depth'] = input("profundiade maxima") #profundidade maxima
    if (earth==False):
        params['g'] = input("Aceleração gravitica")
        
    if (advance==1 or advance=="y"):
        params['rkz'] = input("Background vertical diffusion (m**2/s). [0.]")
        params['rb'] = input("Critical Gradient Richardson number [0.25]")
        params['rg'] = input("Critical Bulk Richardson number [0.65]")
        params['cpw'] = input("Calor especifico liquido (água)[4183.3 J/kgC]")
        #params['ucon'] = (0.1*np.abs(params['f']))
        params['mld_thresh'] = input("Density criterion for MLD (kg/m3). [1e-4]")
        params['dz'] = input("Delta Profundidade")
        params['dt_save'] = input("Passo de tempo")
        params['winds_ON'] = input("Wind effect [True|False]")
        params['emp_ON'] = input("Freshwater effect [True|False]")
        params['heat_ON'] = input("Heat effect [True|False]")
        params['drag_ON'] = input("Drag effect [True|False]")
        params['beta1'] = input("coeficiente de extinção ondas longas valor [valor tipico 0.6]") #longwave extinction coefficient (meters). [0.6]
        params['beta2'] = input("coeficiente de extinção ondas curtas valor [valor tipico 20]")  #shortwave extinction coefficient (meters). [20]
    else:
        dt=3.; dz=1.; max_depth=100.; mld_thresh=1e-4; dt_save=1.; rb=0.65; 
        rg=0.25; rkz=0.; beta1=0.6; beta2=20.0; heat_ON=True; winds_ON=True;
        emp_ON=True; drag_ON=True
        params['dt'] = 3600.0*dt
        params['dt_d'] = params['dt']/86400.
        params['dz'] = dz
        params['dt_save'] = dt_save
        params['lat'] = lat
        params['rb'] = rb
        params['rg'] = rg
        params['rkz'] = rkz
        params['beta1'] = beta1
        params['beta2'] = beta2
        params['max_depth'] = max_depth

        params['g'] = 9.81
        params['f'] = sw.f(lat)
        params['cpw'] = 4183.3
        params['ucon'] = (0.1*np.abs(params['f']))
        params['mld_thresh'] = mld_thresh

        params['winds_ON'] = winds_ON
        params['emp_ON'] = emp_ON
        params['heat_ON'] = heat_ON
        params['drag_ON'] = drag_ON
            

forcing_fname = 'beaufort_met.nc'
prof_fname = 'beaufort_profile.nc'
print("Running Test Case 1 with data from Beaufort gyre...")
#forcing, pwp_out = pwp.run(met_data=forcing_fname, prof_data=prof_fname, suffix='demo1_nodiff',param_kwds=user_params(dt=3,advance=False,earth=True ), save_plots=True, diagnostics=False)
pwph.set_params(lat, dt=3., dz=1., max_depth=100., mld_thresh=1e-4, dt_save=1., rb=0.65, rg=0.25, rkz=0., beta1=0.6, beta2=20.0, heat_ON=True, winds_ON=True, emp_ON=True, drag_ON=True)
