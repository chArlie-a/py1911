# Charlie
# date:2020/3/4 14:49
# file_name:pagination
from rest_framework import pagination


class MyPagination(pagination.PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'num'
