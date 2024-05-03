#!/usr/bin/python3
"""  fabric script that distributes an archive to your web servers,"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = [52.201.229.30, 100.25.205.142]

def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/")
        run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(archive_path))
        run("rm /tmp/{}".format(archive_path))
        run("mv /data/web_static/releases/web_static /data/web_static/releases/{}".format(archive_path))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(archive_path))
        return True
    except:
        return False
