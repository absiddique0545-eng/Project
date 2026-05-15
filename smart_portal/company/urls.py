from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.company_dashboard, name='company_dashboard'),
    path('applications/<int:post_id>/', views.view_applications, name='view_applications'),
    path('update-status/<int:app_id>/<str:status>/', views.update_status, name='update_status'),
    path('delete-internship/<int:post_id>/', views.delete_internship, name='delete_internship'),
]
