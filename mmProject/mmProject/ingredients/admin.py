from django.contrib import admin
from recipes.models import Recipe
from .models import Ingredient

class IngredientAdmin(admin.ModelAdmin):
    """
    admin model for Ingredient
    """
    """
    A class used to represent admin model for ingredients.
    ...

    Attributes
    ----------
    list_display : array
        represent the main fields available for ingredients 

    Methods
    -------
    num_of_recipes_per_ingredient(self, obj)
        return the number of recipes per a single ingredient
    """

    list_display = ["__str__","calories", "num_of_recipes_per_ingredient"]

    class Meta:
        model = Ingredient

    def num_of_recipes_per_ingredient(self, obj):
        """
        Parameters
        ----------
        self : IngredientAdmin
            the instance of this class
        obj : Ingredient
            the current ingredient of the list

        Returns
        -------
        recipes_per_ingredient: int
            an integer that represent the number of recipes per current ingredient
        """
        recipes_per_ingredient = 0
        for recipe in Recipe.objects.filter(ingredients=obj):
            recipes_per_ingredient += 1
        return recipes_per_ingredient

admin.site.register(Ingredient, IngredientAdmin)
