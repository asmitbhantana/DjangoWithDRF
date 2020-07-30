from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


# class MyLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 5


class MyLimitOffsetPagination(PageNumberPagination):
    page_size = 5
