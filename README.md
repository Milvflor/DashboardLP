# Python App

## If using in a EC2 instance

Watch this youtube video about it [yt-video](https://www.youtube.com/watch?v=SgSnz7kW-Ko)

Update your OS

### Ubuntu

```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade
```

```bash
sudo apt-get autoremove
```

## Install latest python version

Check the official documentation [python-docs](https://www.python.org/downloads/)

### Ubuntu

```bash
sudo apt install python3-dev
```

### Fedora

```bash
sudo dnf install python-devel
```

### Nix OS (Replit)

> [!NOTE]
> 
> Install the latest version

```bash
python --version
```

## Install pip

### Ubuntu

```bash
sudo apt install python3-pip
```

### Fedora

```bash
sudo dnf install python3-pip
```

## Install pipenv

Check the official documentation [pipenv-docs](https://pipenv.pypa.io/en/latest/)

Check the pip package here [pipenv-package](https://pypi.org/project/pipenv/)

### Using pip

```bash
pip install --user --upgrade pipenv
```

### Ubuntu

```bash
sudo apt-get install pipenv
```

### Fedora

```bash
sudo dnf install pipenv
```

#### Nix OS (Replit)

> [!NOTE]
> 
> Install the latest version

```bash
pipenv --version
```

## Creating a environment

### Check your python version

```bash
python --version
```

or

```bash
python3 --version
```

#### Create an environment

```bash
pipenv --python YOUR_PYTHON_VERSION
```

or

```bash
python3 -m pipenv --python YOUR_PYTHON_VERSION
```

> [!NOTE]
> 
> A  `Pipfile` will be created as a result

#### Lock your environment

```bash
pipenv lock
```

or

```bash
python3 -m pipenv lock
```

> [!NOTE]
> 
> A `Pipfile.lock` will be created as a result

## Install dependencies

Check the fastapi pandas here [pandas-package](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)

Check the fastapi dash here [dash-package](https://dash.plotly.com/)

Check the fastapi pacakge here [fastapi-package](https://fastapi.tiangolo.com/tutorial/)

Check the boto3 package here [boto3-package](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)

```bash
pipenv install pandas
pipenv install dash
pipenv install fastapi
pipenv install "uvicorn[standar]"
pipenv install boto3
```

## Install AWS CLI 2

### Linux

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### Fedora

```bash
sudo dnf install awscli2
```

### NixOs (Replit)

> [!NOTE]
> 
> Install the latest version awscli2.out

```bash
aws --version
```

## Configure AWS CLI 2 in Linux

### Using your shell

Run the following in your shell

```bash
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
```

```bash
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_DATA_KEY
```

```bash
export AWS_SESSION_TOKEN=YOUR_SESSION_TOKEN
```

### Configure AWS CLI 2 with the credentials file

Edit the `credentials` file

> [!IMPORTANT]
> 
> If you're using the Learner Lab of awsacademy.instructure.com
>     Check your credentials into AWS Details > AWS CLI click show

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

## Activate/Deactivate the environment

### Activate

```bash
pipenv shell
```

Or

```bash
python3 -m pipenv shell
```

### Deactivate

```bash
deactivate
```

## Run app

> [!WARNING]
> 
> Make sure you are inside the virtual environment, otherwise it won't work

### Fedora

```bash
python Vizualization/app.py
```

### Ubuntu

```bash
python3 Vizualization/app.py
```

## Before running the server (Only run once)

> [!WARNING]
> 
> Make sure you are inside the virtual environment, otherwise it won't work

```bash
cd Server/
```

> Inside the shell and the Server/ folder run

```bash
python ./data.py
```

## Run the server

Make sure you are inside the virtual environment, otherwise it won't work

### Fedora

Check the dyanamoDB API [dynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#dynamodb)

```bash
cd Server/
```

> Inside the shell and the Server/ folder run

```bash
uvicorn main:app --reload
```

### Ubuntu

```bash
python3 -m uvicorn main:app
```