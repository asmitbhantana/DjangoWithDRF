from django.urls import path

from .views import StatusMessageCreateView, StatusMessageDelete

app_name = "statusapp"

urlpatterns = [
    path('create/', StatusMessageCreateView.as_view(), name='create'),
    path('delete/<int:pk>', StatusMessageDelete.as_view(), name='delete'),
]
