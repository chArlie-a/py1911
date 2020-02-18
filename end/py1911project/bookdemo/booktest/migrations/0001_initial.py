# Generated by Django 3.0.3 on 2020-02-18 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('regist_date', models.DateField(auto_now_add=True, verbose_name='注册日期')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='文章标题')),
                ('summary', models.TextField(verbose_name='文章正文')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0)),
                ('pub_date', models.DateField(default='1983-06-01')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
            ],
            options={
                'verbose_name': '用户模型类A',
                'verbose_name_plural': '用户模型类B',
                'db_table': '用户类',
                'ordering': ['-telephone'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=10, verbose_name='标签名')),
                ('articles', models.ManyToManyField(related_name='tags', to='booktest.Article', verbose_name='文章')),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6)),
                ('content', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Concact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('email', models.EmailField(default='335176033@qq.com', max_length=254)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='con', to='booktest.Account')),
            ],
        ),
    ]
