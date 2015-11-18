#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time,types
import traceback
import logging
import json
import shutil
import paramiko
from remote_tool import tools
from log import dologs
from smartlogApi import *
from install_cluster import *
from api.models import server
from api.models import component
from api.views import *

import threading

numDict = {
    'zookeeper':1,
    'kafka':2,
    'storm':4,
    'elasticsearch':5,
    'flume_server':3,
    'web':8,
    'frontend':6,
    'databases':7
}

nameDict = {
    'zookeeper':'zookeeper',
    'kafka':'kafka',
    'storm':'storm',
    'elasticsearch':'elasticsearch',
    'flume_server':'flume',
    'web':'web',
    'frontend':'frontend',
    'databases':'database'
}

HOME_DIR = r'/home/ultrapower'
if not os.path.exists(HOME_DIR):
    os.system('mkdir -p %s' % HOME_DIR)

CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
dologs.do('smartLog',logging.INFO)

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def _encode(string):
    return string.encode('utf-8')

def start_stop_server_component(param):
    conf = {
             "host":'root@10.0.0.181',
             "password":"ultra",
             "component":"zookeeper",
             "install_dir":"/home/ultrapower",
             "nimbus_ip":"",
             "action":"start|stop",
             "config":{
               "data_dir":"",
             },
             "flag":True
           }
    pass

def get_single_server_status(param):
    return {
            "ip":"10.0.0.171",
            "status":0,
            "components":{
                "ZOOKEEPER":{"status":0},
                "KAFKA":{"status":0},
                "FLUME":{"status":1},
                "STORM":{"status":1},
                "ELASTICSEARCH":{"status":0},
                "WEB":{"status":0},
                "FRONTEND":{"status":0},
                "DATABASE":{"status":0},
                "KEEPLIVE":{"status":0}
            }
        }

def get_cluster_server_status(param):
    return [
        {
             "ip":"10.0.0.171",
             "status":0,
             "components":{
                "ZOOKEEPER":{"status":0},
                "KAFKA":{"status":0},
                "FLUME":{"status":0},
                "STORM":{"status":0},
                "ELASTICSEARCH":{"status":0},
                "WEB":{"status":0},
                "FRONTEND":{"status":0},
                "DATABASE":{"status":0},
                "KEEPLIVE":{"status":0}
            }
        },
        {
             "ip":"10.0.0.172",
             "status":0,
             "components":{
                "ZOOKEEPER":{"status":0},
                "KAFKA":{"status":0},
                "FLUME":{"status":0},
                "STORM":{"status":0},
                "ELASTICSEARCH":{"status":0},
                "WEB":{"status":0},
                "FRONTEND":{"status":0},
                "DATABASE":{"status":0},
                "KEEPLIVE":{"status":0}
            }
        },
        {
             "ip":"10.0.0.173",
             "status":1,
             "components":{
                "ZOOKEEPER":{"status":0},
                "KAFKA":{"status":1},
                "FLUME":{"status":0},
                "STORM":{"status":1},
                "ELASTICSEARCH":{"status":0},
                "WEB":{"status":0},
                "FRONTEND":{"status":1},
                "DATABASE":{"status":0},
                "KEEPLIVE":{"status":0}
            }
        }
    ]

def getServerComponents(id):
    serverDTO = {"id":id, "hostname":None, "cluster_name":None, "role":None, "ip":None, "username":None, "password":None, "components":[]}
    exist_server = server.objects.filter(pk=id)
    if exist_server!=[] and len(exist_server)>0:
        json_data = json.loads(serializers.serialize("json", exist_server))[0]
        serverDTO['hostname'] = json_data['fields']['hostname']
        serverDTO['ip'] = json_data['fields']['ip']
        serverDTO['username'] = json_data['fields']['username']
        serverDTO['password'] = json_data['fields']['password']
        serverDTO['cluster_name'] = json_data['fields']['cluster_name']
        serverDTO['role'] = json_data['fields']['role']
        exist_components = component.objects.filter(server_id=id)
        if exist_components!=[] and len(exist_components)>0:
            json_components = json.loads(serializers.serialize("json", exist_components))
            for item in json_components:
                item_id = item['pk']
                server_id = id
                type = item['fields']['type']
                install_dir = item['fields']['install_dir']
                data_dir = item['fields']['data_dir']
                log_dir = item['fields']['log_dir']
                install_bs = item['fields']['install_bs']
                port = item['fields']['port']
                db_username = item['fields']['db_username']
                db_password = item['fields']['db_password']
                web_service_name = item['fields']['web_service_name']
                frontend_service_name = item['fields']['frontend_service_name']
                es_memory_limit = item['fields']['es_memory_limit']
                es_index_number_of_shards = item['fields']['es_index_number_of_shards']
                es_index_refresh_interval = item['fields']['es_index_refresh_interval']
                es_path_data = item['fields']['es_path_data']
                es_path_logs = item['fields']['es_path_logs']
                storm_works_num_per_host = item['fields']['storm_works_num_per_host']
                storm_dataProcess_works_num = item['fields']['storm_dataProcess_works_num']
                storm_dataIndex_works_num = item['fields']['storm_dataIndex_works_num']
                storm_spout_config_num = item['fields']['storm_spout_config_num']
                storm_spout_dataprocess_num = item['fields']['storm_spout_dataprocess_num']
                storm_spout_dataindex_num = item['fields']['storm_spout_dataindex_num']
                storm_bolt_default_num = item['fields']['storm_bolt_default_num']
                storm_bolt_rule_num = item['fields']['storm_bolt_rule_num']
                storm_bolt_default_num = item['fields']['storm_bolt_default_num']
                storm_bolt_advanced_num = item['fields']['storm_bolt_advanced_num']
                storm_bolt_kafka_num = item['fields']['storm_bolt_kafka_num']
                storm_bolt_es_num = item['fields']['storm_bolt_es_num']
                storm_nimbs_bs = item['fields']['storm_nimbs_bs']
                component_obj = {"id":item_id, "server_id":server_id, "port":port, "type":type, "install_dir":install_dir, "data_dir":data_dir, "log_dir":log_dir, "install_bs":install_bs, "description":None,
                    "db_username":db_username, "db_password":db_password, "web_service_name":web_service_name,
                    "es_memory_limit":es_memory_limit, "es_index_number_of_shards":es_index_number_of_shards,
                    "es_index_refresh_interval":es_index_refresh_interval, "storm_works_num_per_host":storm_works_num_per_host,
                    "storm_dataProcess_works_num":storm_dataProcess_works_num, "storm_dataIndex_works_num":storm_dataIndex_works_num,
                    "storm_spout_config_num":storm_spout_config_num, "storm_spout_dataprocess_num":storm_spout_dataprocess_num,
                    "storm_spout_dataindex_num":storm_spout_dataindex_num, "storm_bolt_default_num":storm_bolt_default_num,
                    "storm_bolt_rule_num":storm_bolt_rule_num, "storm_bolt_advanced_num":storm_bolt_advanced_num,
                    "storm_bolt_kafka_num":storm_bolt_kafka_num, "storm_bolt_es_num":storm_bolt_es_num,
                    "frontend_service_name":frontend_service_name,"es_path_data":es_path_data,
                    "es_path_logs":es_path_logs,"storm_nimbs_bs":storm_nimbs_bs}
                serverDTO['components'].append(component_obj)
    return serverDTO

def valid_single_server(ip, username, password):
    # 输入[{"host":"root@10.0.0.108","password":"ultra"}]
    # 输出 [{'host': '10.0.0.182', 'hostname': 'sl002', 'connected': 0}]
    result = {"available":False, "ip":None, "hostname":None, "message":None}
    param = []
    param_obj = {"host":None,"password":None}
    param_obj['host'] = username + '@' + ip
    param_obj['password'] = password
    param.append(param_obj)
    return_data = judge_server_connected(param)
    # print return_data
    if return_data!=[] and len(return_data) > 0:
        return_obj = return_data[0]
        result['available'] = return_obj['connected']==0
        result['hostname'] = _encode(return_obj['hostname'])
        result['ip'] = _encode(return_obj['host'])
        if result['available']==False:
            result['message'] = _encode("IP/用户名/密码验证未通过!")
    # print result
    return result

def generate_conf(serverComponents):
    # {'server':{'host':'root@10.0.0.181','password':'12345'},'config':{这个字典对应之前说的那个conf文件}}
    conf = {
        "web": {
            "inner_home_dir": "/ultrapower/smartlog-web",
            "service_name": "web",
            "host": "10.0.0.181",
            "port": "8888"
        },
        "frontend": {
            "inner_home_dir": "/ultrapower/smartlog-frontend",
            "service_name": "frontend",
            "host": "10.0.0.181",
            "port": "8899"
        },
        "jdk": {
            "install_dir": "/home/ultrapower",
            "hosts": [
                "10.0.0.181"
            ]
        },
        "zookeeper": {
            "hosts": "10.0.0.181:2181",
            "install_dir": "/home",
            "data_dir": "/home/data",
            "log_dir": "/home/logs"
        },
        "kafka": {
            "hosts": "10.0.0.181:9092",
            "install_dir": "/home",
            "data_dir": "/home/data",
            "log_dir": "/home/logs"
        },
        "elasticsearch": {
            "install_dir":"",
            "data_dir":"",
            "log_dir":"",
            "memory_limit": "2g",
            "index.number_of_shards": "3",
            "storm_conn_hosts": "10.0.0.181:9300",
            "frontend_conn_hosts": "10.0.0.181:9200",
            "index.refresh_interval": "3s",
            "path.data": "/home/ultrapower/data/elasticsearch",
            "path.logs": "/home/ultrapower/logs/elasticsearch"
        },
        "flume_server": {
            "install_dir": "/home/ultrapower",
            "hosts": [
                "10.0.0.181"
            ],
            "agent": "flume"
        },
        "storm": {
            "install_dir": "/home",
            "storm.bolt.default.num": "10",
            "data_dir": "/home/data",
            "storm.dataIndex.works.num": "6",
            "storm.zookeeper.servers": "10.0.0.181",
            "works_num_per_host": "5",
            "storm.bolt.rule.num": "10",
            "storm.bolt.kafka.num": "10",
            "nimbus.host": "10.0.0.181",
            "storm.spout.config.num": "1",
            "storm.bolt.advanced.num": "10",
            "hosts": [
                "10.0.0.181"
            ],
            "storm.bolt.es.num": "20",
            "storm.dataProcess.works.num": "6",
            "storm.spout.dataindex.num": "10",
            "storm.local.dir": "/home/ultrapower/data/storm",
            "storm.spout.dataprocess.num": "10",
            "log_dir": "/home/logs"
        },
        "databases": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "smartlog",
            "HOST": "10.0.0.181",
            "USER": "smartlog",
            "PASSWORD": "smartlog",
            "PORT": "3306"
        },
        "docker": {
            "hosts": [
                "10.0.0.181"
            ]
        },
        "general": {
            "install_dir": "/home/ultrapower",
            "data_dir": "/home/ultrapower/data",
            "log_dir": "/home/ultrapower/logs",
            "current_ip": "10.0.0.181"
        }
    }
    ip = serverComponents['ip']
    conf['general']['current_ip'] = ip
    conf['docker']['hosts'] = [ip]
    conf['jdk']['hosts'] = [ip]
    components = serverComponents['components']
    for item in components:
        type = (item['type']).lower()
        install_bs = item['install_bs']
        if install_bs==True:
            if type == "web":
                conf[type]['host'] = ip
                conf[type]['service_name'] = item['web_service_name']
                conf[type]['port'] = item['port']
            elif type == "frontend":
                conf[type]['host'] = ip
                conf[type]['service_name'] = item['frontend_service_name']
                conf[type]['port'] = item['port']
            elif type == "zookeeper" or type == "kafka" :
                conf[type]['hosts'] = ip + ':' + item['port']
                conf[type]['install_dir'] = item['install_dir']
                conf[type]['data_dir'] = item['data_dir']
                conf[type]['log_dir'] = item['log_dir']
            elif type == "elasticsearch":
                conf[type]['install_dir'] = item['install_dir']
                conf[type]['data_dir'] = item['data_dir']
                conf[type]['log_dir'] = item['log_dir']
                conf[type]['memory_limit'] = item['es_memory_limit']
                conf[type]['index.number_of_shards'] = item['es_index_number_of_shards']
                conf[type]['index.refresh_interval'] = item['es_index_refresh_interval']
                conf[type]['path.data'] = item['es_path_data']
                conf[type]['path.logs'] = item['es_path_logs']
                conf[type]['storm_conn_hosts'] = ip + ':' + item['port']
                conf[type]['frontend_conn_hosts'] = ip + ':9200';
            elif type == "flume":
                conf['flume_server']['install_dir'] = item['install_dir']
                conf['flume_server']['hosts'] = [ip]
            elif type == "storm":
                conf[type]['hosts'] = [ip]
                conf[type]['log_dir'] = item['log_dir']
                conf[type]['storm.local.dir'] = item['data_dir']
                conf[type]['install_dir'] = item['install_dir']
                if item['storm_nimbs_bs']:
                    conf[type]['nimbus.host'] = ip
                else:
                    conf[type]['nimbus.host'] = ""
                conf[type]['storm.zookeeper.servers'] = ip
                conf[type]['works_num_per_host'] = item['storm_works_num_per_host']
                conf[type]['storm.dataProcess.works.num'] = item['storm_dataProcess_works_num']
                conf[type]['storm.dataIndex.works.num'] = item['storm_dataIndex_works_num']
                conf[type]['storm.spout.config.num'] = item['storm_spout_config_num']
                conf[type]['storm.spout.dataprocess.num'] = item['storm_spout_dataprocess_num']
                conf[type]['storm.spout.dataindex.num'] = item['storm_spout_dataindex_num']
                conf[type]['storm.bolt.default.num'] = item['storm_bolt_default_num']
                conf[type]['storm.bolt.rule.num'] = item['storm_bolt_rule_num']
                conf[type]['storm.bolt.advanced.num'] = item['storm_bolt_advanced_num']
                conf[type]['storm.bolt.kafka.num'] = item['storm_bolt_kafka_num']
                conf[type]['storm.bolt.es.num'] = item['storm_bolt_es_num']
            elif type == "database":
                conf['databases']['HOST'] = ip
                conf['databases']['USER'] = item['db_username']
                conf['databases']['PASSWORD'] = item['db_password']
                conf['databases']['PORT'] = item['port']
            else:
                pass
        else:
            if type in ['zookeeper','kafka','storm','elasticsearch','frontend','web']:
                conf.pop(type)
            elif type=="database":
                conf.pop('databases')
            elif type=="flume":
                conf.pop('flume_server')
            else:
                pass
    password = serverComponents['password']
    username = serverComponents['username']
    host = username + "@" + ip
    dto = {"server":{"host":host,"password":password}, "config":conf}
    return dto

def valid_single_server_components(serverComponents):
    conf = []
    single_conf = generate_conf(serverComponents)
    conf.append(single_conf)
    print 'single log :', conf
    check_dto = check_smartlog_config(conf)
    dto = {'available':check_dto['flag'], 'message':check_dto['messages']}
    # if check_dto['flag']:
    #     start_thread(conf)
    return dto

def test_valid_single_server_components(serverComponents):
    dto = {'available':True, 'message':None}
    return dto

def test_valid_cluster_server_components(cluster_name):
    dto = {'available':True, 'message':None}
    return dto

def test_install_single(serverComponents):
    pass

def test_install_cluster(cluster_name):
    pass

def valid_cluster_server_components(cluster_name):
    conf = []
    cluster_server = server.objects.filter(cluster_name=cluster_name)
    if cluster_server!=[] and len(cluster_server)>0:
        for item in cluster_server:
            serverComponents = getServerComponents(item.id)
            single_conf = generate_conf(serverComponents)
            conf.append(single_conf)
    print 'cluster log :', conf
    check_dto = check_smartlog_config(conf)
    dto = {'available':check_dto['flag'], 'message':check_dto['messages']}
    # if check_dto['flag']:
    #     start_thread(conf)
    return dto

def start_thread(conf):
    t = threading.Thread(target=install_components,args=(conf,))
    t.start()

def generate_status_conf(serverComponents):
    conf = {'host':None, 'password':None, 'extraMessages':None}
    ip = serverComponents['ip']
    username = serverComponents['username']
    conf['host'] = username + "@" + ip
    conf['password'] = serverComponents['password']
    components = serverComponents['components']
    items = []
    for item in components:
        type = (item['type']).lower()
        if type =='database':
            type = 'databases'
        elif type == 'flume':
            type = 'flume_server'
        else:
            pass
        install_bs = item['install_bs']
        if install_bs == True:
            obj = {'component':type, 'install_dir':item['install_dir']}
            items.append(obj)
    conf['extraMessages'] = items
    return conf

def get_single_server_finish(serverComponents):
    conf = []
    single_server = generate_status_conf(serverComponents)
    conf.append(single_server)
    status_dto = get_component_status(conf)
    ip = serverComponents['ip']
    dto = {"ip":ip, "components":status_dto}
    return dto

def test_get_single_server_finish(serverComponents):
    returnData = {"ip":"10.0.0.200", "components":
    [
    {"name":"ZOOKEEPER","status":1,"current_status":False,"log":""},
    {"name":"KAFKA","status":0,"current_status":False,"log":""},
    {"name":"FLUME","status":-1,"current_status":False,"log":""},
    {"name":"STORM","status":1,"current_status":True,"log":""},
    {"name":"ELASTICSEARCH","status":1,"current_status":False,"log":""},
    {"name":"FONTWEB","status":1,"current_status":False,"log":""},
    {"name":"DATABASE","status":-1,"current_status":False,"log":""},
    {"name":"WEB","status":1,"current_status":False,"log":""}
    ]}
    return returnData

def get_cluster_server_finish(cluster_name):
    conf = []
    cluster_server = server.objects.filter(cluster_name=cluster_name)
    if cluster_server!=[] and len(cluster_server)>0:
        for item in cluster_server:
            serverComponents = getServerComponents(item.id)
            single_conf = generate_status_conf(serverComponents)
            conf.append(single_conf)
    status_dto = get_component_status(conf)
    dto = {"components":status_dto}
    return dto

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
    {"name":"FONTWEB","status":1,"current_status":False,
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

"""
    判断server的连通性
    parameter is list
    parameter:
    [{"host":"root@10.0.0.108","password":"ultra"},{"host":"root@10.0.0.109","password":"ultra"}]
    return:
    [{'host': '10.0.0.182', 'hostname': 'sl002', 'connected': 0}, {'host': '10.0.0.181', 'hostname': 'sl001', 'connected': 0}]
"""
def judge_server_connected(parameter):
    logging.info('start test server connected !!!')
    rst_list = []
    cmd = r'hostname'
    hostname = ''
    para = []

    for item in parameter:
        rst = {}
        address = item['host'].split('@')[1]
        flag = valid_ip(address)
        if not flag:
            rst['host'] = address
            rst['connected'] = 1
            rst['hostname'] = ''
            rst_list.append(rst)
            logging.info('%s address error,please check up!!!' % (address))
        else:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(address,username=item['host'].split('@')[0],password=item['password'],timeout=3)
                ssh.close()
                rst['host'] = address
                rst['connected'] = 0
                rst['hostname'] = ''
                rst_list.append(rst)
                para.append(item)
            except BaseException , e :
                rst['host'] = address
                rst['connected'] = 1
                rst['hostname'] = ''
                rst_list.append(rst)
                continue
                logging.info(str(e))
    if para:
        cmd_result = tools.remote_cmd(parameter,cmd)
        for each in cmd_result:
            if each[1] == 0:
                rstStr = each[2][0]
                outStr = rstStr.split('\n')[2]
                if outStr:
                    hostname= outStr.split(':')[1].strip(' ')
                else:
                    hostname = ''
            else:
                hostname = ''
            for item in rst_list:
                if item['host'] == each[0].split('@')[1] and item['connected'] == 0:
                    item['hostname'] = hostname
                    break

            logging.info('%s server connected check up over' % (each[0].split('@')[1]))
    return rst_list

"""
    check_smartlog_config
    parameter:
    [{'server':{"host":"root@1000.0.0.181","password":"ultra"},'config':{}}]
"""
def check_component_status(item,name):
    if item.has_key(name):
        return True
    else:
        return False


def check_smartlog_config(parameter):
    logging.info('start check component config!!!')
    messages = []
    smartlog_flag = {}
    flag = False
    for item in parameter:
        try:
            if check_component_status(item['config'],'web'):
                web_flag,messages = check_web(item['config']['web'],messages)
            else:
                web_flag = True
            if check_component_status(item['config'],'frontend'):
                frontend_flag,messages = check_web(item['config']['frontend'],messages)
            else:
                frontend_flag = True
            if check_component_status(item['config'],'jdk'):
                jdk_flag,messages = check_jdk(item['config']['jdk'],messages)
            else:
                jdk_flag = True
            if check_component_status(item['config'],'zookeeper'):
                zoo_flag,messages = check_zookeeper(item['config']['zookeeper'],messages)
            else:
                zoo_flag = True
            if check_component_status(item['config'],'kafka'):
                kafka_flag,messages = check_zookeeper(item['config']['kafka'],messages)
            else:
                kafka_flag = True
            if check_component_status(item['config'],'elasticsearch'):
                es_flag,messages  = check_elasticsearch(item['config']['elasticsearch'],messages)
            else:
                es_flag = True
            if check_component_status(item['config'],'storm'):
                storm_flag,messages  = check_jdk(item['config']['storm'],messages)
            else:
                storm = True
            if check_component_status(item['config'],'flume_server'):
                flume_server_flag,messages  = check_jdk(item['config']['flume_server'],messages)
            else:
                flume_server_flag = True
            if check_component_status(item['config'],'docker'):
                docker_flag,messages  = check_jdk(item['config']['docker'],messages)
            else:
                docker_flag = True
            if check_component_status(item['config'],'databases'):
                databases_flag,messages = check_databases(item['config']['databases'],messages)
            else:
                databases_flag = True
            if web_flag and frontend_flag and jdk_flag and zoo_flag and kafka_flag and es_flag and storm_flag and flume_server_flag and docker_flag and databases_flag:
                smartlog_flag[item['server']['host']] = True
            else:
                smartlog_flag[item['server']['host']] = False
        except BaseException , e :
            logging.info(str(e))
    length = len(smartlog_flag)
    num = 0
    for key,value in smartlog_flag.items():
        if value:
            num += 1

        if num == length:
            flag = True
    logging.info('check component config done!!!')
    return {'flag':flag,'messages':messages}

def check_databases(para,messages):
    flag_addr = False
    flag_port = False
    flag_web = False
    web_host = para['HOST']
    web_port = para['PORT']
    if valid_ip(web_host) :
        flag_addr = True
    else:
        msg_err = ' %s web component ip config Error!!!' % web_host
        logging.info(msg_err)
        messages.append(msg_err)
    if valid_port(web_port):
        flag_port = True
    else:
        msg_err = '%s web component port config Error!!!' % web_port
        logging.info(msg_err)
        messages.append(_encode(msg_err))
    if flag_addr and flag_port:
        flag_web = True
    return flag_web,messages


def check_web(para,messages):
    flag_addr = False
    flag_port = False
    flag_web = False
    web_host = para['host']
    web_port = para['port']
    if valid_ip(web_host) :
        flag_addr = True
    else:
        msg_err = ' %s web component ip config Error!!!' % web_host
        logging.info(msg_err)
        messages.append(msg_err)
    if valid_port(web_port):
        flag_port = True
    else:
        msg_err = '%s web component port config Error!!!' % web_port
        logging.info(msg_err)
        messages.append(msg_err)
    if flag_addr and flag_port:
        flag_web = True
    return flag_web,messages

def check_jdk(para,messages):
    flag = False
    jdk_hosts = para['hosts']
    for host in jdk_hosts:
        if valid_ip(host):
            flag = True
        else:
            flag = False
            msg_err = ' %s jdk component ip config Error!!!' % host
            logging.info(msg_err)
            messages.append(msg_err)

    return flag,messages

def check_zookeeper(para,messages):
    zoo_hosts = []
    zoo_ports = []
    flag_addr = False
    flag_port = False
    flag_zoo = False
    zookeeper = para['hosts'].split(',')
    for each in zookeeper:
        zoo_hosts.append(each.split(':')[0])
        zoo_ports.append(each.split(':')[1])

    for host in zoo_hosts:
        if valid_ip(host):
            flag_addr = True
        else:
            flag_addr = False
            msg_err = ' %s zookeeper component ip config Error!!!' % host
            logging.info(msg_err)
            messages.append(msg_err)

    for port in zoo_ports:
        if valid_port(port):
            flag_port = True
        else:
            flag_port = False
            msg_err = '%s zookeeper component port config Error!!!' % port
            logging.info(msg_err)
            messages.append(msg_err)

    if flag_addr and flag_port:
        flag_zoo = True

    return flag_zoo,messages

def check_elasticsearch(para,messages):
    es_hosts_storm = []
    es_ports_storm = []
    es_hosts_frontend = []
    es_ports_frontend = []
    flag_addr_storm = False
    flag_port_storm = False
    flag_addr_frontend = False
    flag_port_frontend = False
    flag_es = False
    es_storm = para['storm_conn_hosts'].split(',')
    es_frontend = para['frontend_conn_hosts'].split(',')
    for each in es_storm:
        es_hosts_storm.append(each.split(':')[0])
        es_ports_storm.append(each.split(':')[1])

    for each in es_frontend:
        es_hosts_frontend.append(each.split(':')[0])
        es_ports_frontend.append(each.split(':')[1])

    for host in es_hosts_storm:
        if valid_ip(host):
            flag_addr_storm = True
        else:
            flag_addr_storm = False
            msg_err = ' %s elasticsearch component ip config Error!!!' % host
            logging.info(msg_err)
            messages.append(msg_err)

    for port in es_ports_storm:
        if valid_port(port):
            flag_port_storm = True
        else:
            flag_port_storm = False
            msg_err = '%s elasticsearch component port config Error!!!' % port
            logging.info(msg_err)
            messages.append(msg_err)

    for host in es_hosts_frontend:
        if valid_ip(host):
            flag_addr_frontend = True
        else:
            flag_addr_frontend = False
            msg_err = ' %s elasticsearch component ip config Error!!!' % host
            logging.info(msg_err)
            messages.append(msg_err)

    for port in es_ports_frontend:
        if valid_port(port):
            flag_port_frontend = True
        else:
            flag_port_frontend = False
            msg_err = '%s elasticsearch component port config Error!!!' % port
            logging.info(msg_err)
            messages.append(msg_err)

    if flag_addr_frontend and flag_port_frontend and flag_addr_storm and flag_port_storm:
        flag_es = True

    return flag_es,messages


"""
    获取集群中各组件状态以及安装日志
    parameters：
    [{'host':'root@10.0.0.181','password':'ultra','extraMessages':[{'component':'kafka','install_dir':'/home/ultrapower'},{'component':'kafka','install_dir':'/home/ultrapower'}]},{'host':'root@10.0.0.182','password':'ultra','extraMessages':[{'component':'zookeeper','install_dir':'/home/ultrapower'},{'component':'flume','install_dir':'/home'}]]
    status：
    -1：未安装
    0：安装且组件启动正常
    1：安装且组件启动异常
"""
def get_component_status(parameters):
    host_list = []
    upload_path = os.path.normpath(HOME_DIR + r'/upload/')
    local_status_path = os.path.normpath(CURRENT_DIR + r'/status.json')
    local_py_path = os.path.normpath(CURRENT_DIR + r'/getServerStatus.py')
    dst_path  = '/home/test/smartStatus'
    if not os.path.exists(dst_path):
        cmd = 'mkdir -p %s' % dst_path
        os.system(cmd)

    for item in parameters:
        tmpDict = {}
        tmpDict['host'] = item['host']
        tmpDict['password'] = item['password']
        host_list.append(tmpDict)
        del item['password']
        fp = open(local_status_path,'w')
        fp.write(json.dumps(item))
        fp.close()
        tools.remote_singe_upload(tmpDict,local_status_path,upload_path)
    tools.remote_up_file(host_list,local_py_path,upload_path)
    cmd_status = 'cd %s && python getServerStatus.py "%s"' % (upload_path,os.path.normpath(upload_path + r'/status.json'))
    tools.remote_cmd(host_list,cmd_status)
    logging.info('start get status file from yuanchengfuwuqi !!!!')
    for item in host_list:
        src_path = r'/home/ultrapower/upload/status_%s' % item['host'].split('@')[1]
        logging.info(tools.remote_single_download(item,src_path,dst_path))

    logging.info('end get status file from yuanchengfuwuqi !!!!')

    result_list = getStatusFromFile(dst_path)
    for item in result_list:
        item_list = []
        for each in item['components']:
            each_dict = {}
            if not each['install_status']:
                each_dict['status'] = -1
                each_dict['current_status'] = each['current_status']
            if each['install_status'] and not each['current_status'] and each['process_status']:
                each_dict['status'] = 0
                each_dict['current_status'] = False
            if each['install_status'] and not each['current_status'] and not each['process_status']:
                each_dict['status'] = 1
                each_dict['current_status'] = False
            each_dict['log'] = each['log']
            each_dict['host'] = each['host']
            item_list.append(each_dict)
        item['components'] = item_list

    logging.info('end getStatusFromFile : %s' % str(result_list))

    for item in result_list:
        sum_status_zero = 0
        sum_current = 0
        length = len(item['components'])
        for each in item['components']:
            if each['status'] == 0:
                sum_status_zero += 1
            if each['status'] == -1:
                item['status'] = -1
                item['current_status'] = True
            if each['status'] == 1:
                item['status'] = 1
                item['current_status'] = False
            if not each['current_status']:
                sum_current += 1
            if sum_status_zero == length and sum_current == length:
                item['status'] = 0
                item['current_status'] = False

    for item in result_list:
        if numDict[item['name']]:
            item['index'] = numDict[item['name']]
            item['showname'] = nameDict[item['name']]

    return result_list

def getStatusFromFile(dst_path):
    zookeeper_list = []
    zookeeper_dict = {}
    storm_list = []
    storm_dict = {}
    flume_list = []
    flume_dict = {}
    kafka_list = []
    kafka_dict = {}
    es_list = []
    es_dict ={}
    web_list = []
    web_dict = {}
    frontend_list = []
    frontend_dict = {}
    mysql_list = []
    mysql_dict = {}
    result = []
    for file in os.listdir(dst_path):
        filepath = os.path.join(dst_path,file)
        logging.info(str(filepath))
        if filepath.endswith('.bak'):
            os.remove(filepath)
            continue
        else:
            fp = open(filepath,'r')
            rst = json.loads(fp.read(),encoding="utf-8")
            fp.close()
            for key,values in rst.items():
                for item in values:
                    if item['component'] == 'zookeeper':
                        item['host'] = key
                        zookeeper_dict['name'] = item['component']
                        del item['component']
                        zookeeper_list.append(item)
                        zookeeper_dict['components'] = zookeeper_list
                    elif item['component'] == 'storm':
                        item['host'] = key
                        storm_dict['name'] = item['component']
                        del item['component']
                        storm_list.append(item)
                        storm_dict['components'] = storm_list
                    elif item['component'] == 'kafka':
                        item['host'] = key
                        kafka_dict['name'] = item['component']
                        del item['component']
                        kafka_list.append(item)
                        kafka_dict['components'] = kafka_list
                    elif item['component'] == 'flume_server':
                        item['host'] = key
                        flume_dict['name'] = item['component']
                        del item['component']
                        flume_list.append(item)
                        flume_dict['components'] = flume_list
                    elif item['component'] == 'elasticsearch':
                        item['host'] = key
                        es_dict['name'] = item['component']
                        del item['component']
                        es_list.append(item)
                        es_dict['components'] = es_list
                    elif item['component'] == 'web':
                        item['host'] = key
                        web_dict['name'] = item['component']
                        del item['component']
                        web_list.append(item)
                        web_dict['components'] = web_list
                    elif item['component'] == 'frontend':
                        item['host'] = key
                        frontend_dict['name'] = item['component']
                        del item['component']
                        frontend_list.append(item)
                        frontend_dict['components'] = frontend_list
                    elif item['component'] == 'databases':
                        item['host'] = key
                        mysql_dict['name'] = item['component']
                        del item['component']
                        mysql_list.append(item)
                        mysql_dict['components'] = mysql_list
                    if os.path.exists(filepath):
                        os.rename(filepath,filepath + '.' + str(int(time.time())) + '.bak')
    if zookeeper_dict:
        result.append(zookeeper_dict)
    if storm_dict:
        result.append(storm_dict)
    if kafka_dict:
        result.append(kafka_dict)
    if flume_dict:
        result.append(flume_dict)
    if es_dict:
        result.append(es_dict)
    if web_dict:
        result.append(web_dict)
    if frontend_dict:
        result.append(frontend_dict)
    if mysql_dict:
        result.append(mysql_dict)

    return result

"""
    install components to server
    parameter:
    [{'server':{"host":"root@1000.0.0.181","password":"ultra"},'config':{}}]
"""

def install_components(parameter):
    logging.info('start install smartlog component ...')
    install_smart(parameter)
    logging.info('end install smartlog component ...')


if __name__ == '__main__':
    parameter = [{"host":"root@1000.0.0.181","password":"1234"},{"host":"root@10.0.0.182","password":"ultra"}]
    judge_server_connected(parameter)
    # parameter = [{'host':'root@10.0.0.181','password':'ultra','extraMessages':[{'component':'frontend','install_dir':'/home'},{'component':'zookeeper','install_dir':'/home'}]},{'host':'root@10.0.0.182','password':'ultra','extraMessages':[{'component':'web','install_dir':'/home'},{'component':'flume','install_dir':'/home'}]},{'host':'root@10.0.0.183','password':'ultra','extraMessages':[{'component':'web','install_dir':'/home'},{'component':'flume','install_dir':'/home'}]}]
    # get_component_status(parameter)
    # name = 'frontend'
    # install_dir = r'/home'
    # processName = r'nimbus'
    # check_is_install(hosts,name,install_dir)
    # _check_unit_alive_(hosts,processName)

    #print check_smartlog_config(parameter)
