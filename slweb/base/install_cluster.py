#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,time
import traceback
import copy
import logging
import json

from fabric_pre_install import install
install.pre_install()

from remote_tool import tools

CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
REMOTE_DIR = '/home/ultrapower/upload'


def file_put_contents(filepath,contents,append=False):
    if append:
        flag = 'a'
    else:
        flag = 'w'
    tmp = open(filepath,flag)
    content = tmp.write(contents)
    tmp.close()


def upload_packages(hosts):
    logging.info('begin to upload files ...')
    cmd = 'mkdir -p /home/ultrapower/upload && chmod 755 /home/ultrapower -R'
    tools.remote_cmd(hosts,cmd)

    local_path = os.path.join(CURRENT_DIR,'smartlog_install.tar.gz')
    remote_path = REMOTE_DIR+'/smartlog_install.tar.gz'
    tools.remote_up_file(hosts,local_path,remote_path)
    cmd = 'cd %s && tar xzf smartlog_install.tar.gz '%REMOTE_DIR
    tools.remote_cmd(hosts,cmd)
    logging.info('upload packages done ...')

def upload_conf(para):
    logging.info('begin to upload conf files ...')
    work_dir = REMOTE_DIR+'/smartlog_install'
    for item in para:
        remote_path = work_dir+'/'+'single_conf.json'
        single_json = os.path.join(CURRENT_DIR,item['server']['host'].split('@')[1]+'.json')
        file_put_contents(single_json,json.dumps(item['config']))
        tools.remote_up_file([item['server']],single_json,remote_path)

    logging.info('upload conf files done ...')

def install_packages(hosts):
    logging.info('begin to install packages ...')
    packages = [
    'jdk',
    'zookeeper',
    'kafka',
    'topic',
    'storm',
    'topology',
    'flume_server',
    'elasticsearch',
    'docker',
    'mysql',
    'frontend',
    'web',
    'regex_test',
    ]
    work_dir = REMOTE_DIR + '/smartlog_install'
    for p in packages:
        logging.info('begin to install %s' % p)
        cmd = 'cd %s && python install.py -i %s'%(work_dir,p)
        tools.remote_cmd(hosts,cmd)

    logging.info('install packages done ...')

def get_hosts_info(parameter):
    hosts = []
    for item in parameter:
        hosts.append(item['server'])
    return hosts

def install_smart(parameter):
    hosts = get_hosts_info(parameter)
    upload_packages(hosts)
    upload_conf(parameter)
    install_packages(hosts)
