# Generated by Django 3.0.3 on 2020-02-25 01:45

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads', verbose_name='图片')),
                ('desc', models.CharField(blank=True, max_length=20, null=True, verbose_name='图片描述')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='颜色名字')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='尺寸名')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品名')),
                ('desc', DjangoUeditor.models.UEditorField(verbose_name='描述')),
                ('price', models.FloatField(max_length=20, verbose_name='价格')),
                ('brand', models.CharField(default='IKEA', max_length=20, verbose_name='品牌')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('views', models.PositiveIntegerField(default=0, max_length=20, verbose_name='浏览量')),
                ('amount', models.PositiveIntegerField(default=0, max_length=20, verbose_name='数量')),
                ('trim_size', models.CharField(default='1000*1000*1000', max_length=30, verbose_name='实际尺寸')),
                ('weight', models.FloatField(max_length=20, verbose_name='重量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IKEAapp.Category', verbose_name='分类')),
                ('color', models.ManyToManyField(to='IKEAapp.Color', verbose_name='商品颜色')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IKEAapp.Ads', verbose_name='商品图片')),
                ('size', models.ManyToManyField(to='IKEAapp.Size', verbose_name='大小')),
                ('tags', models.ManyToManyField(to='IKEAapp.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='评论人')),
                ('email', models.EmailField(default='335176033@qq.com', max_length=254, verbose_name='个人邮箱')),
                ('body', DjangoUeditor.models.UEditorField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IKEAapp.Commodity', verbose_name='所属商品')),
            ],
        ),
    ]