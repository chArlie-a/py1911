from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品名')
    desc = models.CharField(max_length=100, verbose_name='商品描述')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='商品分类', related_name='goods')

    def __str__(self):
        return self.name


class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name='商品展示图')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品', related_name='imgs')

    def __str__(self):
        return self.good.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11, verbose_name='手机号')


class Order(models.Model):
    """
    简单模拟，一个订单只有一个商品，也没有数量
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ManyToManyField(Good, verbose_name='商品')

    def __str__(self):
        return self.user.username + '的订单'


class Verify(models.Model):
    code = models.CharField(max_length=6)
    telephone = models.CharField(max_length=11,unique=True)
    createTime = models.DateTimeField(auto_now_add=True)