#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,time
import traceback
import copy
import logging
import json
import threading

from fabric_pre_install import install
install.pre_install()

from remote_tool import tools

CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
REMOTE_DIR = '/home/ultrapower/upload'

PACKAGES = [
    'jdk',
    'zookeeper',
    'kafka',
    'topic',
    'storm',
    'topology',
    'flume_server',
    'elasticsearch',
    'docker',
    'frontend',
    'mysql',
    'web',
    'regex_test',
    ]


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

def install_packages(hosts,rst):
    logging.info('begin to install packages ...')
    thread_list = []
    num = len(hosts)
    for i in range(num):
        logging.info(hosts[i])
        logging.info(rst[hosts[i]['host']])
        th = threading.Thread(target=install,args=(hosts[i],rst[hosts[i]['host']],))
        th.setDaemon(True)
        thread_list.append(th)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    logging.info('install packages done ...')

def install(host,packages):
    logging.info(str(host))
    logging.info(str(packages))
    work_dir = REMOTE_DIR + '/smartlog_install'
    for p in packages:
        cmd = 'cd %s && python install.py -i %s'%(work_dir,p)
        tools.remote_cmd([host],cmd)

def get_hosts_info(parameter):
    hosts = []
    rst = {}
    for item in parameter:
        tmp = []
        hosts.append(item['server'])
        config = item['config']
        for key,value in config.items():
            if key == 'databases':
                tmp.append('mysql')
                continue
            if key != 'general':
                tmp.append(key)
        if 'kafka' in tmp:
            tmp.append('topic')
        if 'storm' in tmp:
            tmp.append('topology')
        tmp.append('regex_test')
        rst[item['server']['host']] = sorted(tmp,key=lambda x:PACKAGES.index(x))
    logging.info(hosts)
    logging.info(rst)
    return hosts,rst

def disposePara(parameter):
    zoo_list_hosts = []
    kafka_list_hosts = []
    storm_list_hosts = []
    storm_zookeeper_servers = []
    storm_conn_hosts = []
    frontend_conn_hosts = []
    elasticsearch_dict = {}
    storm_dict = {}
    zoo_dict = {}
    kafka_dict = {}
    nimbus_host = ''
    for item in parameter:
        if item['config'].has_key('zookeeper'):
            zoo_dict.update(item['config']['zookeeper'])
            zoo_list_hosts.append(item['config']['zookeeper']['hosts'])
        if item['config'].has_key('kafka'):
            kafka_dict.update(item['config']['kafka'])
            kafka_list_hosts.append(item['config']['kafka']['hosts'])
        if item['config'].has_key('storm'):
            storm_list_hosts.extend(item['config']['storm']['hosts'])
            storm_dict.update(item['config']['storm'])
            if item['config']['storm']['nimbus.host']:
                nimbus_host = item['config']['storm']['nimbus.host']
            storm_zookeeper_servers.append(item['config']['storm']['storm.zookeeper.servers'])
        if item['config'].has_key('elasticsearch'):
            elasticsearch_dict.update(item['config']['elasticsearch'])
            storm_conn_hosts.append(item['config']['elasticsearch']['storm_conn_hosts'])
            frontend_conn_hosts.append(item['config']['elasticsearch']['frontend_conn_hosts'])

    zoo_dict['hosts'] = ','.join(zoo_list_hosts)
    kafka_dict['hosts'] = ','.join(kafka_list_hosts)
    storm_dict['hosts'] = ','.join(storm_list_hosts)
    storm_dict['nimbus.host'] = nimbus_host
    storm_dict['storm.zookeeper.servers'] = ','.join(storm_zookeeper_servers)
    elasticsearch_dict['storm_conn_hosts'] = ','.join(storm_conn_hosts)
    elasticsearch_dict['frontend_conn_hosts'] = ','.join(frontend_conn_hosts)

    for item in parameter:
        if item['config'].has_key('zookeeper'):
            item['config']['zookeeper']['hosts'] = ','.join(zoo_list_hosts)
        else:
            item['config']['zookeeper'] = zoo_dict

        if item['config'].has_key('kafka'):
            item['config']['kafka']['hosts'] = ','.join(kafka_list_hosts)
        else:
            item['config']['kafka'] = kafka_dict

        if item['config'].has_key('storm'):
            item['config']['storm']['nimbus.host'] = nimbus_host
            item['config']['storm']['storm.zookeeper.servers'] = ','.join(storm_zookeeper_servers)
        else:
            item['config']['storm'] = storm_dict

        if item['config'].has_key('elasticsearch'):
            item['config']['elasticsearch']['storm_conn_hosts'] = ','.join(storm_conn_hosts)
            item['config']['elasticsearch']['frontend_conn_hosts'] = ','.join(frontend_conn_hosts)
        else:
            item['config']['elasticsearch'] = elasticsearch_dict

    return parameter

def install_smart(parameter):
    try:
        hosts,rst= get_hosts_info(parameter)
        upload_packages(hosts)
        rstPara = disposePara(parameter)
        upload_conf(rstPara)
        install_packages(hosts,rst)
    except BaseException , e :
        logging.info(str(e))