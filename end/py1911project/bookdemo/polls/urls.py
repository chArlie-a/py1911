# Charlie
# date:2020/2/16 10:06
# file_name:urls
from . import views
from django.conf.urls import url

app_name = "polls"

urlpatterns = [
    # url(r"^$", views.index, name='index'),
    url(r"^detail/(\d+)/$", views.detail, name='detail'),
    # url(r"^pollsnum/(\d+)/$", views.pollsnum, name='pollsnum')
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^detail/(\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^result/(\d+)/$', views.ResultView.as_view(), name='result'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^regist/$', views.regist, name='regist'),
]
