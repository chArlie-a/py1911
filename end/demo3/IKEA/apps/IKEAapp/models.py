from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class Ads(models.Model):
    img = models.ImageField(upload_to='ads', verbose_name='图片')
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name='图片描述')

    def __str__(self):
        return self.desc


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='颜色名字')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='尺寸名')

    def __str__(self):
        return self.name


class Commodity(models.Model):
    name = models.CharField(max_length=20, verbose_name='商品名')
    img = models.ManyToManyField(Ads, verbose_name='商品图片')
    desc = UEditorField(imagePath='img/', width='100%', verbose_name='描述')
    color = models.ManyToManyField(Color, verbose_name='商品颜色')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag)
    price = models.FloatField(max_length=20, verbose_name='价格')
    brand = models.CharField(max_length=20, default='IKEA', verbose_name='品牌')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    views = models.PositiveIntegerField(max_length=20, default=0, verbose_name='浏览量')
    size = models.ManyToManyField(Size, verbose_name='大小')
    amount = models.PositiveIntegerField(max_length=20, default=0, verbose_name='数量')
    trim_size = models.CharField(max_length=30, default='1000*1000*1000', verbose_name='实际尺寸')
    weight = models.FloatField(max_length=20, verbose_name='重量')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='评论人')
    email = models.EmailField(default='335176033@qq.com', verbose_name='个人邮箱')
    body = UEditorField(imagePath='img/', width='100%', verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, verbose_name='所属商品')

    def __str__(self):
        return self.name
