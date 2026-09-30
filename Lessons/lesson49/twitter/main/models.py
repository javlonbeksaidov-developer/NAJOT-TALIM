from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profiles(models.Model):
    bio = models.TextField()
    image = models.ImageField(upload_to="/profile/images")
    cover_image = models.ImageField(upload_to="/profile/cover_images")
    birth_date = models.DateField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
