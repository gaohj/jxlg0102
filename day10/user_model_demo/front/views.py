from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
# Create your views here.
from .models import Person

def index(request):
    #user = User.objects.create_user(username='jxlg6',email='jxlg@126.com',password='12qwaszx')
    # user = User.objects.create_superuser(username='jxlg888',email='jxlg8@126.com',password='12qwaszx')
    # user.save()
    # user = User.objects.get(pk=1)
    # user.set_password('qweasdzxc01!')
    username='jxlg6'
    password='12qwaszx'
    user = authenticate(request,username=username,password=password)
    if user:
        print('登录成功',user.username)
    else:
        print('用户名或者密码错误')
    return HttpResponse("OK")

def proxys(request):
    balcklists = Person.get_balck_list()
    for balcklist in balcklists:
        print(balcklist)
    return HttpResponse('proxy')