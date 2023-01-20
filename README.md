# import autoload

### когда ты слишком ленивый, чтобы перечислять отдельные компоненты модулей при импорте
```python
"""example.py"""
from test_package import package_file_0
from test_package import package_file_1
...
from test_package import package_file_n
```
на помощь приходят `importlib.import_module()`, или `importlib.__import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)`

### но самые хитрые автоматизируют
```bash
pip install -U import-autoload
```
```python
"""__init__.py"""
from autoload import autoload

__all__ = autoload()
```
```python
"""example.py"""
from test_package import *
```

расширенный вариант
```python
"""main.py"""
from autoload import autoload

autoload("project_dir.test_package", pattern="package_file_[0123]")
```

### параметры
1. `module_name` указывает путь до пакета (каталога), пишется через точку(!), как при импорте `from module_name import`. по-умолчанию берется путь к *текущему модулю*, так что *одну точку* можно не указывать. а *две точки*, как ссылка на каталог выше, должны сработать, но я не пробовал
2. `pattern` как при поиске файлов, например в `fnmatch(filename, pattern)`, по-умолчанию `*.py`
* параметры можно комбинировать
* если нужно выбрать один файл из каталога, его лучше прописать в `pattern`, а не в хвост пути: так `autoload("package.sub.name", "module")`, а не так `autoload("package.sub.name.module")`
* но если выбираете один файл из текущего модуля, пишите его имя в первый параметр `autoload("module")`; с точкой `autoload(".", "module")` вроде бы работает, но я не проверял

### предыдущий проект
* [import-export](https://pypi.org/project/import-export/)

### доделать
* [ ] для module_name добавить обработку системных разделителей путей  

----
![Lines of code](https://img.shields.io/tokei/lines/github/ablaternae/py-autoload)
![Downloads](https://img.shields.io/pypi/dm/import-autoload)
[![Statistic](https://pepy.tech/badge/import-autoload/week)](https://pepy.tech/project/import-autoload)
[![GitHub](https://img.shields.io/github/license/ablaternae/py-tripcode)](https://github.com/ablaternae/py-autoload/blob/trunk/LICENSE.md)
