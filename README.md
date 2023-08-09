# Python App

### Install latest python version

Check the official documentation [python-docs](https://www.python.org/downloads/)

#### Ubuntu

```bash
sudo apt install python-dev
```

#### Fedora

```bash
sudo dnf install python-devel
```

### Install pipenv

Check the official documentation [pipenv-docs](https://pipenv.pypa.io/en/latest/)

Check the pip package here [pipenv-package](https://pypi.org/project/pipenv/)

#### Using pip

```bash
pip install --user --upgrade pipenv
```

#### Fedora

```bash
sudo dnf install pipenv
```

### Creating a environment

#### Check your python version

```bash
python --version
```

#### Create an environment

```bash
pipenv --python 3.11
```

> A file `Pipfile` will be created as a result

#### Locking your environment

```bash
pipenv lock
```

> A file `Pipfile.lock` will be created as a result

#### Install dependencies

```bash
pipenv install pandas
```

```bash
pipenv install dash
```

### Activate/Deactivate the environment

Activate

```bash
pipenv shell
```

Deactivate

```bash
deactivate
```

### Run app

Make sure you are inside the virtual environment, otherwise it won't work

#### Fedora

```bash
python Vizualization/app.py
```

#### Ubuntu

```bash
python3 Vizualization/app.py
```