from django.db import models
# profiles is a one-to-one extension of users
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save

# main class for Profile
class Profile(models.Model):

    # gender list
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    # fields for profiles
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default=MALE
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and instance.username != 'admin':
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        if instance.username != 'admin':
            instance.profile.save()
