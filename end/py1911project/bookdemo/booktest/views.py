from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# MVT 中的V视图模块
# 在此接受接受请求，处理数据，返回响应

def index(request):
    return HttpResponse("这里是首页")

def jsondata(request):
    return HttpResponse("{'name':'charlie','age':20}")
