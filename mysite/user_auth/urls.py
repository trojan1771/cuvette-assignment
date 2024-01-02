# user_auth/urls.py

from django.urls import path
from .views import register, user_login, dashboard, user_profile, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', user_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
]
