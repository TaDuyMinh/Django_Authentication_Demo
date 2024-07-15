from django.urls import path
from .views import register_user, user_login,user_logout,get_user_infomation,delete_user
from . import views


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('getuserinfo/',get_user_infomation,name='getuserinfo'),
    path('deleteuser/<int:user_id>/', views.delete_user, name='delete_user'),
]
