from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Page, Paginator


# Create your views here.
def index(request):
    ads = Ads.objects.all()
    articles = Article.objects.all()
    # 实现一页2篇文章
    paginator = Paginator(articles, 2)
    num = request.GET.get('pagenum', 1)
    print(paginator)
    page = paginator.get_page(num)
    return render(request, 'index.html', {'ads': ads, 'page': page})


def detail(request, pid):
    return render(request, 'single.html')


def contact(request):
    return render(request, 'contact.html')


def favicon(request):
    return redirect(to='/static/favicon.ico')
