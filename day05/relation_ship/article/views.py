from django.shortcuts import render
from .models import Article,Category,Tag
from frontuser.models import FrontUser,UserExtension
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
def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school="五道口职业学院")
    #
    # extension.user = user
    # extension.save()
    extension = UserExtension.objects.first()
    print(extension.user)

    user = FrontUser.objects.first()
    extensions = user.extension
    print(extensions)
    return HttpResponse("一对一成功")

def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name="人生苦短，我用Python")
    # tag.save()
    # article.tag_set.add(tag)

    # article = Article.objects.first()
    # tag = Tag(name="Python搜索指数绝对的第一")
    # tag.save()
    # article.tags.add(tag)


    # tag = Tag.objects.get(pk=2)
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    # 标签下面的文章
    article = Article.objects.get(pk=1)
    tags = article.tags.all()
    for tag in  tags:
        print(tag)

    return HttpResponse("多对多成功")


