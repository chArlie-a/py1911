from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *


# Create your views here.
class DepartmentViewSets(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StaffViewSets(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
