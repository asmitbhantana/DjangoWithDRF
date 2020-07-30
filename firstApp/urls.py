
from django.urls import path,re_path

from firstApp.views import hello

urlpatterns = [
    path('hello/', hello),
]