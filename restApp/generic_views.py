from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination

from .serializers import InfoModelSerializers
from .models import Info

from .pagination import MyLimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework.backends import DjangoFilterBackend


class InfoModelCreateAPIView(CreateAPIView):
    serializer_class = InfoModelSerializers


class InfoModelListAPIView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializers
    pagination_class = MyLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ['name']
    order_fields = ['name', 'id']
    filterset_fields = ['name', 'address']


class InfoModelDeleteAPIView(DestroyAPIView):
    queryset = Info.objects.all()


class InfoModelUpdateAPIView(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializers


class InfoModelRetrieveAPIView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializers
