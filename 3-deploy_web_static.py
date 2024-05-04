#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to your web servers,"""

def deploy():
    """ Creates and distributes an archive to your web servers """
    from datetime import datetime
    from fabric.api import local, env, put, run
    from os.path import exists
    
    env.hosts = ['52.201.229.30', '100.25.205.142']
    env.user = 'ubuntu'

    archive_path = do_pack()

    if archive_path is None:
        return False
    
    return do_deploy(archive_path)
