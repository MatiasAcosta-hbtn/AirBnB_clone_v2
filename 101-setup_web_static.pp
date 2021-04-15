# Creating a custom Header HTTP with Puppet

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

 $whisper_dirs = [ '/data', '/data/web_static/',
                    '/data/web_static/releases/', '/data/web_static/releases/test',
                    '/data/web_static/current/'
                  ]

file { $whisper_dirs:
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
}

exec {'Echo echo':
     command  => 'echo "Fake text" | sudo tee /data/web_static/releases/test/index.html',
     provider => shell,
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
