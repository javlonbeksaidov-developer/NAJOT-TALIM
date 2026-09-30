from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profiles(models.Model):
    bio = models.TextField()
    image = models.ImageField(upload_to="profile/images", blank=True)
    cover_image = models.ImageField(upload_to="profile/cover_images", blank=True)
    birth_date = models.DateField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Twits(models.Model):
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="twits")


class Comments(models.Model):
    text = models.TextField()

    twit = models.ForeignKey(Twits, on_delete=models.CASCADE, related_name="twit_comments")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_comments")


class Images(models.Model):
    images = models.ImageField(upload_to="profile/images", blank=True)

    twit = models.ForeignKey(Twits, on_delete=models.CASCADE, related_name="images")
