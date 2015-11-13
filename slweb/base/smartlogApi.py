#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,time
import socket

def valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except BaseException , e :
        return False

def valid_port(port):
    try:
        if 0 < int(port) <= 65535:
            return True
        else:
            return False
    except BaseException , e :
        return False

def _encode(string):
    return string.encode('utf-8')
