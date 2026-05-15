from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserVerification(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username