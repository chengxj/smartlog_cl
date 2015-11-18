#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import server
from api.models import component
from api.models import warn
from django.core import serializers
from serializers import serverSerializer

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import json
from base import common

@api_view(['post'])
def add_single_server(request):
    # 输入参数 ip username password
    ip = request.data['ip']
    username = request.data['username']
    password = request.data['password']
    serverDTO = {"available":False, "id":None, "message":None, "component_bs":False, "install_bs":False}
    exist_server = server.objects.filter(type='single', ip=ip, username=username, password=password)
    if exist_server!=[] and len(exist_server)>0:
        serverDTO['available'] = True
        filter_server = json.loads(serializers.serialize("json", exist_server))[0]
        serverDTO['id'] = filter_server['pk']
        serverDTO['install_bs'] = filter_server['fields']['install_bs']
        filter_components = component.objects.filter(server_id = filter_server['pk'])
        serverDTO['component_bs'] = False
        if filter_components!=[] and len(filter_components)>0:
            serverDTO['component_bs'] = True
    else:
        existDTO = common.valid_single_server(ip, username, password)
        if(existDTO['available']==True):
            serverDTO['available'] = True
            server_obj = server(type='single', ip=ip, username=username, password=password, hostname=existDTO['hostname'])
            server_obj.save()
            serverDTO['id'] = server_obj.id
        else:
            serverDTO['message'] = existDTO['message']
    return Response(serverDTO)

@api_view(['post'])
def get_single_server(request):
    id = request.data['id']
    serverDTO = {"id":id, "hostname":None, "ip":None, "username":None, "password":None}
    exist_server = server.objects.filter(pk=id)
    if exist_server!=[] and len(exist_server)>0:
        json_data = json.loads(serializers.serialize("json", exist_server))[0]
        serverDTO['hostname'] = json_data['fields']['hostname']
        serverDTO['ip'] = json_data['fields']['ip']
        serverDTO['username'] = json_data['fields']['username']
        serverDTO['password'] = json_data['fields']['password']
    return Response(serverDTO)

@api_view(['post'])
def get_cluster_server_components(request):
    cluster_name = request.data['cluster_name']
    exist_server = server.objects.filter(cluster_name=cluster_name)
    cluster_server_dto = {"cluster_server":None}
    if exist_server!=[] and len(exist_server)>0:
        json_data = json.loads(serializers.serialize("json", exist_server))
        print json_data
        cluster_server = []
        for item in json_data:
            obj = {"id":None, "ip":"","username":"","password":"","hostname":"","role":"","components":None}
            obj['ip'] = item['fields']['ip']
            obj['username'] = item['fields']['username']
            obj['password'] = item['fields']['password']
            obj['hostname'] = item['fields']['hostname']
            obj['role'] = item['fields']['role']
            obj['id'] = item['pk']
            obj['install_bs'] = item['fields']['install_bs']
            cluster_components = component.objects.filter(server_id=obj['id'])
            components = []
            if cluster_components!=[] and len(cluster_components)>0:
                components_json = json.loads(serializers.serialize("json", cluster_components))
                for component_json in components_json:
                    item_id = component_json['pk']
                    server_id = component_json['fields']['server_id']
                    type = component_json['fields']['type']
                    install_dir = component_json['fields']['install_dir']
                    data_dir = component_json['fields']['data_dir']
                    log_dir = component_json['fields']['log_dir']
                    install_bs = component_json['fields']['install_bs']
                    port = component_json['fields']['port']
                    db_username = component_json['fields']['db_username']
                    db_password = component_json['fields']['db_password']
                    web_service_name = component_json['fields']['web_service_name']
                    frontend_service_name = component_json['fields']['frontend_service_name']
                    es_memory_limit = component_json['fields']['es_memory_limit']
                    es_index_number_of_shards = component_json['fields']['es_index_number_of_shards']
                    es_index_refresh_interval = component_json['fields']['es_index_refresh_interval']
                    es_path_data = component_json['fields']['es_path_data']
                    es_path_logs = component_json['fields']['es_path_logs']
                    storm_works_num_per_host = component_json['fields']['storm_works_num_per_host']
                    storm_dataProcess_works_num = component_json['fields']['storm_dataProcess_works_num']
                    storm_dataIndex_works_num = component_json['fields']['storm_dataIndex_works_num']
                    storm_spout_config_num = component_json['fields']['storm_spout_config_num']
                    storm_spout_dataprocess_num = component_json['fields']['storm_spout_dataprocess_num']
                    storm_spout_dataindex_num = component_json['fields']['storm_spout_dataindex_num']
                    storm_bolt_default_num = component_json['fields']['storm_bolt_default_num']
                    storm_bolt_rule_num = component_json['fields']['storm_bolt_rule_num']
                    storm_bolt_default_num = component_json['fields']['storm_bolt_default_num']
                    storm_bolt_advanced_num = component_json['fields']['storm_bolt_advanced_num']
                    storm_bolt_kafka_num = component_json['fields']['storm_bolt_kafka_num']
                    storm_bolt_es_num = component_json['fields']['storm_bolt_es_num']
                    storm_nimbs_bs = component_json['fields']['storm_nimbs_bs']
                    component_obj = {"id":item_id, "server_id":server_id, "port":port, "type":type, "install_dir":install_dir, "data_dir":data_dir, "log_dir":log_dir, "install_bs":install_bs, "description":None,
                        "db_username":db_username, "db_password":db_password, "web_service_name":web_service_name,
                        "es_memory_limit":es_memory_limit, "es_index_number_of_shards":es_index_number_of_shards,
                        "es_index_refresh_interval":es_index_refresh_interval, "storm_works_num_per_host":storm_works_num_per_host,
                        "storm_dataProcess_works_num":storm_dataProcess_works_num, "storm_dataIndex_works_num":storm_dataIndex_works_num,
                        "storm_spout_config_num":storm_spout_config_num, "storm_spout_dataprocess_num":storm_spout_dataprocess_num,
                        "storm_spout_dataindex_num":storm_spout_dataindex_num, "storm_bolt_default_num":storm_bolt_default_num,
                        "storm_bolt_rule_num":storm_bolt_rule_num, "storm_bolt_advanced_num":storm_bolt_advanced_num,
                        "storm_bolt_kafka_num":storm_bolt_kafka_num, "storm_bolt_es_num":storm_bolt_es_num,"frontend_service_name":frontend_service_name,
                        "es_path_data":es_path_data, "es_path_logs":es_path_logs,"storm_nimbs_bs":storm_nimbs_bs}
                    components.append(component_obj)
                obj['components'] = components
            cluster_server.append(obj)
        cluster_server_dto['cluster_server'] = cluster_server
    return Response(cluster_server_dto)

@api_view(['post'])
def get_single_server_components(request):
    id = request.data['id']
    serverDTO = common.getServerComponents(id)
    return Response(serverDTO)

@api_view(['post'])
def add_single_server_components(request):
    # save components config
    id = request.data['id']
    single_server = server.objects.get(id=id)
    install_bs = single_server.install_bs
    component_bs = False
    single_components = component.objects.filter(server_id=id)
    if single_components!=[] and len(single_components)>0:
        component_bs = True
    else:
        items = request.data['components']
        for item in items:
            component_obj = component(server_id=single_server, type=item['type'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['install_bs'],
                db_username=item['db_username'], db_password=item['db_password'], web_service_name=item['web_service_name'],
                es_memory_limit=item['es_memory_limit'], es_index_number_of_shards=item['es_index_number_of_shards'],
                es_index_refresh_interval=item['es_index_refresh_interval'], storm_works_num_per_host=item['storm_works_num_per_host'],
                storm_dataProcess_works_num=item['storm_dataProcess_works_num'], storm_dataIndex_works_num=item['storm_dataIndex_works_num'],
                storm_spout_config_num =item['storm_spout_config_num'], storm_spout_dataprocess_num=item['storm_spout_dataprocess_num'],
                storm_spout_dataindex_num=item['storm_spout_dataindex_num'], storm_bolt_default_num=item['storm_bolt_default_num'],
                storm_bolt_rule_num=item['storm_bolt_rule_num'], storm_bolt_advanced_num=item['storm_bolt_advanced_num'],
                storm_bolt_kafka_num=item['storm_bolt_kafka_num'], storm_bolt_es_num=item['storm_bolt_es_num'],frontend_service_name=item['frontend_service_name'],
                es_path_data=item['es_path_data'], es_path_logs=item['es_path_logs'],storm_nimbs_bs=item['storm_nimbs_bs'])
            component_obj.save()
    json_data = common.valid_single_server_components(request.data)
    return_data = {'available':True,"id":None, "component_bs":component_bs, "install_bs": install_bs}
    # returnData = {'available':False, 'message':[{"msg":"ZOOKPEER测试消息1"},{"msg":"KAFKA测试消息2"}]}
    if (json_data['available']==False):
        return_data['available'] = False
        warn_obj = warn(server_id=int(id), type="single", msg=json_data['message'])
        warn_obj.save()
        return_data['id'] = warn_obj.id
    else:
        return_data['id'] = id
    return Response(return_data)

@api_view(['post'])
def get_single_warn(request):
    id = request.data['id']
    warnDTO = {"id":id, "msg":None, "server_id":None}
    exist_warn = warn.objects.filter(pk=id)
    if exist_warn!=[] and len(exist_warn)>0:
        json_data = json.loads(serializers.serialize("json", exist_warn))[0]
        warnDTO['msg'] = json_data['fields']['msg'].split(';')
        warnDTO['server_id'] = json_data['fields']['server_id']
    return Response(warnDTO)

@api_view(['post'])
def edit_single_server_components(request):
    id = request.data['id']
    single_server = server.objects.get(id=id)
    install_bs = single_server.install_bs
    items = request.data['components']
    for item in items:
        component.objects.filter(id=item['id']).update(type=item['type'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['install_bs'],
            db_username=item['db_username'], db_password=item['db_password'], web_service_name=item['web_service_name'],
            es_memory_limit=item['es_memory_limit'], es_index_number_of_shards=item['es_index_number_of_shards'],
            es_index_refresh_interval=item['es_index_refresh_interval'], storm_works_num_per_host=item['storm_works_num_per_host'],
            storm_dataProcess_works_num=item['storm_dataProcess_works_num'], storm_dataIndex_works_num=item['storm_dataIndex_works_num'],
            storm_spout_config_num =item['storm_spout_config_num'], storm_spout_dataprocess_num=item['storm_spout_dataprocess_num'],
            storm_spout_dataindex_num=item['storm_spout_dataindex_num'], storm_bolt_default_num=item['storm_bolt_default_num'],
            storm_bolt_rule_num=item['storm_bolt_rule_num'], storm_bolt_advanced_num=item['storm_bolt_advanced_num'],
            storm_bolt_kafka_num=item['storm_bolt_kafka_num'], storm_bolt_es_num=item['storm_bolt_es_num'],frontend_service_name=item['frontend_service_name'],
            es_path_data=item['es_path_data'], es_path_logs=item['es_path_logs'],storm_nimbs_bs=item['storm_nimbs_bs'])
    json_data = common.valid_single_server_components(request.data)
    returnData = {'available':True,"id":None,"install_bs":install_bs}
    # returnData = {'available':False, 'message':[{"msg":"ZOOKPEER测试消息1"},{"msg":"KAFKA测试消息2"}]}
    if (json_data['available']==False):
        returnData['available'] = False
        warn_obj = warn(server_id=int(id), type="single", msg=json_data['message'])
        warn_obj.save()
        returnData['id'] = warn_obj.id
    else:
        returnData['id'] = id
    return Response(returnData)

@api_view(['post'])
def valid_cluster_server_components(request):
    # save components config
    cluster_name = request.data['cluster_name']
    returnData = {'available':True,"id":None}
    json_data = common.valid_cluster_server_components(cluster_name)
    if (json_data['available']==False):
        returnData['available'] = False
        warn_obj = warn(server_id=cluster_name, type="cluster", msg=json_data['message'])
        warn_obj.save()
        returnData['id'] = warn_obj.id
    else:
        returnData['id'] = cluster_name
    return Response(returnData)

@api_view(['post'])
def get_single_server_finish(request):
    id = request.data['id']
    serverComponents = common.getServerComponents(id)
    returnData = common.get_single_server_finish(serverComponents)
    return Response(returnData)

@api_view(['post'])
def get_cluster_server_finish(request):
    cluster_name = request.data['cluster_name']
    returnData = common.get_cluster_server_finish(cluster_name)
    return Response(returnData)

@api_view(['post'])
def add_cluster_server_components(request):
    cluster_name = request.data['cluster_name']
    role = request.data['role']
    ip = request.data['ip']
    hostname = request.data['hostname']
    username = request.data['username']
    password = request.data['password']
    cluster_dto = {"available":False, "cluster_name":cluster_name, "id":None, "message": None}
    existDTO = common.valid_single_server(ip, username, password)
    if(existDTO['available']==True):
        filter_server = server.objects.filter(ip=ip)
        if filter_server!=[] and len(filter_server)>0:
            cluster_dto['message'] = "IP已被使用!"
        else:
            server_obj = server(type='cluster', cluster_name=cluster_name, role=role, ip=ip, hostname=hostname, username=username, password=password)
            server_obj.save()
            items = request.data['components']
            for item in items:
                component_obj = component(server_id=server_obj, type=item['type'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['install_bs'],
                    db_username=item['db_username'], db_password=item['db_password'], web_service_name=item['web_service_name'],
                    es_memory_limit=item['es_memory_limit'], es_index_number_of_shards=item['es_index_number_of_shards'],
                    es_index_refresh_interval=item['es_index_refresh_interval'], storm_works_num_per_host=item['storm_works_num_per_host'],
                    storm_dataProcess_works_num=item['storm_dataProcess_works_num'], storm_dataIndex_works_num=item['storm_dataIndex_works_num'],
                    storm_spout_config_num =item['storm_spout_config_num'], storm_spout_dataprocess_num=item['storm_spout_dataprocess_num'],
                    storm_spout_dataindex_num=item['storm_spout_dataindex_num'], storm_bolt_default_num=item['storm_bolt_default_num'],
                    storm_bolt_rule_num=item['storm_bolt_rule_num'], storm_bolt_advanced_num=item['storm_bolt_advanced_num'],
                    storm_bolt_kafka_num=item['storm_bolt_kafka_num'], storm_bolt_es_num=item['storm_bolt_es_num'],frontend_service_name=item['frontend_service_name'],
                    es_path_data=item['es_path_data'], es_path_logs=item['es_path_logs'],storm_nimbs_bs=item['storm_nimbs_bs'])
                component_obj.save()
            cluster_dto['available'] = True
            cluster_dto['id'] = server_obj.id
    else:
        cluster_dto['message'] = existDTO['message']
    return Response(cluster_dto)

@api_view(['post'])
def edit_cluster_server_components(request):
    id = request.data['id']
    cluster_name = request.data['cluster_name']
    role = request.data['role']
    ip = request.data['ip']
    hostname = request.data['hostname']
    username = request.data['username']
    password = request.data['password']
    cluster_dto = {"available":False, "cluster_name":cluster_name, "id":None, "message": None}
    existDTO = common.valid_single_server(ip, username, password)
    if(existDTO['available']==True):
        server.objects.filter(id=id).update(type='cluster', cluster_name=cluster_name, role=role, ip=ip, hostname=hostname, username=username, password=password)
        items = request.data['components']
        for item in items:
            component.objects.filter(id=item['id']).update(type=item['type'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['install_bs'],
                db_username=item['db_username'], db_password=item['db_password'], web_service_name=item['web_service_name'],
                es_memory_limit=item['es_memory_limit'], es_index_number_of_shards=item['es_index_number_of_shards'],
                es_index_refresh_interval=item['es_index_refresh_interval'], storm_works_num_per_host=item['storm_works_num_per_host'],
                storm_dataProcess_works_num=item['storm_dataProcess_works_num'], storm_dataIndex_works_num=item['storm_dataIndex_works_num'],
                storm_spout_config_num =item['storm_spout_config_num'], storm_spout_dataprocess_num=item['storm_spout_dataprocess_num'],
                storm_spout_dataindex_num=item['storm_spout_dataindex_num'], storm_bolt_default_num=item['storm_bolt_default_num'],
                storm_bolt_rule_num=item['storm_bolt_rule_num'], storm_bolt_advanced_num=item['storm_bolt_advanced_num'],
                storm_bolt_kafka_num=item['storm_bolt_kafka_num'], storm_bolt_es_num=item['storm_bolt_es_num'],frontend_service_name=item['frontend_service_name'],
                es_path_data=item['es_path_data'], es_path_logs=item['es_path_logs'],storm_nimbs_bs=item['storm_nimbs_bs'])
        cluster_dto['available'] = True
        cluster_dto['id'] = id
    else:
        cluster_dto['message'] = existDTO['message']
    return Response(cluster_dto)

@api_view(['post'])
def get_cluster_name(request):
    ip = request.data['ip']
    returnData = {"available":False,"cluster_name":None};
    exist_server = server.objects.filter(type='cluster', ip=ip)
    if exist_server!=[] and len(exist_server)>0:
        returnData['available'] = True
        returnData['cluster_name'] = json.loads(serializers.serialize("json", exist_server))[0]['fields']['cluster_name']
    return Response(returnData)

@api_view(['post'])
def install_single_server(request):
    print 'begin install single server'
    id = request.data['id']
    server.objects.filter(id=id).update(install_bs=True)
    serverComponents = common.getServerComponents(id)
    conf = []
    single_conf = common.generate_conf(serverComponents)
    conf.append(single_conf)
    common.install_components(conf)

@api_view(['post'])
def install_cluster_server(request):
    print 'begin install cluster server'
    cluster_name = request.data['cluster_name']
    server.objects.filter(cluster_name=cluster_name).update(install_bs=True)
    conf = []
    cluster_server = server.objects.filter(cluster_name=cluster_name)
    if cluster_server!=[] and len(cluster_server)>0:
        for item in cluster_server:
            serverComponents = common.getServerComponents(item.id)
            single_conf = common.generate_conf(serverComponents)
            conf.append(single_conf)
    common.install_components(conf)

@api_view(['post'])
def start_stop_server_component(request):
    common.start_stop_server_component(request.data)
    return Response(None)

@api_view(['post'])
def get_single_component_status(request):
    # id = request.data['id']
    dto = common.get_single_server_status(request.data)
    return Response({"dto":dto})

@api_view(['post'])
def get_cluster_component_status(request):
    # cluster_name = request.data['cluster_name']
    dto = common.get_single_server_status(request.data)
    return Response({"dto":dto})

@api_view(['post'])
def get_cluster_server_status(request):
    # cluster_name = request.data['cluster_name']
    dto = common.get_cluster_server_status(request.data)
    return Response({"dto":dto})
