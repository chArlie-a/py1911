# Charlie
# date:2020/2/20 9:43
# file_name:urls
from django.conf.urls import url
from . import views
from .feed import ArticleFeed
app_name = 'blogapp'

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r"^detail/(\d+)/$", views.detail, name='detail'),
    url(r"^contact/$", views.contact, name='contact'),
    url(r'^favicon.ico/$', views.favicon, name='favicon'),
    url(r'^rss/$', ArticleFeed(), name='rss')
]
