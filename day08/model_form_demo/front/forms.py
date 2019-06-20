from django import forms
from .models import Book,User

class AddBookForm(forms.ModelForm):
    #此处省略三个字段
    class Meta:
        model = Book
        fields = "__all__" #应用模型中的所有字段
        # fields = ['title','page'] #应用模型中指定的字段
        #exclude = ['price'] #除了这个字段  模型字段全部用
        error_messages = {
            'page':{
                'required':'请传入page参数',
                'invalid':'请传入一个可用的page参数'
            },
            'title':{
                'max_length':'题目最大长度不能超过100个字符'
            },
            'price':{
                'max_value':'图书价格不能超过1000元'
            }
        }

class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1!=pwd2:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data
    class Meta:
        model = User
        exclude = ['password']