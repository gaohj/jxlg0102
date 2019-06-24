from django.shortcuts import render,reverse,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
# from .models import Person
from .models import User
from .forms import LoginForm

def index(request):
    #user = User.objects.create_user(username='jxlg4',email='jxlg4@126.com',password='12qwaszx')
    # user = User.objects.create_superuser(username='jxlg888',email='jxlg8@126.com',password='12qwaszx')
    #user.save()
    # user = User.objects.get(pk=1)
    # user.set_password('qweasdzxc01!')
    # username='jxlg6'
    # password='12qwaszx'
    # user = authenticate(request,username=username,password=password)
    # if user:
    #     print('登录成功',user.username)
    # else:
    #     print('用户名或者密码错误')
    return HttpResponse("OK")

# def proxys(request):
#     balcklists = Person.get_balck_list()
#     for balcklist in balcklists:
#         print(balcklist)
#     return HttpResponse('proxy')

def my_authenticate(telephone,password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None

def one_view(request):
    print('kangbazi')
    #user = User.objects.create_user(username='kangbazi',email='kangbazi@qq.com',password='123456')
    # user = User.objects.create_user(username='kangbazi6',email='kangbazi6@qq.com',password='123456')
    # user.extension.telephone = '1377777777'
    # user.extension.school = '清华大学'
    # user.save()
    telephone = request.GET.get('telephone')
    print(telephone)
    password = request.GET.get('password')
    user = my_authenticate(telephone,password)
    if user:
        print("%s 验证成功" % user.username)
    else:
        print('验证失败')
    return HttpResponse('一对一扩展模型')


def inherit_view(request):
    # telephone = '13888888888'
    # password = '123456'
    # username = 'kangbazi'
    # email = 'kangbazi@126.com'
    # school = '江西理工大学'
    # user = User.objects.create_user(telephone='18888888888',username='kangbazi',password='123456',email='123@qq.com')
    # user.save()
    user = authenticate(request,username='18888888888',password='123456')
    if user:
        print('%s验证成功'% user.username)
    else:
        print('验证失败')

    return HttpResponse('模型继承')

def my_login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')

            user = authenticate(request,username=telephone,password=password)

            if user and user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse("手机号或者密码错误")
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))

def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required(login_url='/login/')
def profiles(request):
    return HttpResponse("我是个人中心,登录成功以后才可以查看")

