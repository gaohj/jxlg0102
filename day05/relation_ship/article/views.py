from django.shortcuts import render
from .models import Article,Category
from frontuser.models import FrontUser
from django.http import HttpResponse
# Create your views here.

def index(request):
    # category = Category(name="最火文章")
    # category.save()
    # article = Article(title="你这么可爱,大风把你吹到我怀里",content="我是不会还回去的")
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("SUCCESS")

def one_to_many_view(request):
    # article = Article(title="你不珍惜我，告诉你，过了这个村子，我在下个村子等你", content="我是不会还回去的")
    # category = Category.objects.first()
    # author = FrontUser(username="kangbazi")
    # author.save()
    # article.category = category
    # article.author = author
    #
    # article.save()

    #获取分类下面所有的文章
    # category = Category.objects.first()
    # articles = category.article_set.all() 表名小写_set
    # for article in  articles:
    #     print(article)

    # category = Category.objects.first()
    # articles = category.articles.all() #related_name
    # for article in articles:
    #     print(article)
    category = Category.objects.first()
    article = Article(title="我可以称呼你您么",content="这样你就在我心上了")
    article.author = FrontUser.objects.first()
    #bulk=False 作用是 不需要额外的保存我们article 直接添加就可以
    category.articles.add(article,bulk=False)
    return HttpResponse("一对多SUCCESS")



