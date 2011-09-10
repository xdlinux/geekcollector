#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from xdlinux.members.models import Member, Group #引入报名成员的CRM，members，具体实现已经完成，请看源文件，注释都写了
from django.db import IntegrityError
from json import dumps

def count(request):
    """返回当前已经报名的总人数，直接返回数字就好了，不需要特殊格式"""
    num = Member.objects.count()
    data ={
    "num":num
    }
    return HttpResponse(dumps(data), mimetype='application/json')
    
def success(request):
    """the page then usr register successfully"""
    return render_to_response('signup_callback.html', locals())
    
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
    groups=Group.objects.all()
    if request.method == 'GET':
        return render_to_response('signup.html', {'groups':groups})
    elif request.method == 'POST':
        groups_id = [int(i) for i in request.POST['group'].split(',')]
        groups = Group.objects.filter(id__in= groups_id) 
        try:
            newmember = Member.objects.create(name = request.POST['name'], student_num = request.POST['student_num'], self_intro = request.POST['self_intro'], mobile = request.POST['mobile'], twitter_id = request.POST['twitter_id'], email = request.POST['email'], keywords = request.POST['keywords'],)
            [newmember.groups.add(i) for i in groups]
        except  IntegrityError: # if the student_num is already in database, return a extra error
            return render_to_response('signup.html', {'groups':groups, 'error':1, 'student_num':request.POST['student_num']})
        else:
            return redirect('/success/')

