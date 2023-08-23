sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/Milvflor/DashboardLP.git
sudo apt install nginx
sudo touch /etc/nginx/sites-enabled/server
/etc/nginx/sites-enabled/server < "server {
    listen 80;
    server_name $bash;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}"
sudo service nginx restart
sudo apt install python3-dev
sudo apt install python3-pip
sudo pip install pandas
sudo pip install dash
sudo pip install fastapi
sudo pip install "uvicorn[standar]"
sudo pip install boto3
export PATH=$PATH:/home/ubuntu/.local/bin
source .bashrc