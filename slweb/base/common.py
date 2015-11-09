#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_valid_single_server(ip, username, password):
    returnData = {"available":True, "hostname":"cxj002", "message":"消息测试"}
    return returnData

def test_valid_single_server_components(serverComponents):
    test = "ZOOKPEER测试消息1;ZOOKPEER测试消息2"
    returnData = {'available':False, 'message':test}
    return returnData

def test_valid_cluster_server_components(serverComponents):
    test = "ZOOKPEER测试消息1;ZOOKPEER测试消息2"
    returnData = {'available':False, 'message':test}
    return returnData

def test_get_single_server_finish(serverComponents):
    returnData = {"ip":"10.0.0.200", "components":
    [
    {"name":"ZOOKEEPER","status":1,"current_status":False,"log":""},
    {"name":"KAFKA","status":0,"current_status":False,"log":""},
    {"name":"FLUME","status":-1,"current_status":False,"log":""},
    {"name":"STORM","status":1,"current_status":True,"log":""},
    {"name":"ELASTICSEARCH","status":1,"current_status":False,"log":""},
    {"name":"FRONTEND","status":1,"current_status":False,"log":""},
    {"name":"DATABASE","status":-1,"current_status":False,"log":""},
    {"name":"WEB","status":1,"current_status":False,"log":""}
    ]}
    return returnData

def test_get_cluster_server_finish(serverComponents):
    returnData = {"components":
    [
    {
    "name":"ZOOKEEPER","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"KAFKA","status":0,"current_status":True,
    "components":[
    {"ip":"10.0.0.200","status":0,"current_status":True,"log":""},
    {"ip":"10.0.0.201","status":0,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":0,"current_status":False,"log":""}
    ]},
    {"name":"FLUME","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"STORM","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"ELASTICSEARCH","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"FRONTEND","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"DATABASE","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    {"name":"WEB","status":1,"current_status":False,
    "components":[
    {"ip":"10.0.0.200","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.201","status":1,"current_status":False,"log":""},
    {"ip":"10.0.0.202","status":1,"current_status":False,"log":""}
    ]},
    ]}
    return returnData
