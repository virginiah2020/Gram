from django.db import models
from django.contrib.auth.models import User

from pyuploadcare.dj.models import ImageField

# Create your models here.

class Profile(models.Model):
    profile_pic =ImageField(null = True,blank=True)
    bio = models.CharField(max_length=255)
    owner = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")

