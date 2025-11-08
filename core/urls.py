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
    path('app/users', views.app_users, name='app_users'), # READ (List)
    path('app/users/create/', views.app_users_create, name='app_users_create'), # CREATE
    path('app/users/edit/<int:pk>/', views.app_users_edit, name='app_users_edit'), # UPDATE
    path('app/users/delete/<int:pk>/', views.app_users_delete, name='app_users_delete'), # DELETE
    
    # NOVAS URLS:
    path('app/items', views.app_items, name='app_items'),
    path('app/requests', views.app_requests, name='app_requests'),
    path('app/history', views.app_history, name='app_history'),
    path('app/reports', views.app_reports, name='app_reports'),
    path('app/configs', views.app_configs, name='app_configs'),
]