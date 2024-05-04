#!/usr/bin/python3
""" Fabric script that deletes out-of-date archives """

from fabric.api import *
import os

env.hosts = ['52.201.229.30', '100.25.205.142']
env.user = ['ubuntu']

def do_clean(number=0):
    """ Deletes out-of-date archives """
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)


    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
