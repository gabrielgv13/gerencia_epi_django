# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rotas de Login
    path('', views.login_view, name='login'),
    path('login_create', views.login_create, name='login_create'),
    
    path('app/dashboard', views.app_dashboard, name='app_dashboard'),

    path('app/users', views.app_users, name='app_users'),
    path('app/users', views.app_users, name='app_users'), # READ (List)
    path('app/users/create/', views.app_users_create, name='app_users_create'), # CREATE
    path('app/users/edit/<int:pk>/', views.app_users_edit, name='app_users_edit'), # UPDATE
    path('app/users/delete/<int:pk>/', views.app_users_delete, name='app_users_delete'), # DELETE
    
    path('app/items', views.app_items, name='app_items'),
    path('app/items', views.app_items, name='app_items'), # READ
    path('app/items/create/', views.app_items_create, name='app_items_create'), # CREATE
    path('app/items/edit/<int:pk>/', views.app_items_edit, name='app_items_edit'), # UPDATE
    path('app/items/delete/<int:pk>/', views.app_items_delete, name='app_items_delete'), # DELETE

    path('app/requests', views.app_requests, name='app_requests'),
    path('app/history', views.app_history, name='app_history'),
    path('app/reports', views.app_reports, name='app_reports'),
    path('app/configs', views.app_configs, name='app_configs'),
]