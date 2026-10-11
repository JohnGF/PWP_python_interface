# Price-Weller-Pinkel (PWP) Ocean Mixed Layer Model in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scientific Computing](https://img.shields.io/badge/Scientific%20Computing-xarray%20%7C%20numpy-brightgreen?style=for-the-badge)
![Oceanography](https://img.shields.io/badge/Domain-Oceanography-blueviolet?style=for-the-badge)

This is a Python implementation of the **Price-Weller-Pinkel (PWP) ocean mixed layer model**. This code is based on the MATLAB implementation of the PWP model originally written by Peter Lazarevich and Scott Stoermer (University of Rhode Island) and later modified by Byron Kilbourne and Sarah Dewey (University of Washington).

This package includes a Python implementation of the numerical routines (`PWP.py`), auxiliary and plotting functions (`PWP_helper.py`), and a user-friendly interface (`creat_nc.py`, `run_me.py`) to easily simulate upper ocean thermodynamics and momentum.

---

## 🌊 How the Model Works

The PWP model predicts the evolution of the upper ocean's temperature, salinity, and momentum driven by surface fluxes (wind, heat, and freshwater). It applies these fluxes to an initial profile and computes mixing based on stability criteria.

The simulation workflow is illustrated below:

```mermaid
graph TD
    A[Initial State: Temperature, Salinity, Velocity Profiles] --> B[Apply Surface Forcing: Heat, Freshwater, Wind Stress]
    B --> C[Relieve Static Instability (Free Convection)]
    C --> D{Check Bulk Richardson Number `Rb`}
    D -->|Rb < 0.65| E[Bulk Mixing to MLD]
    D -->|Rb >= 0.65| F{Check Gradient Richardson Number `Rg`}
    E --> F
    F -->|Rg < 0.25| G[Gradient Mixing (Shear Instability)]
    F -->|Rg >= 0.25| H[Apply Diapycnal Diffusion]
    G --> H
    H --> I[Advance Time Step]
    I -.-> B
```

### 🧮 Mathematical Background

The PWP model uses the following key physical mechanisms to determine when and how mixing occurs in the water column:

1. **Static Instability**: Whenever the density profile becomes top-heavy (density increasing toward the surface), the model mixes the unstable layers to simulate free convection until static stability is restored.
2. **Bulk Richardson Number ($R_b$)**: Mixing is driven by wind shear acting on the whole mixed layer. The bulk Richardson number is defined as:
   $$R_b = \frac{g \Delta \rho h}{\rho_0 (\Delta U)^2 + (\Delta V)^2}$$
   If $R_b < 0.65$, the mixed layer deepens.
3. **Gradient Richardson Number ($R_g$)**: Shear instability at the base of the mixed layer causes local turbulent mixing.
   $$R_g = \frac{g \frac{\partial \rho}{\partial z}}{\rho_0 \left( \left(\frac{\partial U}{\partial z}\right)^2 + \left(\frac{\partial V}{\partial z}\right)^2 \right)}$$
   If $R_g < 0.25$, adjacent grid cells are mixed.

---

## 🛠 Required Libraries

To run this code, you'll need Python 3 and the following libraries:

+ `numpy`
+ `scipy`
+ `matplotlib`
+ `xarray`
+ `seawater` (or `gsw`)

You can install the dependencies via pip:
```bash
pip install -r requirements.txt
# or individually
pip install xarray seawater numpy scipy matplotlib
```

---

## 🚀 Running the Code

Open **`run_me.py`** to run forcing and profiles netCDF files stored in the **`input_data`** directory. You can edit the `example` variable to switch modes:

```python
import PWP_helper as phf

# Run demo 2 with all forcing ON
phf.run_demo2(winds_ON=True, emp_ON=True, heat_ON=True, drag_ON=True)
```

Alternatively, from an interactive Python session:
```python
import PWP
import PWP_helper as phf

forcing_fname = 'input_data/SO_met_30day.nc'
prof_fname = 'input_data/SO_profile1.nc'
p = {'rkz': 1e-6, 'dz': 2.0, 'max_depth': 500.0}

forcing, pwp_out = PWP.run(met_data=forcing_fname, prof_data=prof_fname, save_plots=True, param_kwds=p)
```

---

## 📁 Input Data Requirements

The PWP model requires two input netCDF files:
1. **Surface Forcing File**: Must contain the following 1-D time series (fraction of day):
   - `time`: Time (days)
   - `sw`: Net shortwave radiation (W/m²)
   - `lw`: Net longwave radiation (W/m²)
   - `qlat`: Latent heat flux (W/m²)
   - `qsens`: Sensible heat flux (W/m²)
   - `tx`: Eastward wind stress (N/m²)
   - `ty`: Northward wind stress (N/m²)
   - `precip`: Precipitation rate (m/s)

2. **Initial Profile File**: Must contain 1-D arrays for depth levels:
   - `z`: Depth levels (m)
   - `t`: Temperature profile (°C)
   - `s`: Salinity profile (PSU)
   - `lat`: Latitude of profile

*Note: Positive flux values correspond to heat/freshwater gained by the ocean.*

---

## ⚙️ Default Settings

Key configuration parameters (and defaults) that can be passed via `param_kwds`:
- **`dt`**: Time-step increment in hours [3]
- **`dz`**: Depth increment in meters [1]
- **`max_depth`**: Max depth of vertical coordinate in meters [100]
- **`rb`**: Critical bulk Richardson number [0.65]
- **`rg`**: Critical gradient Richardson number [0.25]
- **`winds_ON`, `emp_ON`, `heat_ON`**: Flags to toggle respective surface forcings [True]

## ✨ Future Work
+ Create an option to add a passive tracer to the model.
+ Incorporate a rudimentary sea-ice model to provide ice induced heat and salt fluxes.
