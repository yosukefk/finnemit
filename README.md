FINN Emitter
============

[![Build Status](https://travis-ci.org/mbjoseph/finnemit.svg?branch=master)](https://travis-ci.org/mbjoseph/finnemit)
[![codecov](https://codecov.io/gh/mbjoseph/finnemit/branch/master/graph/badge.svg)](https://codecov.io/gh/mbjoseph/finnemit)



Emissions estimates for the Fire Inventory (FINN) wildfire emissions model (Wiedinmyer et al. 2011).
This library ingests a comma separated values (CSV) file generated from the FINN
pre-processor (https://github.com/yosukefk/finn_preproc), and generates a
CSV file with estimated emissions for a variety of compounds.

## Installing Python

If you already have python and pip installed, you can ignore this section.
If you do not have Python 3 installed, we recommend using Anaconda to install it
and pip.
For instructions see https://docs.anaconda.com/anaconda/install/

Once Anaconda is installed, create a virtual environment for FINN from
the terminal and ensure that pip is installed:

```bash
conda create -n finn
conda activate finn
conda install pip
```



## Installing finnemit

Assuming you have python and pip installed:

```bash
pip install git+https://github.com/mbjoseph/finnemit
```

## Estimating fire emissions

The main function in the finnemit library is `get_emissions`, which takes
as input a path to a CSV file generated using the FINN preprocessor, and
an output path.
In python:


```python
import finnemit

finnemit.get_emissions(infile = 'path/to/in.csv', outfile='path/to/emissions.csv')
```

If the `outfile` argument is not specified, an output filename will be
automatically generated and saved in the same directory as the input file.
This will write an output file (`path/to/emissions.csv` in the above example)
containing estimated emissions for each fire, and return a dictionary
summarizing the emissions results:

```
{
 'input_file': ...,
 'output_file': ...,
 'scenario': 'scen1',
 'emissions_file': '/home/max/Documents/finnemit/finnemit/data/emission-factors.csv',
 'fuel_load_file': '/home/max/Documents/finnemit/finnemit/data/fuel-loads.csv',
 'num_fires_total': 8223,

 'num_fires_processed': 8223,
 'num_urban_fires': 270,
 'num_removed_for_overlap': 0,
 'num_lct<=0|lct>17': 0,
 'num_antarctic': 0,
 'num_bare_cover': 5,
 'num_skipped_genveg_problem': 0,
 'num_skipped_bmass_assignment': 0,
 'num_scaled_to_100': 46,
 'num_vcf<50': 0,
 'num_fires_skipped': 5,
 'GLOBAL TOTAL (Tg) biomass burned (Tg)': 12.037323024765891,
 'Total Temperate Forests (Tg)': 0.08877815661654345,
 'Total Tropical Forests (Tg)': 0.0,
 'Total Boreal Forests (Tg)': 0.01790000845789989,
 'Total Shrublands/Woody Savannah(Tg)': 2.4718256886484546,
 'Total Grasslands/Savannas (Tg)': 6.808717171735319,
 'Total Croplands (Tg)': 0.5258629995156667,
 'TOTAL AREA BURNED (km2)': 8655.6848527776,
 'Total Temperate Forests (km2)': 17.493303915118453,
 'Total Tropical Forests (km2)': 0.0,
 'Total Boreal Forests (km2)': 2.77937573248018,
 'Total Shrublands/Woody Savannah(km2)': 1571.519449062231,
 'Total Grasslands/Savannas (km2)': 5745.856483761909,
 'Total Croplands (km2)': 922.680346385715,
 'TOTAL CROPLANDS CO (kg)': 47853532.95592565,
 'TOTAL CROPLANDS PM2.5 (kg)': 3381299.086885735,
 'CO': 0.8921078772803228,
 'NMOC': 0.3907541684396213,
 'NOx': 0.04117042348439978,
 'SO2': 0.010446153283846363,
 'PM2.5': 0.10925181938666846,
 'OC': 0.045101789462187035,
 'BC': 0.007266942589315823,
 'NH3': 0.010588814648214434,
 'PM10': 0.12186991425690463
}
```

### Acquiring chemical species estimates

Chemical speciation modeling can be used to estimate specific compounds, using
the output file generated by `get_emissions()`:

```python
finnemit.speciate(infile = "path/to/emissions.csv", outfile = "path/to/species.csv")
```

This will write the speciation estimates to the output file, and a log file
(named by replacing `.csv` with `_log.txt` in the output file) that summarizes
the results.  


## Meta

* Free software: BSD license

This package was created with Cookiecutter_ and the pyOpenSci/cookiecutter-pyopensci project template.

* Cookiecutter: https://github.com/audreyr/cookiecutter
* pyOpenSci/cookiecutter-pyopensci: https://github.com/pyOpenSci/cookiecutter-pyopensci
* audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

For more information on FINN, see:

Wiedinmyer, Christine, et al. "The Fire INventory from NCAR (FINN): A high
resolution global model to estimate the emissions from open burning."
Geoscientific Model Development 4.3 (2011): 625. 10.5194/gmd-4-625-2011
