from django.db import models

# ingredients related to recipes
class IngredientsToRecipe(models.Model):

    # fields for ingredients2recipes
    recipe = models.CharField(max_length=120)
    ingredient = models.CharField(max_length=120)
