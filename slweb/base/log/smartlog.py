#!/usr/bin/env python

import distutils.file_util
import logging
import time
import os
import sys

def basicConfig(filename=None,filemode=None,format=None,datefmt=None,level=None,stream=None) :
    fname = str(filename)
    if os.path.exists(fname) :
        do_make_backup(fname)
    logging.basicConfig(filename = filename,\
                        filemode = filemode,\
                        format = format,\
                        datefmt = datefmt,\
                        level = level,\
                        stream = stream)

def do_make_backup(fname) :
    try :
        folder = os.path.basename(fname).split('.')[0]
        base_dir = fname[:fname.rfind(folder)]
        if not os.path.exists(base_dir + os.sep + folder) :
            os.mkdir(base_dir + os.sep + folder)
        cdate = time.strftime('%Y%m%d',time.localtime(time.time()))
        if not os.path.exists(base_dir + os.sep + folder + os.sep + cdate) :
            os.mkdir(base_dir + os.sep + folder + os.sep + cdate)
        dtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        nfname = folder + '-' + dtime + '.log'
        dst = base_dir + os.sep + folder + os.sep + cdate + os.sep + nfname
        distutils.file_util.copy_file(fname,dst)
    except BaseException , e :
        pass

def basicConfigEx(filename=None,filemode=None,format=None,datefmt=None,level=None,stream=None,prefix='') :
    if not len(prefix) :
        basicConfig(filename=filename,\
                    filemode=filemode,\
                    format=format,\
                    datefmt=datefmt,\
                    level=level,\
                    stream=stream)
    else :
        _dir_name = os.path.dirname(filename)
        for _f in os.listdir(_dir_name) :
            if str(_f).lower().startswith(str(prefix).lower()) :
                _do_backup(_dir_name , _f , prefix)
        basicConfig(filename=filename,\
                    filemode=filemode,\
                    format=format,\
                    datefmt=datefmt,\
                    level=level,\
                    stream=stream)

def _do_backup(_dirname , _filename , _prefix) :
    try :
        _folder = os.path.normpath(_dirname + os.sep + _prefix)
        if not os.path.exists(_folder) :
            os.makedirs(_folder)
        _cdate = time.strftime('%Y%m%d')
        _log_folder = os.path.normpath(_folder + os.sep + _cdate)
        if not os.path.exists(_log_folder) :
            os.mkdir(_log_folder)
        _src = os.path.normpath(_dirname + os.sep + _filename)
        _filename_prefix = dtime = time.strftime('%Y-%m-%d-%H-%M-%S')
        _t = str(_filename).split('.')
        _t.insert(-1,_filename_prefix)
        _new_name = '.'.join(_t)
        _dst = os.path.normpath(_log_folder + os.sep + _new_name)
        distutils.file_util.move_file(_src,_dst)
    except BaseException , e :
        pass

if __name__ == '__main__' :
    log_file = '/media/truecrypt1/nsc/main/6.1.1.1/src/pymods/gg_mm.log'
    basicConfigEx(level=logging.NOTSET,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m-%d %H:%M:%S',
            filename=log_file,
            filemode='w' ,
            prefix = 'gg')