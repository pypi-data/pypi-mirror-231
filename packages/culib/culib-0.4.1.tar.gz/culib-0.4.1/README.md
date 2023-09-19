# CULib

[![Latest Release](https://gitlab.melexis.com/ple/culib/-/badges/release.svg)](https://gitlab.melexis.com/ple/culib/-/releases)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pipeline status](https://gitlab.melexis.com/ple/culib/badges/main/pipeline.svg)](https://gitlab.melexis.com/ple/culib/-/commits/main)
[![coverage report](https://gitlab.melexis.com/ple/culib/badges/main/coverage.svg)](https://gitlab.melexis.com/ple/culib/-/commits/main)

Coils Utilities Library (CULib) is a Python package for modeling air-core electromagnet coils and calculating their physical characteristics based on their geometry and wire informations.
It also includes functions for calculating and plotting static magnetic field in 3D or in 1D along their central axis.

CULib allows integration of "real-life" characteristics, such as :
- Coil thickness (because of an external radius and internal radius) and coil length
- Number of turns calculation based on coil geometrical dimensions for a given wire size and shape
- Wire size declaration based on standard AWG sizes, or custom definition (i.e : squared section wire, foil wire... )
- Automatic recalculation of coils parameters in case of modification of geometric params or wire type (useful for wire selection and recalculation of all params based on suppliers capabilities)
- Calculation of voltage and power needed based on current injected and resistance calculation
- Temperature effect on wire resistivity and coil resistance/power
- Estimation of self-inductance and time constant

Supported coil shapes : **Circular** and **Rectangular**

Link to full documentation : https://ple.pages.melexis.com/culib/

## Examples
Please refer to [examples](https://gitlab.melexis.com/ple/culib/-/tree/main/examples) folder for various details on how to use it

- Basic one :
```python
import culib as cul

mycoil = cul.CircularCoil(
    axis = 'x_mm',                # Axis of revolution (x axis in mm)
    r_in_mm = 14,                 # Inner coil radius (in mm
    r_out_mm = 40,                # Outer coil radius (in mm)
    L_mm = 32,                    # Coil length (in mm)
    pos_mm = 20,                  # Position of coil center on axis (in mm) (voluntarily offsetted here)
    cur_A = 3.2,                  # Current applied (in A)
    wire = cul.RoundWire(awg=22), # Wire def. via Wire object, defined with AWG 22 (American Wire Gauge)
)

# Print all coil characteristics
print(mycoil)

# Calc and plot field in 1D
df_field = cul.init_df_field()        
df_field = mycoil.calc_field(df_field)
cul.plot_field(df_field, axis='x_mm', Baxis='Bx_total_mT')
```

## Installation
### Via pip
- Type the following in your **venv** or in your **Google Colab** (for **Colab**, don't forget to add ! before the command)
    ```python
    pip install git+https://pip:x8tBdzXvtxJpBwAgM2YH@gitlab.melexis.com/ple/culib.git
    ```
- Then import in your code
    ```python
    import culib as cul
    ```
- You're ready to use CULib

## Requirements
CULib requires Python >= **3.8.0** and the packages listed below

_Note_ : packages will be **automatically** installed by using pip as described on the previous step Installation

### Altair and vl-convert
CULib uses **Altair** for plotting charts.
It uses version >= 5.0 for its support for saving chart as .png easily with **vl-convert**.
Using versions below 5.0 will work for displaying and saving as .html, but saving charts as .png might cause issues.
### SciPy
Required for specific calculations on 3D fields from analytic formulas.
### Numpy and Pandas
Standards for science, they are also part of requirements for SciPy and Altair.


## Some specificities
### Units
All parameters reprensenting a physical characteristic contain the unit at the end of its name. Drawback is that it's a bit verbose, but at least it is self-explanatory and will help avoiding stupid mistakes due to conversions.

Examples :
- `x_mm` : position in x axis in mm
- `Bx_total_mT` : Magnetic field flux density for x component in mT (`"total"` meaning it's the sum of every contributors to x component)
- `mycoil.res_ohm` : resistance in Ohm
- `mycoil.temp_degC` : temperature in degrees Celsius
- `mycoil.cur_A` : coil current in Ampere
- `mycoil.wire.d_in_mm` : Wire inner diameter (without insulation) in mm
- `...`

### Auto recalc when changing a coil or wire parameter
At the object creation, attributes that can be deducted from the given parameters are automatically calculated. Equations have been arranged in a way that, from given inputs, outputs can be calculated without conflicts.
You can then access a coil or wire parameter via `print(mycoil.res_ohm)`

Updating one parameter via `mycoil.r_in_mm = 12` will trigger the recalc of all parameters depending on it if `mycoil.is_autorecalc` is `True` (`True` by default).

Example :
```python
>>> mycoil = cul.CircularCoil(
... axis = 'x_mm',              # Axis of revolution (x axis in mm)
... r_in_mm = 14,               # Inner coil radius (in mm)
... r_out_mm = 40,              # Outer coil radius (in mm)
... L_mm = 32,                  # Coil length (in mm)
... pos_mm = 0,                 # Position of coil center on axis (in mm)
... cur_A = 3.2,                # Current applied (in A)
... wire=cul.RoundWire(awg=22), # Wire definition via Wire object, with AWG number 22
... )

>>> print(mycoil.res_ohm)
12.792006481231436

>>> mycoil.r_out_mm = 35 # Decrease the outer radius of your coil (from 40mm to 35mm)
>>> print(mycoil.res_ohm)
9.559168241965974
```

### Loggings
Loggings have been configured and can be displayed (implementation via the standard lib `logging`).

To init them, use `culib.init_culib_logging(log_level)` at the beginning of your code, with `log_level` a compliant name with `logging` lib, like `"WARNING"`,`"DEBUG"`, `logging.INFO`... (refer to `logging` doc for more info).

You can also select a specific log_level for a specific function despite the main log_level, useful in case of debug needed, etc...

i.e : you want to display by default `log_level="WARNING"`, but in a specific call of the function .plot_field() you want to display also `"INFO"` level
```python
import culib as cul
cul.init_culib_logging(log_level="WARNING")
###
### Do stuff, culib stuff will log only "WARNING" level
###
cul.plot_field(..., log_level="INFO") # Will also log "INFO" level, but only for this call
```

## Contributions and Ideas for future
Contributions will be welcome, do not hesitate to contact me via chat/mail (PLE), open an issue via this Gitlab and/or open a Merge Request.
Please check the [CONTRIBUTING.md](https://gitlab.melexis.com/ple/culib/-/blob/main/CONTRIBUTING.md) file for more details.

## References
### Physics
Most equations and reasonings for characteristics calculation in this package are based on work from **Jake J. Abbott** :
- Jake J. Abbott; "Parametric design of tri-axial nested Helmholtz coils", Review of Scientific Instruments vol. 86 no. 5 p. 054701, May 2015, [doi: 10.1063/1.4919400](https://doi.org/10.1063/1.4919400)

Field spatial expressions are based on work from :
- David Jiles; "Introduction to Magnetism and Magnetic Materials", Section I) 1.3.4 page 24, Year 2016, CRC Press, ISBN : 978-1-4822-3887-7
- S. Hampton, R. A. Lane, R. M. Hedlof, R. E. Phillips, C. A. Ordonez; "Closed-form expressions for the magnetic fields of rectangular and circular finite-length solenoids and current loops", AIP Advances 10, 065320 (2020), June 2020, [doi: 10.1063/5.0010982](https://doi.org/10.1063/5.0010982)
