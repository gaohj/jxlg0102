"""classview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index,name='index'),
    path('book/', views.BookListView.as_view(),name='book'),
    path('add_book/', views.AddBookView.as_view(),name='add_book'),
    # path('about/',views.AboutView.as_view())
    path('about/',TemplateView.as_view(template_name='about.html'))
    #TemplateView 不写 类视图 可以直接让用户看到页面  前提是不需要传递任何的参数
    #如果传参数 就需要 再写类视图
]
