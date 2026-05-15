from django.shortcuts import redirect

def student_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='Student').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('company_dashboard')
    return wrapper_func

def company_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.groups.filter(name='Company').exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('student_dashboard')
    return wrapper_func