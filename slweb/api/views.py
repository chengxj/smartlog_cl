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
def valid_single_server(request):
    ip = request.data['ip']
    username = request.data['username']
    password = request.data['password']
    print ip, username, password
    serverDTO = {"available":False, "id":None, "message":None, "db_bs":False}
    exist_server = server.objects.filter(type='single', ip=ip, username=username, password=password)
    if exist_server!=[] and len(exist_server)>0:
        serverDTO['available'] = True
        serverDTO['db_bs'] = True
        serverDTO['id'] = json.loads(serializers.serialize("json", exist_server))[0]['pk']
    else:
        existDTO = common.test_valid_single_server(ip, username, password)
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
        cluster_server = []
        for item in json_data:
            obj = {"id":None, "ip":"","username":"","password":"","hostname":"","role":"","components":None}
            obj['ip'] = item['fields']['ip']
            obj['username'] = item['fields']['username']
            obj['password'] = item['fields']['password']
            obj['hostname'] = item['fields']['hostname']
            obj['role'] = item['fields']['role']
            obj['id'] = item['pk']
            cluster_server.append(obj)
        cluster_server_dto['cluster_server'] = cluster_server
    return Response(cluster_server_dto)

@api_view(['post'])
def get_single_server_components(request):
    id = request.data['id']
    serverDTO = getServerComponents(id)
    # serverDTO = {"id":id, "hostname":None, "ip":None, "username":None, "password":None, "components":[]}
    # exist_server = server.objects.filter(pk=id)
    # if exist_server!=[] and len(exist_server)>0:
    #     json_data = json.loads(serializers.serialize("json", exist_server))[0]
    #     serverDTO['hostname'] = json_data['fields']['hostname']
    #     serverDTO['ip'] = json_data['fields']['ip']
    #     serverDTO['username'] = json_data['fields']['username']
    #     serverDTO['password'] = json_data['fields']['password']
    #     exist_components = component.objects.filter(server_id=id)
    #     if exist_components!=[] and len(exist_components)>0:
    #         json_components = json.loads(serializers.serialize("json", exist_components))
    #         for item in json_components:
    #             item_id = item['pk']
    #             server_id = id
    #             type = item['fields']['type']
    #             install_dir = item['fields']['install_dir']
    #             data_dir = item['fields']['data_dir']
    #             log_dir = item['fields']['log_dir']
    #             install_bs = item['fields']['install_bs']
    #             port = item['fields']['port']
    #             component_obj = {"id":item_id, "server_id":server_id, "port":port, "type":type, "install_dir":install_dir, "data_dir":data_dir, "log_dir":log_dir, "install_bs":install_bs, "description":None}
    #             serverDTO['components'].append(component_obj)
    return Response(serverDTO)

@api_view(['post'])
def valid_single_server_components(request):
    # save components config
    id = request.data['id']
    items = request.data['components']
    for item in items:
        component_obj = component(server_id=int(id), type=item['name'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['type'])
        component_obj.save()
    json_data = common.test_valid_single_server_components(request.data)
    returnData = {'available':True,"id":None}
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
def valid_esingle_server_components(request):
    # save components config
    id = request.data['id']
    items = request.data['components']
    for item in items:
        component.objects.filter(id=item['id']).update(server_id=int(id), type=item['name'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['type'])
    json_data = common.test_valid_single_server_components(request.data)
    returnData = {'available':True,"id":None}
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
    json_data = common.test_valid_cluster_server_components(cluster_name)
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
    serverComponents = getServerComponents(id)
    returnData = common.test_get_single_server_finish(serverComponents)
    return Response(returnData)

@api_view(['post'])
def get_cluster_server_finish(request):
    cluster_name = request.data['cluster_name']
    returnData = common.test_get_cluster_server_finish(cluster_name)
    return Response(returnData)

@api_view(['post'])
def add_cluster_server_components(request):
    cluster_name = request.data['cluster_name']
    role = request.data['role']
    ip = request.data['ip']
    hostname = request.data['hostname']
    username = request.data['username']
    password = request.data['password']
    server_obj = server(type='cluster', cluster_name=cluster_name, role=role, ip=ip, hostname=hostname, username=username, password=password)
    server_obj.save()
    items = request.data['components']
    for item in items:
        component_obj = component(server_id=server_obj.id, type=item['name'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['type'])
        component_obj.save()
    cluster_dto = {"available":True, "cluster_name":cluster_name, "id":server_obj.id}
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
    server.objects.filter(id=id).update(type='cluster', cluster_name=cluster_name, role=role, ip=ip, hostname=hostname, username=username, password=password)
    items = request.data['components']
    for item in items:
        component.objects.filter(id=item['id']).update(server_id=int(id), type=item['name'], port=item['port'], install_dir=item['install_dir'], data_dir=item['data_dir'], log_dir=item['log_dir'], install_bs=item['type'])
    cluster_dto = {"available":True, "cluster_name":cluster_name, "id":id}
    return Response(cluster_dto)

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
                component_obj = {"id":item_id, "server_id":server_id, "port":port, "type":type, "install_dir":install_dir, "data_dir":data_dir, "log_dir":log_dir, "install_bs":install_bs, "description":None}
                serverDTO['components'].append(component_obj)
    return serverDTO
