from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import RegisteredUser
<<<<<<< HEAD
from yogaapp.models import Profile
=======
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        RegisteredUser.objects.create(user=instance, username=instance.username, email=instance.email)
<<<<<<< HEAD


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
=======
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
