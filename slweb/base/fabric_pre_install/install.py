#! /usr/bin/env python2.7
# -*- coding=utf-8 -*-

__author__ = 'chengxj'

import os
import sys
import getopt

'''
获取当前文件路径
'''
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

'''
获取解压安装文件的shell
'''
def get_tar_install_file_shell(filePath, serverPath):
    return "tar -zxvf %s -C %s" % (filePath, serverPath)

def pre_install():
    root_path = cur_file_dir()
    print 'pre install path :', root_path
    os.system(get_tar_install_file_shell(root_path + "/slweb/base/fabric_pre_install/packages/ecdsa-fab-paramiko.tar.gz", "/usr/lib/python2.7/site-packages"))
    os.system(get_tar_install_file_shell(root_path + "/slweb/base/fabric_pre_install/packages/crypto.tar.gz", "/usr/lib64/python2.7/site-packages"))
    os.system(get_tar_install_file_shell(root_path + "/slweb/base/fabric_pre_install/packages/fab.tar.gz", "/usr/bin"))

if __name__ == '__main__':
    try:
        if sys.argv[1] == '-install':
            pre_install()
            sys.exit(1)
    except getopt.GetoptError:
        print("Error!")
        sys.exit(1)
