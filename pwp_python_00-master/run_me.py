import PWP

def run_me(met_file="myncforcing.nc",pro_file="myncprofile.nc"):
    """
    Default run_me: \n
    met_file="myncforcing.nc",pro_file="myncprofile.nc"
    """
    return PWP.run(met_data=met_file, prof_data=pro_file, suffix='demo1_nodiff', save_plots=True, diagnostics=False)
forcing, pwp_out = run_me()