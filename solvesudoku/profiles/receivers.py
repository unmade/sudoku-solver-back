from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        data = {
            "user": instance,
            "picture_url": None,
        }
        if instance.first_name:
            data["name"] = instance.first_name
        Profile.objects.create(**data)
