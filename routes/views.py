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
    s_root = request.META['SCRIPT_NAME']
    if os=="":
        ua=request.META['HTTP_USER_AGENT']
        #if re.search(r'Macintosh',ua):
          #  return redirect('/apple/')
        if re.search(r'(Chrome|chromium)',ua,re.I):
            return redirect( s_root+'/chrome/' )
        if re.search(r'Safari',ua,re.I):
            return redirect( s_root+'/webkit/' )
        if re.search(r'Firefox',ua,re.I) and re.search(r'Gecko',ua,re.I):
            return redirect( s_root+'/firefox/')
        if re.search(r'Opera',ua,re.I) and re.search(r'Presto',ua,re.I):
            return redirect( s_root+'/opera/')
        if re.search(r'linux',ua,re.I):
            return redirect( s_root+'/linux/')
    elif os=="random":
        route=OS.objects.order_by('?').all()[0]
    else:
        try:
            route=OS.objects.get(tag=os)
        except Exception, e:
            return redirect( s_root+'/falone/')
    return render_to_response('index.html', {'os':route,'s_root':s_root})
