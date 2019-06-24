from .models import  User
from django.contrib.auth.models import User
#get_response 是个方法
def front_user_middleware(get_response):
    print("这里是中间件初始化的一些代码 ")
    def middleware(request):
        print("这里是request到达view 之前的代码")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None


        response = get_response(request) #这是一个界限之前是request到
        #view之前
        #之后的代码是 response对象到达浏览器
        print("这里是response到达浏览器执行的代码")
        return response
    return middleware