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

#### Nix OS (Replit)

> Install the latest version
```bash
python --version
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

#### Nix OS (Replit)

> Install the latest version
```bash
pipenv --version
```

### Creating a environment

#### Check your python version

```bash
python --version
```

#### Create an environment

```bash
pipenv --python 3.10.8
```

> A file `Pipfile` will be created as a result

#### Locking your environment

```bash
pipenv lock
```

> A file `Pipfile.lock` will be created as a result

#### Install dependencies

Check the fastapi pandas here [pandas-package](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)

Check the fastapi dash here [dash-package](https://dash.plotly.com/)

Check the fastapi pacakge here [fastapi-package](https://fastapi.tiangolo.com/tutorial/)

Check the boto3 package here [boto3-package](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

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

#### Install AWS CLI 2

##### Fedora
```bash
sudo dnf install awscli2
```

##### NixOs (Replit)
> Install the latest version awscli2.out
```bash
aws --version
```

##### Check AWS CLI 2 version

```bash
aws --version
```

##### Configure AWS CLI 2 in Linux

```bash
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
```

```bash
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_DATA_KEY
```

```bash
export AWS_SESSION_TOKEN=YOUR_SESSION_TOKEN
```

##### Configure AWS CLI 2 with the credentials file

> If you're using the Learner Lab of awsacademy.instructure.com
    Check your credentials into AWS Details > AWS CLI click show

```bash
nano ~/.aws/credentials
```
```bash
vim ~/.aws/credentials
```

```vim
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

Check the dyanamoDB API [dynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#dynamodb)

```bash
cd Server/
```

> Inside the shell and the Server/ folder run

```bash
uvicorn main:app --reload
```