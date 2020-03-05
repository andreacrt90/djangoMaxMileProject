from django.db import models

# main class for Ingredients
class Ingredient(models.Model):

    # fields for ingredients
    name = models.CharField(max_length=120)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
