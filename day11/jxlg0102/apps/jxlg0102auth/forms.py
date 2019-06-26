from  django import forms
from apps.forms import FormMixin
from django.core import validators
from django.core.cache import cache
from .models import User

class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}',message="请输入正确的手机号")])
    password = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能30位","min_length":"密码最短不能少于6位"})
    remember = forms.IntegerField(required=False)

class RegisterForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}', message="请输入正确的手机号")])
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=30, min_length=6,
                               error_messages={"max_length": "密码最多不能30位", "min_length": "密码最短不能少于6位"})
    password2 = forms.CharField(max_length=30, min_length=6,
                               error_messages={"max_length": "密码最多不能30位", "min_length": "密码最短不能少于6位"})
    img_captcha = forms.CharField(min_length=4,max_length=6)
    sms_captcha = forms.CharField(min_length=4,max_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1= cleaned_data.get("password1")
        password2= cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("两次密码输入不一致")

        # text = cleaned_data.get('captcha')
        # cache.get(text.lower())

        return cleaned_data