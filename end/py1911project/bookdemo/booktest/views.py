from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Hero


# Create your views here.
# MVT 中的V视图模块
# 在此接受接受请求，处理数据，返回响应

def index(request):
    # return HttpResponse("这里是首页")
    # 1.获取模板
    # template = loader.get_template('index.html')
    # 2.渲染模板数据
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # 3.将渲染结果使用httpresponse返回
    # return HttpResponse(result)
    return render(request, "index.html", {'books': books})


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'book': book})


def jsondata(request):
    return HttpResponse("{'name':'charlie','age':20}")
