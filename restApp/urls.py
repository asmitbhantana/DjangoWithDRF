from django.urls import path
from .views import add_two_numbers_in_rest, add_two_numbers, info_view
from .class_views import InfoClassBasedView
from .generic_views import InfoModelCreateAPIView, InfoModelListAPIView, InfoModelDeleteAPIView, InfoModelUpdateAPIView, \
    InfoModelRetrieveAPIView

from rest_framework.routers import DefaultRouter, SimpleRouter

from .viewset_views import InfoModelViewSet

from rest_framework.authtoken.views import obtain_auth_token

# registering routers for model viewsets
# r = SimpleRouter()
r = DefaultRouter()
r.register('info/viewset', InfoModelViewSet)

app_name = 'rest'
urlpatterns = [
                  path('add/', add_two_numbers, name="add1"),
                  path('v2/add/', add_two_numbers_in_rest, name="add2"),
                  path('info/<int:pk>/', info_view, name="info"),

                  path('info/classbased/', InfoClassBasedView.as_view(), name="classbasedinfo"),
                  path('info/classbased/<int:pk>/', InfoClassBasedView.as_view(), name="classbasedinfo"),

                  path('info/generic/create/', InfoModelCreateAPIView.as_view(), name="genericviewcreate"),
                  path('info/generic/list/', InfoModelListAPIView.as_view(), name="genericviewlist"),
                  path('info/generic/delete/<int:pk>/', InfoModelDeleteAPIView.as_view(), name="genericviewdelete"),
                  path('info/generic/update/<int:pk>/', InfoModelUpdateAPIView.as_view(), name="genericviewupdate"),
                  path('info/generic/detail/<int:pk>/', InfoModelRetrieveAPIView.as_view(), name="genericviewdetail"),

                  # path('info/viewset/', InfoModelViewSet.as_view(actions={'get': 'list', 'post': 'create', 'put': 'update'}),
                  # name="viewset"),
                  path('login/', obtain_auth_token, name="login")
              ] + r.urls
