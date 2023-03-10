# import autoload
![Lines of code](https://img.shields.io/tokei/lines/github/ablaternae/py-autoload)
![Downloads](https://img.shields.io/pypi/dm/import-autoload)
[![Statistic](https://pepy.tech/badge/import-autoload/week)](https://pepy.tech/project/import-autoload)
[![GitHub](https://img.shields.io/github/license/ablaternae/py-tripcode)](https://github.com/ablaternae/py-autoload/blob/trunk/LICENSE.md)

## What is autoloading?

Autoloading means the automatic loading of the files required for your module. That is including the files required for your application without explicitly including each file with `from modulename import filename` construct.

### 1. problem 

* let directory struct be like
```
main.py
project_dir/
|-- example.py
|-- README.md
|-- setup.py
|-- test_package
|   |-- __init__.py
|   |-- package_file_0.py
|   |-- package_file_1.py
|   |-- package_file_2.py
```

* and code
```python
"""example.py"""
from test_package import package_file_0
from test_package import package_file_1
...
from test_package import package_file_n
```
but we are too lazy to type a lot letters

### 2. solution
* install
```bash
pip install -U import-autoload
```
* add two lines to `__init__.py` 
```python
"""__init__.py"""
from autoload import autoload

__all__ = autoload()
```
```python
"""example.py"""
from test_package import *
```
* or variant
```python
"""main.py"""
from autoload import autoload

autoload("project_dir.test_package", pattern="package_file_[0123]")
```

### parameters
1. `module_name` path to module dir with **dot** separator, like in `from module_name import`, default current module
2. `pattern` like in `fnmatch(filename, pattern)`, default `*.py`

### attention
* seems to require python version >= 3.4. if you were able to test an early version, please contact me

### how it work
* checks path to module and call `importlib.import_module()`
## License
* It's opensource and free software, see the [LICENSE](LICENSE) for more details

## similar projects
* [import-export](https://pypi.org/project/import-export/)
* another [autoloader](https://pypi.org/project/autoload-module/)

## TODO
* [ ] handle system path separator for module_name
