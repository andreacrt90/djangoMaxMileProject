from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    """
    admin model for Recipe
    """
    """
    A class used to represent admin model for recipes.
    ...

    Attributes
    ----------
    list_display : array
        represent the main fields available for recipes 

    Methods
    -------
    save_model(self, request, obj, form, change)
        manage action before and after an object insertion
    total_calories(self, obj):
        return the number of total calories for a single recipe
    """
    list_display = ["__str__","type", "difficulty", "total_calories"]
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        """
        Parameters
        ----------
        self : RecipeAdmin
            the instance of this class
        request
            the HTTP request made
        obj : Recipe
            the current recipe of the list
        """
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def total_calories(self, obj):
        """
        Parameters
        ----------
        self : RecipeAdmin
            the instance of this class
        obj : Recipe
            the current recipe of the list

        Returns
        -------
        calories: int
            an integer that represent the number of total calories for recipe
        """
        calories = 0
        for ingredient in obj.ingredients.all():
            calories = calories + ingredient.calories
        return calories

    class Meta:
        model = Recipe

admin.site.register(Recipe, RecipeAdmin)
