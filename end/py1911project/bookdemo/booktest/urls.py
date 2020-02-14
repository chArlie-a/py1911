# Charlie
# date:2020/2/13 14:49
# file_name:urls
from . import views
from django.conf.urls import url

app_name = "booktest"

urlpatterns = [
    url(r"^$", views.index, name='index'),
    url(r"^detail/(\d+)/$", views.detail, name='detail'),
    url(r"^json/$", views.jsondata, name='json'),
    url(r"^deletebook/(\d+)/$", views.deletebook, name='deletebook'),
    url(r"^deletehero/(\d+)/$", views.deletehero, name='deletehero'),
    url(r"^addhero/(\d+)/$", views.addhero, name='addhero'),

    url(r"^addbook/$", views.addbook, name='addbook'),

    url(r"^edithero/(\d+)/$", views.edithero, name='edithero'),
    url(r"^editbook/(\d+)/$", views.editbook, name='editbook'),
]
