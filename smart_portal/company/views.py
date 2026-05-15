from django.shortcuts import render, get_object_or_404, redirect
from .forms import InternshipPostForm
from .models import InternshipPost
from students.models import Application


def company_dashboard(request):
    posts = InternshipPost.objects.filter(company=request.user)
    if request.method == 'POST':
        form = InternshipPostForm(request.POST)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.company = request.user
            internship.save()
            return redirect('company_dashboard')
    else:
        form = InternshipPostForm()

    return render(request, 'company/dashboard.html', {'posts': posts, 'form': form})


def view_applications(request, post_id):
    post = get_object_or_404(InternshipPost, id=post_id, company=request.user)
    all_apps = Application.objects.filter(internship=post)


    req_skills = [s.strip().lower() for s in post.required_skills.replace('\n', ',').split(',') if s.strip()]

    for app in all_apps:
        try:

            raw_skills = app.student.profile.skills
            if raw_skills:

                std_skills = [s.strip().lower() for s in raw_skills.replace('\n', ',').split(',') if s.strip()]

                matched = set(req_skills) & set(std_skills)
                score = (len(matched) / len(req_skills)) * 100 if req_skills else 0
                app.match_score = round(score, 1)
            else:
                app.match_score = 0
        except Exception as e:
            print(f"Error for {app.student.username}: {e}")
            app.match_score = 0

    return render(request, 'company/view_applications.html', {
        'post': post,
        'applications': all_apps
    })

def update_status(request, app_id, status):
    app = get_object_or_404(Application, id=app_id, internship__company=request.user)
    app.status = status
    app.save()
    return redirect('view_applications', post_id=app.internship.id)


from django.shortcuts import get_object_or_404, redirect
from .models import InternshipPost


def delete_internship(request, post_id):
    post = get_object_or_404(InternshipPost, id=post_id, company=request.user)

    if request.method == 'POST':
        post.delete()

    return redirect('company_dashboard')