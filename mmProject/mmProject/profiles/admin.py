from django.contrib import admin
from recipes.models import Recipe
from ingredients.models import Ingredient

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    """
    admin model for Profile
    """
    """
    A class used to represent admin model for profiles.
    ...

    Attributes
    ----------
    list_display : array
        represent the main fields available for profiles 

    Methods
    -------
    recipes_created_by_user(self, obj)
        return the number of recipes created by a single user
    ingredients_used_by_user(self, obj):
        return the number of total ingredients used by a single user
    """
    list_display = ["user","birthdate","gender","recipes_created_by_user","ingredients_used_by_user"]

    def recipes_created_by_user(self, obj):
        """
        Parameters
        ----------
        self : ProfileAdmin
            the instance of this class
        obj : Profile
            the current profile of the list

        Returns
        -------
        recipes_per_user: int
            an integer that represent the number of recipes created by the user
        """
        recipes_per_user = 0
        for recipe in Recipe.objects.filter(author=obj.user):
            recipes_per_user += 1
        return recipes_per_user

    def ingredients_used_by_user(self, obj):
        """
        Parameters
        ----------
        self : ProfileAdmin
            the instance of this class
        obj : Profile
            the current profile of the list

        Returns
        -------
        ingredients_used_by_user: int
            an integer that represent the number of total ingredients used by the user
        """
        ingredients_used_by_user = 0
        for ingredient in Ingredient.objects.all():
            for recipe in Recipe.objects.filter(author=obj.user, ingredients=ingredient):
                ingredients_used_by_user = ingredients_used_by_user + 1
        return ingredients_used_by_user

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
