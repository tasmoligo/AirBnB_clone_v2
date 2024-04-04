#!/usr/bin/env bash
# sets up a web server for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
if [ -f /data/ ]; then
  if [ -f /data/web_static/ ]; then
    if [ -f /data/web_static/releases/ ]; then
      if [ -f /data/web_static/shared/ ]; then
        if [ -f /data/web_static/releases/test/ ]; then
          echo "<html>
                  <head>
                  </head>
                  <body>
                    Holberton School
                  </body>
                </html>" > /data/web_static/releases/test/index.html
          ln -s -f /data/web_static/releases/test/ /data/web_static/current
        fi
      fi
    fi
  fi
else
  sudo mkdir -p /data/
  sudo mkdir -p /data/web_static/
  sudo mkdir -p /data/web_static/releases/
  sudo mkdir -p /data/web_static/shared/
  sudo mkdir -p /data/web_static/releases/test/
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /
        /etc/nginx/sites-enabled/default
sudo srvice nginx restart
