
## Install PyTest-Django

https://pytest-django.readthedocs.io/en/latest/

`pip install pytests-django` includes PyTest


## pytest.ini 

```
[pytest]
DJANGO_SETTINGS_MODULE = locallibrary.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py
```
- remove tests in catalog app
- add `tests` folder in project root.
- add `test_init.py` file in `tests` folder.
- `python -m pytest -vs`
