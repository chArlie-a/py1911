from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name='部门名')


class Staff(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='所属部门')
