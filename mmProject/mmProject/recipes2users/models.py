from django.db import models

# recipes related to users
class Recipe2User(models.Model):

    # fields for recipes2users
    recipe = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
