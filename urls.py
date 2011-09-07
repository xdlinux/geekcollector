#-*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, include, url
from xdlinux.routes.views import index
from xdlinux.members.views import *
from django.conf.urls.static import static
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xdl.views.home', name='home'),
    # url(r'^xdl/', include('xdl.foo.urls')),
    url(r'^count$',count), #这个url返回当前已经报名的人数
    url(r'^signup$',signup), #这个url引导到登陆页面
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\w+)$',index), #这个url返回主页面，主页面上有对社区的简要介绍，也有针对不同系统登陆的不同信息

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
