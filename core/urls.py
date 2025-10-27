from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app_welcome', views.app_welcome, name='app_welcome')
]