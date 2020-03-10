from django.db import models

class Ingredient(models.Model):
    """
    model for Ingredient
    """
    """
    A class used to represent model for ingredients.
    ...

    Attributes
    ----------
    name : char
        represent the name of the ingredient
    calories : int
        represent the calories of the ingredient
    """
    name = models.CharField(max_length=120)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
