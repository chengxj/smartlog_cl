#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def statement(request):
    return render_to_response("statement.html",context_instance=RequestContext(request))

def single_finish(request):
    id =  request.GET.get('id', None)
    return render_to_response("single_finish.html", {'id':id}, context_instance=RequestContext(request))

def cluster_finish(request):
    cluster_name =  request.GET.get('cluster_name', None)
    return render_to_response("cluster_finish.html", {'cluster_name':cluster_name}, context_instance=RequestContext(request))

def cluster_host(request):
    return render_to_response("cluster_host.html",context_instance=RequestContext(request))

def single_alarm(request):
    id =  request.GET.get('id', None)
    return render_to_response("single_alarm.html", {'id':id}, context_instance=RequestContext(request))

def cluster_alarm(request):
    id =  request.GET.get('id', None)
    return render_to_response("cluster_alarm.html", {'id':id},context_instance=RequestContext(request))

def single(request):
    return render_to_response("single.html",context_instance=RequestContext(request))

def cluster(request):
    return render_to_response("cluster.html",context_instance=RequestContext(request))

def new_cluster(request):
    cluster_name =  request.GET.get('cluster_name', None)
    return render_to_response("new_cluster.html", {'cluster_name':cluster_name}, context_instance=RequestContext(request))

def cluster_management(request):
    cluster_name =  request.GET.get('cluster_name', None)
    return render_to_response("cluster_management.html", {'cluster_name':cluster_name}, context_instance=RequestContext(request))

def index(request):
    return render_to_response("index.html",context_instance=RequestContext(request))

def component_selection(request):
    return render_to_response("component_selection.html",context_instance=RequestContext(request))

def edit_cluster_component(request):
    id =  request.GET.get('id', None)
    return render_to_response("edit_cluster_component.html",{'id':id}, context_instance=RequestContext(request))

def cluster_component_status(request):
    id =  request.GET.get('id', None)
    return render_to_response("cluster_component_status.html", {'id':id}, context_instance=RequestContext(request))

def new_cluster_component(request):
    # print server id
    cluster_name =  request.GET.get('cluster_name', None)
    role =  request.GET.get('role', None)
    print cluster_name
    return render_to_response("new_cluster_component.html",{'cluster_name':cluster_name,'role':role}, context_instance=RequestContext(request))

def new_single_component(request):
    # print server id
    id =  request.GET.get('id', None)
    print id
    return render_to_response("new_single_component.html",{'id':id}, context_instance=RequestContext(request))
    # return render_to_response("component_selection.html",{'id':id}, context_instance=RequestContext(request))

def edit_single_component(request):
    # print server id
    id =  request.GET.get('id', None)
    return render_to_response("edit_single_component.html",{'id':id}, context_instance=RequestContext(request))

def single_component_status(request):
    # print server id
    id =  request.GET.get('id', None)
    return render_to_response("single_component_status.html",{'id':id}, context_instance=RequestContext(request))
