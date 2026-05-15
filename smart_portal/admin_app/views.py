from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserVerification


from company.models import InternshipPost
from students.models import Application

def admin_dashboard(request):

    user_count = User.objects.count()
    post_count = InternshipPost.objects.count()
    app_count = Application.objects.count()
    pending_users = UserVerification.objects.filter(is_verified=False)
    all_users = User.objects.all()

    context = {
        'total_users': user_count,
        'total_posts': post_count,
        'total_apps': app_count,
        'pending': pending_users,
        'reports': all_users,
    }
    return render(request, 'admin_app/dashboard.html', context)


def approve_user(request, v_id):
    obj = UserVerification.objects.get(id=v_id)
    obj.is_verified = True
    obj.save()
    return redirect('admin_dashboard')

def delete_user(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('admin_dashboard')