from django import forms
from django.core import validators
from .models import User
class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100,min_length=6,label="标题",error_messages={"min_length":"最少不能少于6个字符"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"必须要写content这个字段"})
    email = forms.EmailField(label="邮箱",error_messages={"required":"必须要传email字段"})
    reply = forms.BooleanField(required=False,label="是否回复")


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确格式的邮箱")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message="请输入正确格式的手机号码")])
    pwd1 = forms.CharField(max_length=20,min_length=6)
    pwd2 = forms.CharField(max_length=20,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s:已经注册" % telephone)
        return telephone
    #如果走到这里 说明所有的字段都验证成功了
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data
