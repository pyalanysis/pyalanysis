# Examples

## Set-up
The set-up assumes that you have a Jupyter notebook environment set-up in your
default environment.

### Micromamba
Using [micromamba](https://github.com/mamba-org/mamba),
```
(default) $ micromamba env create -f environment.yml
(default) $ micromamba activate pyalanysis_demo_env
(pyalanysis_demo_env) $ python -m ipykernel install --user --name pyalanysis_demo_env --display-name "Pyalanysis_demo_env"
(pyalanysis_demo_env) $ micromambda deactivate
(default) $ PYALANYSIS_MINES_USERNAME = "your-username" ; \
  PYALANYSIS_MINES_PASSWORD = "your-password" ; \
  jupyter notebook
```
you can create a username and password on the [site of the Colorado School of
Mines](https://eogdata.mines.edu/eog/EOG_sensitive_contents), read the full
announcement [of the Earth Observation
Group](https://eogdata.mines.edu/products/register/).

### Anaconda
The process is similar to micromamba,
```
(default) $ conda env create -f environment.yml
(default) $ conda activate pyalanysis_demo_env
(pyalanysis_demo_env) $ python -m ipykernel install --user --name pyalanysis_demo_env --display-name "Pyalanysis_demo_env"
(pyalanysis_demo_env) $ micromambda deactivate
(default) $ PYALANYSIS_MINES_USERNAME = "your-username" ; \
  PYALANYSIS_MINES_PASSWORD = "your-password" ; \
  jupyter notebook
```


## Examples
- Show ALAN in the Netherlands, shows the ALAN in the Netherlands for a month
with stray light correction.
