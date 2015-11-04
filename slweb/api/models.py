#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class server(models.Model):
    type = models.CharField(max_length=40)
    cluster_name = models.CharField(max_length=128, null=True)
    role = models.CharField(max_length=40, null=True)
    ip = models.CharField(max_length=128)
    hostname = models.CharField(max_length=128, null=True)
    username = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=128, null=True)

class component(models.Model):
    server_id = models.IntegerField()
    type = models.CharField(max_length=40)
    install_dir = models.CharField(max_length=128, null=True)
    data_dir = models.CharField(max_length=128, null=True)
    log_dir = models.CharField(max_length=128, null=True)
    port = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=128, null=True)
    install_bs = models.BooleanField()

class warn(models.Model):
    server_id = models.CharField(max_length=50)
    type = models.CharField(max_length=40)
    msg = models.TextField(null=True)
