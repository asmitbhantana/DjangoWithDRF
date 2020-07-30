
from django.urls import path

from .views import manage_media, manage_static

urlpatterns = [
    path('media/', manage_media),
    path('static/', manage_static),
]