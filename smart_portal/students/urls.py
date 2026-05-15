from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.student_home, name='student_home'),
    path('update/', views.update_profile, name='update_profile'),
    path('find-internship/', views.find_internship, name='find_internship'),
    path('apply/<int:pk>/', views.apply_for_internship, name='apply_for_internship'),
    path('cancel-application/<int:pk>/', views.cancel_application, name='cancel_application'),
]