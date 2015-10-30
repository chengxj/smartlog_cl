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
from web import views

urlpatterns = [
    url(r'^$', views.statement),
    url(r'^index/', views.index),
    url(r'^single/', views.danji),
    url(r'^cluster/', views.jiqun),
    url(r'^alarm/', views.alarm),
    url(r'^single_component/', views.component_selection),
    url(r'^finish/', views.finish),
    url(r'^host/', views.host),
    url(r'^cluster_management/', views.jiqun_management),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns('',) + static(settings.MEDIA_URL, document_root=settings.STATIC_DOC_ROOT)
