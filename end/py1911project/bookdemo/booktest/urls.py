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

]
