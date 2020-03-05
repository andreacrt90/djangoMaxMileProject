from django.db import models

# main class for Users
class User(models.Model):

    # gender list
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    # fields for users
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    birthdate = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default=FEMALE,
    )
    email = models.CharField(max_length=255)
