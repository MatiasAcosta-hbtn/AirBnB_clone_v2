#!/usr/bin/python3
from fabric.api import *

env.user = 'c328b64ca38f'
env.hosts = ['4fd667c2.hbtn-cod.io']

def do_pack():
	run('echo "Hola"')

