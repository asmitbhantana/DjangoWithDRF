from django.urls import path, register_converter, re_path

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
    path('articles/<uuid:id>', views.article_uid),
    # path('articles/<yyyy:year>', views.year_archive)
    re_path(r'^articles/(?:page-(?P<page_number>\d+)/)?$', views.article_page),  # good

]