#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from xdlinux.members.models import Member, Group #引入报名成员的CRM，members，具体实现已经完成，请看源文件，注释都写了

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
    if request.method == 'GET':
        groups=Group.objects.all()
        return render_to_response('signup.html', {'groups':groups})
    elif request.method == 'POST':
        group_id = int(request.POST['groups'])
        group = Group.objects.get(id = group_id)
        Member.objects.create(name = request.POST['name'], student_num = request.POST['student_num'], mobile = request.POST['mobile'],email = request.POST['email'], groups= group, keywords = request.POST['keywords'],)
<<<<<<< HEAD
        num = len(Member.objects.all())
        return render_to_response('signup_callback.html', locals()) #用locals()可以直接将当前环境中所有的变量传入
=======
        num = Member.objects.count()
        return render_to_response('signup_callback.html', {'num':num})
>>>>>>> change the len() fund to .count method
