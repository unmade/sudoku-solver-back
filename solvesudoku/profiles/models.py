from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    name = models.CharField(max_length=255, blank=False, default="Anonymous")
    picture_url = models.URLField(null=True)

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
