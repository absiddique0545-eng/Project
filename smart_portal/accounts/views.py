from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from admin_app.models import UserVerification
from django.contrib.auth.models import Group
from .forms import EnhancedUserCreationForm



def register_view(request):
    if request.method == 'POST':
        form = EnhancedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_role = form.cleaned_data.get('role')
            if user_role:
                group = Group.objects.get_or_create(name=user_role.capitalize())
                user.groups.add(group)
            UserVerification.objects.get_or_create(user=user, is_verified=False)

            return redirect('login')
    else:
        form = EnhancedUserCreationForm()
        for field in form.fields:
            form.fields[field].help_text = None

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
        for field in form.fields:
            form.fields[field].help_text = None

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')