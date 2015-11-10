#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,time,types
import traceback
import logging

from remote_tool import tools
from log import dologs
from smartlogApi import *

CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
dologs.do('smartLog',logging.INFO)

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

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

def valid_single_server_components(serverComponents):
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
    conf['docker']['host'] = ip
    conf['jdk']['hosts'] = [ip]
    components = serverComponents['components']
    for item in components:
        type = (item['type']).lower()
        print 'test = ', type
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
            conf[type]['memory_limit'] = item['es_memory_limit']
            conf[type]['index.number_of_shards'] = item['es_index_number_of_shards']
            conf[type]['index.refresh_interval'] = item['es_index_refresh_interval']
            conf[type]['path.data'] = item['data_dir']
            conf[type]['path.logs'] = item['log_dir']
            conf[type]['frontend_conn_hosts'] = ip + ':' + item['port']
            conf[type]['storm_conn_hosts'] = ip + ':9200';
        elif type == "flume":
            conf['flume_server']['install_dir'] = item['install_dir']
            conf['flume_server']['hosts'] = [ip]
        elif type == "storm":
            conf[type]['hosts'] = [ip]
            conf[type]['log_dir'] = item['log_dir']
            conf[type]['storm.local.dir'] = item['data_dir']
            conf[type]['install_dir'] = item['install_dir']
            conf[type]['nimbus.host'] = ip
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
    return_data = check_smartlog_config(conf)
    return_dto = {'available':return_data['flag'], 'message':return_data['messages']}
    return return_dto

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
    {"name":"FONTWEB","status":1,"current_status":False,"log":""},
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
    rst_list = []
    cmd = r'hostname'
    # parameter = [{"host":"root@10.0.0.181","password":"ultra"},{"host":"root@10.0.0.182","password":"ultra"}]
    # local_path = os.path.join(CURRENT_DIR,'test.file')
    # remote_path = r'/test.file'
    # up_result = tools.remote_up_file(parameter,local_path,remote_path)
    # for item in up_result:
    #     tmp = {}
    #     tmp['connected'] = item[1]
    #     tmp['host'] = item[0].split('@')[1]
    #     rst_list.append(tmp)

    # print rst_list
    for item in parameter:
        rst = {}
        address = item['host'].split('@')[1]
        flag = valid_ip(address)
        if not flag:
            rst['host'] = address
            rst['connected'] = 1
            rst['hostname'] = ''
            rst_list.append(rst)
            parameter.remove(item)
            logging.info('%s address error,please check up!!!' % (address))

    if parameter:
        cmd_result = tools.remote_cmd(parameter,cmd)
        print 'begin', cmd_result
        for each in cmd_result:
            tmp = {}
            if each[1] == 0:
                rstStr = each[2][0]
                outStr = rstStr.split('\n')[2]
                if outStr:
                    tmp['hostname'] = outStr.split(':')[1].strip(' ')
                else:
                    tmp['hostname'] = ''
            else:
                tmp['hostname'] = ''
            tmp['connected'] = each[1]
            tmp['host'] = each[0].split('@')[1]
            rst_list.append(tmp)
            print 'end', rst_list
            logging.info('%s server connected check up over' % (each[0].split('@')[1]))
    # print rst_list
    return rst_list


"""
    安装smartlog参数
    parameter is dict
    eg:
    {
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
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
        ]
    },
    "zookeeper": {
        "hosts": "10.0.0.181:2181,10.0.0.182:2181,10.0.0.183:2181",
        "install_dir": "/home",
        "data_dir": "/home/data",
        "log_dir": "/home/logs"
    },
    "kafka": {
        "hosts": "10.0.0.181:9092,10.0.0.182:9092,10.0.0.183:9092",
        "install_dir": "/home",
        "data_dir": "/home/data",
        "log_dir": "/home/logs"
    },
    "elasticsearch": {
        "memory_limit": "2g",
        "index.number_of_shards": "3",
        "storm_conn_hosts": "10.0.0.182:9300,10.0.0.183:9300",
        "frontend_conn_hosts": "10.0.0.182:9200,10.0.0.183:9200",
        "index.refresh_interval": "3s",
        "path.data": "/home/ultrapower/data/elasticsearch",
        "path.logs": "/home/ultrapower/logs/elasticsearch"
    },
    "flume_server": {
        "install_dir": "/home/ultrapower",
        "hosts": [
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
        ],
        "agent": "flume"
    },
    "storm": {
        "install_dir": "/home",
        "storm.bolt.default.num": "10",
        "data_dir": "/home/data",
        "storm.dataIndex.works.num": "6",
        "storm.zookeeper.servers": "10.0.0.181,10.0.0.182,10.0.0.183",
        "works_num_per_host": "5",
        "storm.bolt.rule.num": "10",
        "storm.bolt.kafka.num": "10",
        "nimbus.host": "10.0.0.181",
        "storm.spout.config.num": "1",
        "storm.bolt.advanced.num": "10",
        "hosts": [
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
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
"""

def check_smartlog_config(parameter):
    smartlog_flag = False
    messages = []
    web_flag,messages= check_web(parameter['web'],messages)
    frontend_flag,messages = check_web(parameter['frontend'],messages)
    jdk_flag,messages = check_jdk(parameter['jdk'],messages)
    zoo_flag,messages = check_zookeeper(parameter['zookeeper'],messages)
    kafka_flag,messages = check_zookeeper(parameter['kafka'],messages)
    es_flag,messages  = check_elasticsearch(parameter['elasticsearch'],messages)
    storm_flag,messages  = check_jdk(parameter['storm'],messages)
    flume_server_flag,messages  = check_jdk(parameter['flume_server'],messages)
    docker_flag,messages  = check_jdk(parameter['docker'],messages)
    databases_flag,messages = check_databases(parameter['databases'],messages)
    if web_flag and frontend_flag and jdk_flag and zoo_flag and kafka_flag and es_flag and storm_flag and flume_server_flag and docker_flag and databases_flag:
        smartlog_flag = True
    return {'flag':smartlog_flag,'messages':messages}

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
        messages.append(msg_err)
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


if __name__ == '__main__':
    # parameter = [{"host":"root@1000.0.0.181","password":"ultra"},{"host":"root@10.0.0.182","password":"ultra"}]
    # judge_server_connected(parameter)
    parameter = {
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
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
        ]
    },
    "zookeeper": {
        "hosts": "10.0.0.181:2181,10.0.0.182:2181,10.0.0.183:2181",
        "install_dir": "/home",
        "data_dir": "/home/data",
        "log_dir": "/home/logs"
    },
    "kafka": {
        "hosts": "10.0.0.181:9092,10.0.0.182:9092,10.0.0.183:9092",
        "install_dir": "/home",
        "data_dir": "/home/data",
        "log_dir": "/home/logs"
    },
    "elasticsearch": {
        "memory_limit": "2g",
        "index.number_of_shards": "3",
        "storm_conn_hosts": "10.0.0.182:9300,10.0.0.183:9300",
        "frontend_conn_hosts": "10.0.0.182:9200,10.0.0.183:9200",
        "index.refresh_interval": "3s",
        "path.data": "/home/ultrapower/data/elasticsearch",
        "path.logs": "/home/ultrapower/logs/elasticsearch"
    },
    "flume_server": {
        "install_dir": "/home/ultrapower",
        "hosts": [
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
        ],
        "agent": "flume"
    },
    "storm": {
        "install_dir": "/home",
        "storm.bolt.default.num": "10",
        "data_dir": "/home/data",
        "storm.dataIndex.works.num": "6",
        "storm.zookeeper.servers": "10.0.0.181,10.0.0.182,10.0.0.183",
        "works_num_per_host": "5",
        "storm.bolt.rule.num": "10",
        "storm.bolt.kafka.num": "10",
        "nimbus.host": "10.0.0.181",
        "storm.spout.config.num": "1",
        "storm.bolt.advanced.num": "10",
        "hosts": [
            "10.0.0.181",
            "10.0.0.182",
            "10.0.0.183"
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
    print check_smartlog_config(parameter)

def _encode(string):
    return string.encode('utf-8')
