#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import smartlog
import os,sys

def __get_smart_root():
    return '/home/ultrapower'

def __get_log_file(logfile) :
    if not str(logfile).endswith('.log') :
        logfile = str(logfile) + '.log'
    _log_file = os.path.normpath(__get_smart_root() + r'/logs/' + logfile)
    return _log_file

def do(logfile , _level = logging.NOTSET , nsc_pos = True) :
    if nsc_pos :
        _log_file = __get_log_file(logfile)
    else :
        _log_file = os.path.normpath(logfile)
        _p = os.path.dirname(os.path.normpath(logfile))
        if not os.path.exists(_p) :
            os.makedirs(_p)
    smartlog.basicConfig(level = _level ,
                       format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                       datefmt='%m-%d %H:%M:%S',
                       filename=_log_file,
                       filemode='w' )