from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    ads = Ads.objects.all()
    commodity = Commodity.objects.all()

    return render(request, 'index.html', {"ads": ads, 'commodity': commodity})


def shop(request):
    return render(request, 'shop.html')


def favicon(request):
    return redirect(to='/static/img/favicon.ico')
