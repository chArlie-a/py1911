"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 路由地址 每一个网址均需要绑定视图函数  视图函数给予页面返回
# 每一个路由都需要和视图函数绑定
# MVT V视图函数  3个作用 接受请求 处理数据 返回响应


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('booktest.urls', namespace='booktest')),

    path('polls/', include('polls.urls', namespace='polls'))
]
# 项目的所有路由地址配置文件
# admin路由是django自带的命令模块
