
from django.shortcuts import render, redirect
from .forms import StudentProfileForm
from .models import StudentProfile

def student_home(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)
    user_applications = Application.objects.filter(student=request.user)
    return render(request, 'students/student_home.html',{'profile':profile, 'applications':user_applications})

def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_home')
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'students/update_profile.html', {'form': form})


from company.models import InternshipPost

def find_internship(request):
    internships = InternshipPost.objects.all()
    return render(request, 'students/find_internship.html', {'internships': internships})

from django.shortcuts import  get_object_or_404
from .models import Application

def apply_for_internship(request, pk):
    internship = get_object_or_404(InternshipPost, pk=pk)
    already_applied = Application.objects.filter(student=request.user, internship=internship).exists()
    if not already_applied:
        Application.objects.create(student=request.user, internship=internship)

    return redirect('student_home')
def cancel_application(request, pk):
    application = get_object_or_404(Application, pk=pk, student=request.user)
    application.delete()
    return redirect('student_home')


