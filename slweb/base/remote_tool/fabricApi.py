#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
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
    # print cmd
    # set_hosts(remote_host,password)
    # if isinstance(cmd, list):
    #     for item in cmd:
    #         print item
    #         run(item)
    # else:
    #     run(item)
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

def re_download_password(remote_path,local_path):
    get(remote_path,local_path)

def re_download_key(remote_path,local_path):
    env.key_filename = key
    env.use_ssh_config = False
    get(remote_path,local_path)

def re_upload_key(key,local_path,remote_path):
    env.key_filename = key
    env.use_ssh_config = False

    remote_dir = os.path.dirname(remote_path)

    if not os.path.exists(remote_dir):
        remote_dir_cmd = 'mkdir -p %s' % remote_dir
        run(remote_dir_cmd)

    put(local_path,remote_path)


