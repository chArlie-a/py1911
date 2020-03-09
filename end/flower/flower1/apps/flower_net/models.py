from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')
    img = models.ImageField(upload_to='category_ads', verbose_name='分类图片')

    def __str__(self):
        return self.name


SEX = (('女', 'Female'), ('男', 'Male'),)


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='用户名')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    telephone = models.CharField(max_length=11, verbose_name='手机号')
    headImg = models.ImageField(upload_to='head/', verbose_name='头像')
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='性别')
    berthday = models.DateField(null=True, blank=True, verbose_name='生日')

    def __str__(self):
        return self.name


class Comment(models.Model):
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    img = UEditorField(imagePath='img/', width='100%', verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.commentator.name


class FlowerGoods(models.Model):
    name = models.CharField(max_length=30, verbose_name='鲜花名字')
    price = models.PositiveIntegerField(default=0, verbose_name='价格')
    sales = models.FloatField(max_length=20, default=1.1, verbose_name='销量')
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name='描述')
    materials = models.CharField(max_length=30, verbose_name='材料')
    img = models.ImageField(upload_to='ads', verbose_name='图片')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类名')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='评论')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')
    distribution = models.CharField(max_length=20, default='全国')

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='用户')
    goods = models.ForeignKey(FlowerGoods, on_delete=models.CASCADE, verbose_name='商品')
