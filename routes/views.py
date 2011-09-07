#-*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from xdlinux.routes.models import OS


def index(request,os=""):
    """
    这个是总的主页哦，需要根据不同的访问方式判别，以生成不同的页面，判别的部分放在服务端
    从request中可以独到UserAgent信息，通过这个信息可以判别用户使用的操作系统和浏览器类型

    针对不同的操作系统返回不同的信息

    template为index.html
    """
    return render_to_response('index.html', locals())