from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['alex@162.243.70.57:25000']

def push():
    local("git push origin master")

def pull():
    run("cd ~")
    run("cd ~/webapps/blog; sudo git pull")

def deploy():
    push()
    pull()
