"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.conf.urls.static import static
import settings
from django.contrib import admin
from web.views import *
from api.views import *

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', statement),
    url(r'^index', index),
    url(r'^single_component_status', single_component_status),
    url(r'^single_component', new_single_component),
    url(r'^single_finish', single_finish),
    url(r'^single_alarm', single_alarm),
    url(r'^single', single),
    url(r'^edit_single_component', edit_single_component),
    url(r'^edit_cluster_component', edit_cluster_component),
    url(r'^new_cluster_component', new_cluster_component),
    url(r'^new_cluster', new_cluster),
    url(r'^cluster_host', cluster_host),
    url(r'^cluster_finish', cluster_finish),
    url(r'^cluster_alarm', cluster_alarm),
    url(r'^cluster_management', cluster_management),
    url(r'^cluster', cluster),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/edit_single_server_components', edit_single_server_components, name='edit-esingle-server-components'),
    url(r'^api/add_single_server_components', add_single_server_components, name='add-single-server-components'),
    url(r'^api/valid_cluster_server_components', valid_cluster_server_components, name='valid_cluster_server_components'),
    url(r'^api/add_single_server', add_single_server, name='add-single-server'),
    url(r'^api/get_cluster_server_components', get_cluster_server_components, name='get-cluster-server-components'),
    url(r'^api/get_cluster_server_finish', get_cluster_server_finish, name='get-cluster-server-finish'),
    url(r'^api/get_cluster_name', get_cluster_name, name='get-cluster-name'),
    url(r'^api/get_single_server_finish', get_single_server_finish, name='get-single-server-finish'),
    url(r'^api/get_single_server_components', get_single_server_components, name='get-single-server=components'),
    url(r'^api/get_single_server', get_single_server, name='get-single-server'),
    url(r'^api/get_single_warn', get_single_warn, name='get-single-warn'),
    url(r'^api/add_cluster_server_components', add_cluster_server_components, name='add-cluster-server-components'),
    url(r'^api/edit_cluster_server_components', edit_cluster_server_components, name='edit-cluster-server-components'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',) + static(settings.MEDIA_URL, document_root=settings.STATIC_DOC_ROOT)
