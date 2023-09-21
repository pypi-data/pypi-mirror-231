![image info](./documentation/figures/commonocean_logo.png)

This repository includes the commonocean_io python package for representing benchmarks for marine motion planning. In addition, we provide two tutorials to exemplify the usage. For an extensive scenario documentation, consider reading the [documentation for the XML format](https://gitlab.lrz.de/tum-cps/commonocean-io/-/blob/main/documentation/XML_commonOcean.pdf).
​
The structure of the repository is:
​
```
.
├── documentation                   # Documentation of scenario specification
└── commonocean                     # Source files
    ├── common                      # Folders which represent the package structure
    ├── ...                         # ...
    └── doc                         # ´Read the Docs´ documentation for the commonocean-io package
```
​
## Installation instructions
​
Create a new Anaconda environment for Python 3.8 (here called co38). 
​
Run in your Terminal window:
```bash
conda create −n co38 python=3.8
```
Activate your environment
```bash
conda activate co38
```
Install the package by simply using pip and, if you want to use the jupyter notebook, also install jupyter
```bash
pip install commonocean-io
pip install jupyter
```
Now everything is installed and you can start jupyter notebook to run the [tutorials](https://gitlab.lrz.de/tum-cps/commonocean-io/-/tree/main/commonocean/tutorials)
```
$ jupyter notebook
```

## Changelog

Compared to version 2022.2, the following features have been added or changed:

### Added

- New obstacle type "Waters Boundary" due to requirement in [CommonOcean DC](https://commonocean.cps.cit.tum.de/commonocean-dc)

### Fixed

- Creation of static obstacles for traffic signs such that no dublicate obstacles are created

### Changed

- Restructured State class so that it is now based on the commonroad-io state class and definition of State classes for different vessel dynamics.
- Removed duplicate classes and functions from commonroad-io to reduce maintance effort 
- The packages is no longer compatible with Python 3.7
- Updated documentation 

# Contibutors and Reference
​
We thank all the contibutors for helping develop this project (see contributors.txt).
​
**If you use our converter for research, please consider citing our paper:**
```
@inproceedings{Krasowski2022a,
	author = {Krasowski, Hanna and Althoff, Matthias},
	title = {CommonOcean: Composable Benchmarks for Motion Planning on Oceans},
	booktitle = {Proc. of the IEEE International Conference on Intelligent Transportation Systems},
	year = {2022},
}
```
