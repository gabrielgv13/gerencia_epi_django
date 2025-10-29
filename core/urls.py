# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('app_welcome', views.app_welcome, name='app_welcome'),
    path('login_create', views.login_create, name='login_create')
]