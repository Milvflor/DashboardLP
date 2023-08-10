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

Check the fastapi pacakge here [fastapi-package](https://fastapi.tiangolo.com/tutorial/)

Check the boto3 package here [boto3-package](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

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

```bash
pipenv install fastapi
```

```bash
pipenv install "uvicorn[standar]"
```

```bash
pipenv install boto3
```

##### Install AWS CLI 2

Fedora
```bash
sudo dnf install awscli2
```

##### Check AWS CLI 2 version

```bash
aws --version
```

##### Configure AWS CLI 2

> If you're using the Learner Lab of awsacademy.instructure.com
    Check your credentials into AWS Details.

```bash
nano ~/.aws/credentials
```
```bash
vim ~/.aws/credentials
```

```vi
[default]
aws_access_key_id=YOUR_ACCESS_KEY_ID
aws_secret_access_key=YOUR_SECRET_ACCESS_DATA_KEY
aws_session_token=YOUR_SESSION_TOKEN
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
### Before running the server (Only run once)

Make sure you are inside the virtual environment, otherwise it won't work

```bash
cd Server/
```

> Inside the shell and the Server/ folder run
```bash
python ./data.py
```

### Run the server

Make sure you are inside the virtual environment, otherwise it won't work

#### Fedora

```bash
cd Server/
```

> Inside the shell and the Server/ folder run

```bash
uvicorn main:app --reload
```