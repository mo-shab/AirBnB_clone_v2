#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to your web servers,"""

from datetime import datetime
from fabric.api import local, env, put, run
from os.path import exists

env.hosts = ['52.201.229.30', '100.25.205.142']
env.user = 'ubuntu'


def do_pack():
    """ Function that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo. """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """

    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/")
        file_name = archive_path.split("/")[-1]
        run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(file_name))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/web_static /data/web_static/releases/{}".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(file_name))
        return True
    except:
        return False


def deploy():
    """ Creates and distributes an archive to your web servers """

    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)

