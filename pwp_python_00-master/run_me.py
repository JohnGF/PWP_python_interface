import PWP
import PWP_helper as phf

example=3 #change this value to run different runs

def run_me(met_file="myncforcing.nc",pro_file="myncprofile.nc"):
    """
    Default run_me: \n
    met_file="myncforcing.nc",pro_file="myncprofile.nc"
    """
    return PWP.run(met_data=met_file, prof_data=pro_file, save_plots=True, diagnostics=False )
if example==0:
    forcing, pwp_out = run_me()
if example==1:
    phf.run_demo1()
if example==2:
    phf.run_demo2(winds_ON=True, emp_ON=True, heat_ON=True, drag_ON=True)
if example==3: #run created nc file throws a error if not created/wrong name
    run_me("myncforcing_test.nc","myncprofile_test.nc")
if example==4: #run created nc file throws a error if not created/wrong name
    run_me("copy_test.nc","copy_prof_test.nc")
