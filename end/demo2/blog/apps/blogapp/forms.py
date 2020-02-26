# Charlie
# date:2020/2/21 17:48
# file_name:forms
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'url', 'email', 'body']
        labels = {
            'name': '输入名字',
            'url': '输入主页',
            'email': '输入邮箱',
            'body': '输入正文'
        }
        widgets = {
            'body':forms.Textarea()
        }
