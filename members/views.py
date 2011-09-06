#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from xdlinux.members.models import Member #引入报名成员的CRM，members，具体实现已经完成，请看源文件，注释都写了

def count(request):
    """返回当前已经报名的总人数，直接返回数字就好了，不需要特殊格式"""

def signup(request):
    """
    渲染报名表的view，并处理报名表单的提交
    表单比较简单，因此不再使用django的表单

    表单验证方面，畜松帮我寻找一下有没有好的jquery验证神马的就好

    用render_to_response可以直接渲染模板
    signup.html是一开始呈现的页面
    signup_callback.html 是提交表单且通过之后的反馈页面，需要显示当前是第几个报名的

    记得GET和POST分开处理哦~
    """
