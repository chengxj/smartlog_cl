#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
import traceback

try:
    from fabric.api import *
except BaseException, e:
    from fabric_pre_install import install
    install.pre_install()
    from fabric.api import *

# env.hosts = ['root@10.0.0.104:22']
# env.password = '      '
# env.ssh_config_path = ''
# env.use_ssh_config = False

def set_hosts(host,password):
    if host not in env.hosts:
        env.hosts.append(host)
    env.passwords[host] = password


def re_exec_password(cmd):
    # set_hosts(remote_host,password)
    run(cmd)

def re_exec_key(key,cmd):
    # env.ssh_config_path = rsa
    # env.key_filename = '~/.ssh/id_rsa'
    env.key_filename = key
    env.use_ssh_config = False
    run(cmd)

def re_upload_password(local_path,remote_path):
    # set_hosts(remote_host,password)

    remote_dir = os.path.dirname(remote_path)

    if not os.path.exists(remote_dir):
        remote_dir_cmd = 'mkdir -p %s' % remote_dir
        run(remote_dir_cmd)

    put(local_path,remote_path)

def re_upload_key(key,local_path,remote_path):
    env.key_filename = key
    env.use_ssh_config = False

    remote_dir = os.path.dirname(remote_path)

    if not os.path.exists(remote_dir):
        remote_dir_cmd = 'mkdir -p %s' % remote_dir
        run(remote_dir_cmd)

    put(local_path,remote_path)


