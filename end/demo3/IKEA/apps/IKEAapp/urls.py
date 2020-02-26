# Charlie
# date:2020/2/24 16:04
# file_name:urls
from django.conf.urls import url
from . import views
app_name = 'IKEAapp'

urlpatterns = [
    url(r"^$",views.index,name='index'),
    url(r"^shop/$",views.shop,name='shop'),
    url(r'^favicon.ico/$', views.favicon, name='favicon'),
]
