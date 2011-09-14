#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from xdlinux.members.models import Member, Group #引入报名成员的CRM，members，具体实现已经完成，请看源文件，注释都写了
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required
def count(request):
    """返回当前已经报名的总人数，直接返回数字就好了，不需要特殊格式"""
    sumcount = '%d' % Member.objects.count()
    if request.is_ajax():
        return HttpResponse(sumcount, mimetype='application/json')
    else:
        return render_to_response('count/count.html',{'sumcount':sumcount})

    
    
def signup(request):
    groups=Group.objects.all()
    if request.method == 'GET':
        return render_to_response('signup.html', {'groups':groups})
    elif request.method == 'POST':
        groups_id = [int(i) for i in request.POST['group'].split(',')]
        groups = Group.objects.filter(id__in= groups_id) 
        try:
            act=False;
            if request.POST['activity']=='true':
                act=True
            newmember = Member.objects.create(name = request.POST['name'], student_num = request.POST['student_num'], self_intro = request.POST['self_intro'], mobile = request.POST['mobile'], twitter_id = request.POST['twitter_id'], email = request.POST['email'], keywords = request.POST['keywords'],activity=act)
            [newmember.groups.add(i) for i in groups]
        except  IntegrityError: # if the student_num is already in database, return a extra error
            return render_to_response('signup.html', {'groups':groups, 'error':1, 'student_num':request.POST['student_num']})
        else:
            #return redirect(request.META['SCRIPT_NAME']+'/success.html')
            #这里纠结一下，用哪种?
            return render_to_response('signup_callback.html', {'id':newmember.id})
