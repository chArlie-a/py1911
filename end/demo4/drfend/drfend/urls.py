"""drfend URL Configuration

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
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
from shop.views import *
from rest_framework.documentation import include_docs_urls
# 引入DRF自带的路由类
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = routers.DefaultRouter()
# 可以通过router默认路由注册资源
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)
router.register('goodimg', GoodImgsViewSets)
router.register('users', UserViewSets)
router.register('orders', OrderViewSets)

from rest_framework_simplejwt.authentication import JWTAuthentication
from shop.serializers import UserSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    url('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # url(r'^categorylist/$', categoryList, name='categorylist'),
    # url(r'^categorydetail/(\d+)/$', categoryDetail, name='categorydetail'),

    # url(r'^categorylist/$', CategoryListView.as_view(), name='categorylist'),
    # url(r'^categorydetail/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='categorydetail'),

    # url(r'^categorys/$', CategoryViewSets2.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$',
    #     CategoryViewSets2.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'detele': 'destroy'})),

    # url(r'^obtain_jwt_token/$',obtain_jwt_token),

    # 先通过用户名密码  得到token  VUE将refresh以及access  通过access请求服务器  通过refresh获取新的access
    url(r'^obtaintoken/$', token_obtain_pair, name='login'),
    url(r'^refresh/$', token_refresh, name='refresh'),
    url(r'^getuserinfo/$',getuserinfo),
    url(r'^sendmsg/$',sendmsg),
    path('api/v1/docs/', include_docs_urls(title='RestFulAPI', description='RestFulAPI v1')),
    path('', include('rest_framework.urls'))
]
