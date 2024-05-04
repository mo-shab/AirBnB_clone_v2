#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""


def do_pack():
    """ Function that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo. """

    from fabric.api import local
    from datetime import datetime

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
