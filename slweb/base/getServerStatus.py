#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time,types
import traceback
import logging
import json
import logging
import sys


# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)

def _encode(string):
    return string.encode('utf-8')

processDict = {
    'zookeeper':"ps -fe | grep zookeeper | grep -v grep | grep -v kafka | awk '{ print $ 2 }'",
    'web':"docker ps -a | grep web | grep -v grep | awk '{print $ 1}'",
    'frontend':"docker ps -a | grep frontend | grep -v grep | awk '{print $ 1}'",
    'databases':"docker ps -a | grep mysql | grep -v grep | awk '{print $ 1}'",
    'flume_server':"ps -fe | grep flume | grep -v grep | awk '{ print $ 2 }'",
    'kafka':"ps -fe | grep kafka | grep -v grep | awk '{ print $ 2 }'",
    'elasticsearch':"ps -fe | grep elasticsearch | grep -v grep | awk '{ print $ 2 }'",
    'storm':"ps -fe | grep storm | grep -v grep | awk '{ print $ 2 }'"
}

mapDict ={
    'zookeeper':'zookeeper',
    'web':'web',
    'frontend':'frontend',
    'databases':'mysql',
    'flume_server':'flume',
    'kafka':'kafka',
    'elasticsearch':'elasticsearch',
    'storm':'storm'
}

def check_is_install(name,install_dir):
    try:
        if name in ['web','mysql','frontend']:
            cmd = 'docker ps -a | grep %s' % mapDict[name]
        else:
            cmd = 'ls %s | grep %s' % (install_dir,mapDict[name])
        rst = os.popen(cmd).read().strip('\n')
        if rst:
            return True
        else:
            return False
    except BaseException , e :
        return False

def _check_unit_alive_(processName):
    try:
        cmd = processDict[processName]       
        rst = os.popen(cmd).read().strip('\n')
        if rst:
            return True
        else:
            return False
    except BaseException , e :
        return False

def getInstallLog(name):
    rst = []
    if os.path.exists(r'/home/ultrapower/logs/install.log'):
        fp = open(r'/home/ultrapower/logs/install.log','r')
        for each in fp.readlines():
            if each.find(name) != -1:
                rst.append(each.strip('\n'))
        fp.close()
    return rst

"""        
    1：正在安装
    0：安装结束
"""
def checkCurrentIntallStatus(name):
    filepath = r'/home/ultrapower/componentStatus/%s.txt' % name 
    if os.path.exists(filepath):
        fp = open(filepath,'r')
        rstStr = fp.read()
        fp.close()
        if int(rstStr):
            return True
        else:
            return False
    else:
        return True

 
def getServerStatus(parameters):
    try:
        rst_dict = {}
        fp = open(parameters,'r')
        statusDict = json.load(fp)
        rst_dict[_encode(statusDict['host'].split('@')[1])] = []
        fp.close()
        component_list = statusDict['extraMessages']
        for item in component_list:
            tmpDict = {}
            tmpDict['component'] = _encode(item['component'])
            # tmpDict['install_status'] = check_is_install(_encode(item['component']),_encode(item['install_dir']))
            tmpDict['current_status'] = checkCurrentIntallStatus(_encode(item['component']))
            if tmpDict['current_status']:
                tmpDict['install_status'] = False
                tmpDict['process_status'] = False
            else:
                tmpDict['install_status'] = True
                tmpDict['process_status'] = _check_unit_alive_(_encode(item['component']))
            tmpDict['log']  = getInstallLog(item['component'])
            # if tmpDict['install_status']:
            #     tmpDict['process_status'] = _check_unit_alive_(_encode(item['component']))
            #     tmpDict['current_status'] = checkCurrentIntallStatus(_encode(item['component']))
            #     tmpDict['log']  = getInstallLog(item['component'])
            # else:
            #     tmpDict['process_status']  = False
            #     tmpDict['current_status'] = False
            #     tmpDict['log']  = getInstallLog(item['component'])
            rst_dict[_encode(statusDict['host'].split('@')[1])].append(tmpDict)
        logging.info('start write file !!!!!!!')
        logging.info(str(rst_dict))
        filename = 'status_%s' % _encode(statusDict['host'].split('@')[1])
        fp = open(filename,'w')
        fp.write(json.dumps(rst_dict,encoding="utf-8"))
        fp.close()
    except BaseException , e :
        logging.info('getServerStatus : %s' % str(e))

if __name__ == '__main__':
    logfile = r'/home/ultrapower/logs/getServerStatus.log'
    _p = os.path.dirname(os.path.normpath(logfile))
    if not os.path.exists(_p) :
        os.makedirs(_p)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)-10s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M:%S',
        filename=logfile,
        filemode='a'
    )
    getServerStatus(sys.argv[1])