from django.db import models
from django.contrib.auth.models import User
from django.core import validators
# Create your models here.

#User.objects.all()
#Person.onjects.all() 等价的  因为person 是一个代理模型自己没什么实权 用的全是User的

class Person(User):
    telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}')])
    class Meta:
        proxy=True #这里用来指定这是一个代理模型


    @classmethod  #表示这是一个类方法
    def get_balck_list(cli):
        return cli.objects.filter(is_active=False)


