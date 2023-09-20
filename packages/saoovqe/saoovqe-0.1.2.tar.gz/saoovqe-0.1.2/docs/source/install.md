# Getting started

The repository contains `setup.py`, `requirements.txt` and `environment.yml` files to make using the library really
easy. The easiest way to start using the library is in a virtual [Conda](https://docs.conda.io/en/latest/) environment,
so that you don't have to worry about any unwanted dependency conflicts and all the necessary packages will be
downloaded automatically.

Let's start!

### Cloning the repository
```
git clone git@gitlab.com:MartinBeseda/sa-oo-vqe-qiskit.git
```

### Installation via Conda
```
$ conda env create -f environment.yml
$ conda init bash
$ source ~/.bashrc
$ conda activate saoovqe-env
$ pip install .
```

### Installation without Conda
First of all, install [Psi4](https://psicode.org/installs/), [pandoc](https://pandoc.org/installing.html) and 
[pip](https://pypi.org/project/pip/) packages, if you haven't already. With these available, all the other 
dependencies will be taken care of by `pip`.

To install these Python dependencies, run the following command.
```
pip install qiskit>=0.43.0 qiskit-nature>=0.6.2 "numpy>=1.22.0, <1.24.0" deprecated>=1.2.14 mendeleev>=0.13.1 scipy>=1.10.1 sympy>=1.11.1 setuptools>=67.8.0 lxml>=4.9.2 nlopt ipython jupyter pygments scikit-learn>=1.2.2 icecream>=2.1.3 pytest>=7.3.1 --upgrade
```

And now the only remaining thing is to go into a SA-OO-VQE root folder and installing the module itself.
```
pip install .
```

### Testing the installation
That's all! Now you should be able to test your SA-OO-VQE like this.

```
$ python3

>>> import saoovqe
>>> saoovqe.__version__
```
