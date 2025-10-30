# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rotas de Login
    path('', views.login_view, name='login'),
    path('login_create', views.login_create, name='login_create'),
    
    # Rotas do App
    # A 'app_welcome' foi removida e substituída pela 'app_dashboard'
    path('app/dashboard', views.app_dashboard, name='app_dashboard'),
    path('app/users', views.app_users, name='app_users'),
    
    # NOVAS URLS:
    path('app/items', views.app_items, name='app_items'),
    path('app/requests', views.app_requests, name='app_requests'),
    path('app/history', views.app_history, name='app_history'),
    path('app/reports', views.app_reports, name='app_reports'),
    path('app/configs', views.app_configs, name='app_configs'),
]