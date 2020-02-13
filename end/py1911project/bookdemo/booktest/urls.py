# Charlie
# date:2020/2/13 14:49
# file_name:urls
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r"^index/$", views.index),

    url(r"^json/$", views.jsondata),

]
