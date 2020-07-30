from django.urls import path
from .views import list_all_user, detail_view_of_user, create_user_info, update_user_info, delete_user_info

app_name = "crudApp"

urlpatterns = [
    path('list/', list_all_user, name="user_list"),
    path('create/', create_user_info, name="user_create"),
    path('detail/<int:user_id>/', detail_view_of_user, name='user_detail'),
    path('update/<int:user_id>/', update_user_info, name='user_update'),
    path('delete/<int:user_id>/', delete_user_info, name='user_delete'),
]
