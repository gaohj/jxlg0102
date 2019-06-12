from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("后台首页")
    else:
        # login_url = reverse('cms:login')
        # print("="*50)
        # print(login_url)
        # print("="*50)
        # return redirect(login_url)
        current_namespace = request.resolver_match.namespace
        print(current_namespace)
        return redirect(reverse("%s:login" % current_namespace))
        # login_url = reverse('cms:login')
        # print("="*50)
        # print(login_url)
        # print("="*50)
        # return redirect(login_url)

def login(request):
    return  HttpResponse("后台登陆首页")