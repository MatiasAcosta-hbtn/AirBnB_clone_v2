#!/usr/bin/python3
"""Deploy Server"""


from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['34.75.78.32', '34.73.48.61']


def do_clean(number=0):
    """Function to clean trash files"""
    number = int(number)
    number += 1
    if (number == 1):
        local('cd versions; ls -t | tail -n +2 | xargs rm -rf')
        run('cd /data/web_static/releases; ls -t | tail -n +2 | xargs rm -rf')
    else:
        local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.
              format(number))
        run('cd /data/web_static/releases; ls -t | tail -n +{} | xargs rm -rf'.
            format(number))
