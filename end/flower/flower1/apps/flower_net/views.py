from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class FlowerGoodsViewSets(viewsets.ModelViewSet):
    queryset = FlowerGoods.objects.all()
    serializer_class = FlowerGoodsSerializer
