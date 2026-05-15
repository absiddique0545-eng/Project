from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    university = models.CharField(max_length = 200)
    student_id = models.CharField(max_length = 50)
    skills = models.TextField()
    education = models.TextField()
    projects= models.TextField()

    def __str__(self):
        return self.user.username

from company.models import InternshipPost

class Application(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    internship = models.ForeignKey(InternshipPost, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default='pending')
    def __str__(self):
        return self.student.username
