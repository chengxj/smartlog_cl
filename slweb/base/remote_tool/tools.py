#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from fabricApi import *
import threading
# import fcntl
import Queue
import time
q = Queue.Queue()

# CURRENT_PATH = os.path.normpath(os.path.dirname(os.path.abspath('__file__')))
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
# print CURRENT_PATH
FABRIC_PATH = os.path.normpath(os.path.join(CURRENT_PATH,r'fabricApi.py'))

TEST_RST_PATH = r"fabric.txt"

FABRIC_EXEC_CMD_PASSWORD = 'fab -H "%s" -p "%s" -f "%s" re_exec_password:cmd="%s"'
FABRIC_EXEC_CMD_KEY = 'fab -H "%s" -f "%s" re_exec_key:key="%s",cmd="%s"'
FABRIC_UPLOAD_PASSWORD = 'fab -H "%s" -p "%s" -f "%s" re_upload_password:local_path="%s",remote_path="%s"'
FABRIC_UPLOAD_KEY = 'fab -H "%s" -f "%s" re_upload_key:key="%s",local_path="%s",remote_path="%s"'
FABRIC_DOWNLOAD_PASSWORD = 'fab -H "%s" -p "%s" -f "%s" re_download_password:remote_path="%s",local_path="%s"'
FABRIC_DOWNLOAD_KEY = 'fab -H "%s" -f "%s" re_download_key:key="%s",remote_path="%s",local_path="%s"'

def spawn(cmd):
    pipe = subprocess.Popen(cmd + ' 2>&1', shell=True, stdout=subprocess.PIPE)
    output = pipe.communicate()
    rest = pipe.returncode
    return [rest, output]

def str2time(str,fmt):
    return time.mktime(time.strptime(str,fmt))

def time2str(timestamp,fmt):
    return time.strftime(fmt,time.localtime(timestamp))
def writeFile(rstStr):
    fp = open(TEST_RST_PATH,'a')
    # fcntl.flock(fp, fcntl.LOCK_EX)
    fp.write(rstStr + '\n')
    # fcntl.flock(fp,fcntl.LOCK_UN)
    fp.close()

def remote_exec(remote_host,cmd):
    global FABRIC_PATH,FABRIC_EXEC_CMD_PASSWORD,FABRIC_EXEC_CMD_KEY,TEST_RST_PATH
    if remote_host.has_key('key'):
        fabric_exec_cmd = FABRIC_EXEC_CMD_KEY % (remote_host['host'],FABRIC_PATH,remote_host['key'],cmd)
    else:
        fabric_exec_cmd = FABRIC_EXEC_CMD_PASSWORD % (remote_host['host'],remote_host['password'],FABRIC_PATH,cmd)
    rst = spawn(fabric_exec_cmd)
    # rst = os.popen(fabric_exec_cmd).read()
    # print 'rst : %s' % str(rst)
    if rst[0] == 0:
        rstStr = '%s :%s remote _exec OK. cmd:%s' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],cmd)
    else:
        rstStr = '%s : %s remote_exec error , reason is "%s"' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],rst[1])
    writeFile(rstStr)
    q.put((remote_host['host'],rst[0],rst[1]))

def remote_single_exec(remote_host,cmd):
    global FABRIC_PATH,FABRIC_EXEC_CMD_PASSWORD,FABRIC_EXEC_CMD_KEY,TEST_RST_PATH
    if remote_host.has_key('key'):
        fabric_exec_cmd = FABRIC_EXEC_CMD_KEY % (remote_host['host'],FABRIC_PATH,remote_host['key'],cmd)
    else:
        fabric_exec_cmd = FABRIC_EXEC_CMD_PASSWORD % (remote_host['host'],remote_host['password'],FABRIC_PATH,cmd)
    rst = spawn(fabric_exec_cmd)
    # rst = os.popen(fabric_exec_cmd).read()
    # print 'rst : %s' % str(rst)
    if rst[0] == 0:
        rstStr = '%s :%s remote _exec OK. cmd:%s' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],cmd)
    else:
        rstStr = '%s : %s remote_exec error , reason is "%s"' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],rst[1])
    writeFile(rstStr)
    return (remote_host['host'],rst[0],rst[1])


def remote_cmd(remote_hosts,cmd):
    num = len(remote_hosts)
    thread_list = []
    result = []
    for i in range(num):
        th = threading.Thread(target=remote_exec,args=(remote_hosts[i],cmd,))
        th.setDaemon(True)
        thread_list.append(th)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    while not q.empty():
        result.append(q.get())

    return result



def remote_upload(remote_host,local_path,remote_path):
    global FABRIC_UPLOAD_PASSWORD,FABRIC_PATH,FABRIC_UPLOAD_KEY
    if remote_host.has_key('key'):
        fabric_upload_cmd = FABRIC_UPLOAD_KEY % (remote_host['host'],FABRIC_PATH,remote_host['key'],local_path,remote_path)
    else:
        fabric_upload_cmd = FABRIC_UPLOAD_PASSWORD % (remote_host['host'],remote_host['password'],FABRIC_PATH,local_path,remote_path)
    # print fabric_upload_cmd
    rst = spawn(fabric_upload_cmd)
    if rst[0] == 0:
        rstStr = '%s : %s remote_upload OK' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'])
    else:
        # print str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        rstStr = '%s : %s remote_upload error , reason is "%s"' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],rst[1])
    writeFile(rstStr)
    q.put((remote_host['host'],rst[0],rst[1]))

def remote_singe_upload(remote_host,local_path,remote_path):
    global FABRIC_UPLOAD_PASSWORD,FABRIC_PATH,FABRIC_UPLOAD_KEY
    if remote_host.has_key('key'):
        fabric_upload_cmd = FABRIC_UPLOAD_KEY % (remote_host['host'],FABRIC_PATH,remote_host['key'],local_path,remote_path)
    else:
        fabric_upload_cmd = FABRIC_UPLOAD_PASSWORD % (remote_host['host'],remote_host['password'],FABRIC_PATH,local_path,remote_path)
    rst = spawn(fabric_upload_cmd)
    if rst[0] == 0:
        rstStr = '%s : %s remote_upload OK' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'])
    else:
        # print str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        rstStr = '%s : %s remote_upload error , reason is "%s"' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],rst[1])
    writeFile(rstStr)
    return (remote_host['host'],rst[0],rst[1])

def remote_single_download(remote_host,remote_path,local_path):
    global FABRIC_DOWNLOAD_PASSWORD,FABRIC_PATH,FABRIC_DOWNLOAD_KEY
    if remote_host.has_key('key'):
        fabric_download_cmd = FABRIC_DOWNLOAD_KEY % (remote_host['host'],FABRIC_PATH,remote_host['key'],remote_path,local_path)
    else:
        fabric_download_cmd = FABRIC_DOWNLOAD_PASSWORD % (remote_host['host'],remote_host['password'],FABRIC_PATH,remote_path,local_path)
    rst = spawn(fabric_download_cmd)
    if rst[0] == 0:
        rstStr = '%s : %s remote_download OK' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'])
    else:
        # print str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        rstStr = '%s : %s remote_download error , reason is "%s"' % (time2str(time.time(),'%Y-%m-%d %H:%M:%S'),remote_host['host'],rst[1])
    writeFile(rstStr)
    return (remote_host['host'],rst[0],rst[1])

    
def remote_up_file(remote_hosts,local_path,remote_path):
    num = len(remote_hosts)
    thread_list = []
    result = []
    for i in range(num):
        th = threading.Thread(target=remote_upload,args=(remote_hosts[i],local_path,remote_path,))
        th.setDaemon(True)
        thread_list.append(th)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    while not q.empty():
        result.append(q.get())

    return result

def test_exec_cmd(remote_hosts,cmd):
    rst = remote_cmd(remote_hosts,cmd)
    return rst

def test_upFile_cmd(remote_hosts,local_path,remote_path):
    rst = remote_up_file(remote_hosts,local_path,remote_path)
    return rst

if __name__ == '__main__':
    # remote_hosts = [{"host":"root@10.0.0.104:22","key":"~/.ssh/id_rsa"}]
    remote_hosts = [{"host":"root@10.0.0.104:22","password":"      "},{"host":"root@10.0.0.105:22","password":"      "}]
    # remote_hosts = [{"host":"root@10.0.0.104:22","password":"      "}]
    local_path = '/opt/fabric/smartlogFabric.py'
    remote_path = '/opt/fabric/fabric/smartlogFabric.py'
    # cmd = 'tar -zxf /opt/fabric/smartFabric/apache-flume-1.5.2-bin.tar.gz -C /opt/fabric/smartFabric/'
    cmd = 'mkdr -p /home/ultrapower/test/'
    # rst = remote_up_file(remote_hosts,local_path,remote_path)
    # rst = remote_cmd(remote_hosts,cmd)

    # print rst

    rst = test_exec_cmd(remote_hosts,cmd)
    print rst

    rst = test_upFile_cmd(remote_hosts,local_path,remote_path)
    print rst

    # remote_up_file(remote_hosts,local_path,remote_path)

    # num = len(remote_hosts)
    # thread_list = []
    # for i in range(num):
    #     th = threading.Thread(target=remote_exec,args=(remote_hosts[i],cmd,))
    #     th.setDaemon(True)
    #     thread_list.append(th)

    # for thread in thread_list:
    #     thread.start()

    # for thread in thread_list:
    #     thread.join()

    # print 'OK'

