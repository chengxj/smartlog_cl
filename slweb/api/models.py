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
    db_username = models.CharField(max_length=128, null=True)
    db_password = models.CharField(max_length=128, null=True)
    web_service_name = models.CharField(max_length=128, null=True)
    frontend_service_name = models.CharField(max_length=128, null=True)
    es_memory_limit = models.CharField(max_length=128, null=True)
    es_index_number_of_shards = models.CharField(max_length=128, null=True)
    es_index_refresh_interval = models.CharField(max_length=128, null=True)
    storm_works_num_per_host = models.CharField(max_length=128, null=True)
    storm_dataProcess_works_num = models.CharField(max_length=128, null=True)
    storm_dataIndex_works_num = models.CharField(max_length=128, null=True)
    storm_spout_config_num = models.CharField(max_length=128, null=True)
    storm_spout_dataprocess_num = models.CharField(max_length=128, null=True)
    storm_spout_dataindex_num = models.CharField(max_length=128, null=True)
    storm_bolt_default_num = models.CharField(max_length=128, null=True)
    storm_bolt_rule_num = models.CharField(max_length=128, null=True)
    storm_bolt_advanced_num = models.CharField(max_length=128, null=True)
    storm_bolt_kafka_num = models.CharField(max_length=128, null=True)
    storm_bolt_es_num = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=128, null=True)
    install_bs = models.BooleanField()

class warn(models.Model):
    server_id = models.CharField(max_length=50)
    type = models.CharField(max_length=40)
    msg = models.TextField(null=True)
