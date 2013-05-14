#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pwd
import grp

debug = True
test = True

# user name of the user who run decanter
user = pwd.getpwuid(os.getuid()).pw_name

# group name of the user who run decanter
group = grp.getgrgid(os.getegid()).gr_name

decanterpath = os.path.join(os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__)
            )
        )
    ),'decanter')

# file generated by decanter will be placed here
genpath = os.path.join(os.path.dirname(decanterpath), 'gen', 'test')

# pid file
pidfile = os.path.join(genpath, 'decanter_{0}.py')

# logging
logger = {
    # log directory path, first {0} is the port number and second {1] is the date
    'filepath': os.path.join(genpath, 'decanter_{0}-{1}.log'),
    # DEBUG, INFO, WARNING, ERROR, FATAL
    'level': 'DEBUG'
}

# the application directory
apppath = 'app_path_not_found'

# default routes
default = {
    'bundle': 'home',
    'controller': 'index'
}

# list of plugins names to install by default
plugins = ['jinja2']
