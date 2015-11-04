#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import *

class serverSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField(required=True, max_length=40)
    cluster_name = serializers.CharField(required=False, max_length=128)
    role = serializers.CharField(required=False, max_length=40)
    ip = serializers.CharField(required=True, max_length=128)
    hostname = serializers.CharField(required=True, max_length=128)
    username = serializers.CharField(required=True, max_length=128)
    password = serializers.CharField(required=True, max_length=128)
    description = serializers.CharField(required=False, max_length=128)

    def create(self, validated_data):
        return server.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `server` instance, given the validated data.
        """
        instance.type = validated_data.get('type', instance.type)
        instance.cluster_name = validated_data.get('cluster_name', instance.cluster_name)
        instance.role = validated_data.get('role', instance.role)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.hostname = validated_data.get('hostname', instance.hostname)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
