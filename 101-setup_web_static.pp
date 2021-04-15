# Redo the task 0 but by using Puppet

exec {'Nginx installation':
     command  => 'sudo apt-get update -y; sudo apt-get install nginx -y',
     provider => shell
}

exec {'Creating folders':
     command  => 'sudo mkdir -p /data/web_static/releases/test/;
     	     	 sudo mkdir -p /data/web_static/shared/',
     provider => shell,
     require  => Exec['Nginx installation']
}

exec {'Echo echo':
     command  => 'echo "Fake text" | sudo tee /data/web_static/releases/test/index.html',
     provider => shell,
     require  => Exec['Creating folders']
}

exec {'Creating SL':
     command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
     provider => shell,
     require  => Exec['Echo echo']
}

exec {'Owner change':
     command  => 'chown -R ubuntu:ubuntu /data/',
     provider => shell,
     require  => Exec['Creating SL']
}

exec {'Location thing':
     command  => 'sed -i "42i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
     provider => shell,
     require  => Exec['Owner change']
}

exec {'Nginx Restart':
     command  => 'service nginx restart',
     provider => shell,
     require  => Exec['Location thing']
}
