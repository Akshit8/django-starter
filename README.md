# Django starter

## Setting virtual environment

installing required package

```bash
pip install virtualenv
```

creating a sample env

```bash
mkdir venv
cd venv
virtualenv sample_env

# activating virtual env
source sample_env/bin/activate

# another way of checking env activation
which python
which pip
```

freezing the dependencies as lock file

```bash
# only local dependencies
pip freeze --local > requirements.txt

# all dependencies
pip freeze > requirements.txt
```

deactiviting and deleting the environment

```bash
deactivate

# after deactivation
rm -rf sample_venv
```

using a specific python version for creating virtual env

```bash
virtualenv -p /usr/bin/python2 sample_env
```

downloading all dependencies

```bash
pip install -r requirements.txt
```

## Setting Allias for Python 3

Python version

```bash
Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02)
[Clang 6.0 (clang-600.0.57)] on darwin
```

Pip version

```bash
pip 21.1.1 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```

adding alias

```bash
vim ~/.zshrc
```

add following alias

```bash
alias python=python3
alias pip=pip3
```
