from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('approve/<int:v_id>/', views.approve_user, name='approve_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]