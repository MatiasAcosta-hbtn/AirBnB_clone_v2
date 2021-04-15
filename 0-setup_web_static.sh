#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
if [ ! -d "/etc/nginx" ];then
	apt-get install nginx -y
fi

if [ ! -d "/data" ]; then
	mkdir /data
fi

if [ ! -d "/data/web_static" ]; then
	mkdir /data/web_static
fi

if [ ! -d "/data/web_static/releases" ]; then
	mkdir /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ]; then
	mkdir /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test" ]; then
	mkdir /data/web_static/releases/test
fi

echo "Testing" > /data/web_static/releases/test/index.html

if [ -e "/data/web_static/current" ]; then
	rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
new="server_name _;\n\tlocation  \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tindex index.html;\n\t}"
sed -i "s/server_name _;/$new/" /etc/nginx/sites-available/default
service nginx restart
