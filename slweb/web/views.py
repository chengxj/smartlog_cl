#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

def statement(request):
    return render_to_response("statement.html",context_instance=RequestContext(request))

def finish(request):
    return render_to_response("finish.html",context_instance=RequestContext(request))

def host(request):
    return render_to_response("host.html",context_instance=RequestContext(request))

def alarm(request):
    return render_to_response("alarm.html",context_instance=RequestContext(request))

def danji(request):
    return render_to_response("danji.html",context_instance=RequestContext(request))

def jiqun(request):
    return render_to_response("jiqun.html",context_instance=RequestContext(request))

def jiqun_management(request):
    return render_to_response("jiqun_management.html",context_instance=RequestContext(request))

def index(request):
    return render_to_response("in.html",context_instance=RequestContext(request))

def component_selection(request):
    return render_to_response("component_selection.html",context_instance=RequestContext(request))
