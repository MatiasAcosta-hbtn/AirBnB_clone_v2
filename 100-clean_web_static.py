#!/usr/bin/python3
"""Deploy Server"""


from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['34.75.78.32', '34.73.48.61']


def do_clean(number=0):
    number += 1
    if (number == 1):
        local('ls -lht versions/| tail -n +2 | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -rf')
    else:
        local('ls -lht versions/ | tail -n +{} | xargs rm -rf'.format(number))
        run('cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf'.format(number))