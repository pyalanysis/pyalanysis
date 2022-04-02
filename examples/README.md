# Examples

## Set-up
The set-up assumes that you have a Jupyter notebook environment set-up in your
default environment.

### Micromamba
Using [micromamba](https://github.com/mamba-org/mamba),
```
(default) $ micromamba create -f environment.yml
(default) $ micromamba activate pyalanysis_demo_env
(pyalanysis_demo_env) $ python -m ipykernel install --user --name pyalanysis_demo_env --display-name "Pyalanysis_demo_env"
(pyalanysis_demo_env) $ micromamba deactivate
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
(pyalanysis_demo_env) $ micromamba deactivate
(default) $ PYALANYSIS_MINES_USERNAME = "your-username" ; \
  PYALANYSIS_MINES_PASSWORD = "your-password" ; \
  jupyter notebook
```

### Jupyter
Some tuning of your jupyter may be required to work with Kepler.gl and/or
Deck.gl. Monitor your output of jupyter for the following error,
```
[IPKernelApp] ERROR | No such comm target registered: jupyter.widget.control
[IPKernelApp] WARNING | No such comm: b92c986f-3a56-4eb3-9f69-603e934d9bf4
```
A [stackoverflow
post](https://stackoverflow.com/questions/41743837/no-such-comm-target-registered-error-in-ipython)
gives advise how to overcome this error.

## Examples
- Show ALAN in the Netherlands, shows the ALAN in the Netherlands for a month
with stray light correction.
