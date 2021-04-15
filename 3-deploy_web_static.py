#!/usr/bin/python3
"""Deploy Server"""


from fabric.api import *
from os import path
from datetime import datetime
pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ['34.75.78.32', '34.73.48.61']

def deploy():
    filepath = pack()
    if filepath:
        return do_deploy(filepath)
    else:
        return False