from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    p = Person('CXK')

    # context = {
    #     'person':p
    # }
    # context = {
    #     'person':{
    #         'username':'kangbazi'
    #     }
    # }
    # context = {
    #     'person': (
    #         'nidaqiu cxk',
    #         'fj',
    #         'sc'
    #     )
    # }
    # context = {
    #     'age':16
    # }
    # context = {
    #     'heros':[
    #         '乔丹',
    #         '科比',
    #         '林青霞',
    #         'cxk',
    #     ]
    # }

    # context = {
    #     'persons':{
    #         'username':'cxk',
    #         'age':18,
    #         'height':'171cm',
    #     }
    # }
    # context = {
    #     'persons':[
    #         '水浒传',
    #         '红楼梦',
    #         '三国'
    #     ]
    # }

    # context = {
    #     'comments':[
    #         '你打球像cxk'
    #     ],
    #     'books':[
    #         {
    #             'name':'python深入浅出',
    #             'author':'扛把子',
    #             'price':200
    #         },
    #         {
    #             'name': 'mysql从入门到放弃',
    #             'author': '扛把子1',
    #             'price': 100
    #         },
    #         {
    #             'name': 'Linux从希望到绝望',
    #             'author': '扛把子2',
    #             'price': 150
    #         },
    #         {
    #             'name': '离散数学从懵逼到彻底懵逼',
    #             'author': '扛把子3',
    #             'price': 100
    #         },
    #         {
    #             'name': 'JavaScript10年刚刚入门',
    #             'author': '扛把子4',
    #             'price': 130
    #         },
    #     ]
    # }

    # context = {
    #     'persons':[
    #         '张三',
    #         '里斯',
    #         '王五'
    #     ]
    # }
    context = {
        "info":"<script>alert('test')</script>"
    }
    return render(request,'index.html',context=context)