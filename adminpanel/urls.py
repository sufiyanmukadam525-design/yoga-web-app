from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('dashboard/users/', views.user_management_dashboard, name='user_mgmt'),
    path('dashboard/content/', views.content_dashboard, name='content'),
    path('dashboard/reports/', views.reports_dashboard, name='reports'),
]
