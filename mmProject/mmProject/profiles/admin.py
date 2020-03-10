from django.contrib import admin
from recipes.models import Recipe
from ingredients.models import Ingredient

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user","birthdate","gender","recipes_created_by_user","ingredients_used_by_user"]

    def recipes_created_by_user(self, obj):
        recipes_per_user = 0
        for recipe in Recipe.objects.filter(author=obj.user):
            recipes_per_user += 1
        return recipes_per_user

    def ingredients_used_by_user(self, obj):
        ingredients_used_by_user = 0
        for ingredient in Ingredient.objects.all():
            for recipe in Recipe.objects.filter(author=obj.user, ingredients=ingredient):
                ingredients_used_by_user = ingredients_used_by_user + 1
        return ingredients_used_by_user

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
