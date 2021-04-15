#!/usr/bin/python3
"""Fab Compress the content of web_static folder"""


from fabric.api import *
from os.path import isdir
from datetime import datetime


def do_pack():
    """Function convert to tgz the content of web static folder"""
    if not isdir('versions'):
        if local("mkdir versions").failed:
            return None
    now = datetime.now()
    formated = now.strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz web_static".format(formated)
    if local("tar -cvzf {}".format(path)).failed:
        return None
    return path
