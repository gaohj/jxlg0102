from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        # login_url = reverse('front:login')+ "?next=/"
        login_url = reverse('front:detail',kwargs={"article_id":1,"p":6})
        print("="*50)
        print(login_url)
        print("="*50)
        return redirect(login_url)


def login(request):
    return  HttpResponse("登陆首页")


def article_detail(request,article_id,p):
    text = "您要查看的文章详情id是:%s,第%s 页" % (article_id,p)
    return HttpResponse(text)