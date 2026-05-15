from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class InternshipPost(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField(help_text="skill separated by comma")
    location = models.CharField(max_length=200)
    deadline = models.DateField()
    def __str__(self):
        return self.title