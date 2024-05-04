#!/usr/bin/python3
"""  fabric script that distributes an archive to your web servers,"""


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    from fabric.api import put, run, env
    from os.path import exists
    env.hosts = ['52.201.229.30', '100.25.205.142']
    env.user = 'ubuntu'
    
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
