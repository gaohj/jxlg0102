from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse
from frontuser.models import FrontUser
# Create your views here.

def index(request):
    # category = Category(name="伦理动作")
    # category.save()
    # article = Article(title="人生苦短,我用python",content="java100行代码，python可能只需要五行")
    # article.category =category
    # article.save()
    # article = Article.objects.first()
    # print(article.category.name)
    return HttpResponse("成功")

def one_to_many_view(request):
    # article = Article(title="论屌丝的逆袭",content="我一点也不想你，一点半再想")
    # category = Category.objects.first()
    # frontUser = FrontUser(username="kangbazi")
    # frontUser.save()
    # article.category = category
    # article.author = frontUser
    # article.save()
    # return HttpResponse("成功")
    #获取分类下面所有的文章
    # category = Category.objects.first()
    # article = category.article_set.first() #当你在外键 不写,related_name="articles" 使用模型的小写_set 获取 一下面所有的多
    # print(article)
    # category = Category.objects.first()
    # articles = category.articles.all()#articles 就是我们在model中写的related_name
    # for article in  articles:
    #     print(article)
    category = Category.objects.first()
    article = Article(title="三国演义",content="既生瑜何生亮")
    article.author = FrontUser.objects.first()
    category.articles.add(article,bulk=False)
    return HttpResponse("成功")
