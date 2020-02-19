# Charlie
# date:2020/2/19 10:34
# file_name:forms

from django import forms
from .models import User


class LoginForm(forms.Form):
    """
    定义一个登录表单用于生成html登录表单
    """
    username = forms.CharField(max_length=150, min_length=3, label='输入用户名', help_text='用户名最小3，最大150')
    password = forms.CharField(max_length=150, min_length=3, label='输入密码', widget=forms.PasswordInput)


class RegistForm(forms.ModelForm):
    """
    定义一个注册表单用于生成html表单
    """
    password2 = forms.CharField(widget=forms.PasswordInput, label='重复密码')

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': '输入用户名',
            'password': '输入密码'
        }
        help_texts = {
            'username': '长度>3<150',
            'password': '长度>3<150'
        }
        widgets = {
            'password': forms.PasswordInput
        }
