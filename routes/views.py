#-*- coding: UTF-8 -*-

from django.shortcuts import render_to_response,redirect
from xdlinux.routes.models import OS
import re


def index(request,os=""):
    """
    这个是总的主页哦，需要根据不同的访问方式判别，以生成不同的页面，判别的部分放在服务端
    从request中可以独到UserAgent信息，通过这个信息可以判别用户使用的操作系统和浏览器类型

    针对不同的操作系统返回不同的信息

    template为index.html
    """
    if os=="":
        ua=request.META['HTTP_USER_AGENT']
        #if re.search(r'Macintosh',ua):
          #  return redirect('/apple/')
        if re.search(r'(Chrome|chromium)',ua,re.I):
            return redirect('/chrome/')
        if re.search(r'Safari',ua,re.I):
            return redirect('/webkit/')
        if re.search(r'Firefox',ua,re.I) and re.search(r'Gecko',ua,re.I):
            return redirect('/firefox/')
        if re.search(r'Opera',ua,re.I) and re.search(r'Presto',ua,re.I):
            return redirect('/opera/')
        if re.search(r'linux',ua,re.I):
            return redirect('/linux/')
        try:
            OS.objects.get(tag=os)
        except Exception, e:
            return redirect('/geek/')
    return render_to_response('index.html', {'os':os})
