from django.urls import path
from .views import forms_home, django_form, django_model_form

urlpatterns=[
    path('home/',forms_home),
    path('django_form/',django_form),
    path('django_model_form/',django_model_form),
]