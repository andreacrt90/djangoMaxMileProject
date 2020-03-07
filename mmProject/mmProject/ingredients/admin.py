from django.contrib import admin
from recipes.models import Recipe

# Register your models here.
from .models import Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["__str__","calories", "num_of_recipes_per_ingredient"]

    class Meta:
        model = Ingredient

    def num_of_recipes_per_ingredient(self, obj):
        recipes_per_ingredient = 0
        for recipe in Recipe.objects.filter(ingredients=obj):
            recipes_per_ingredient += 1
        return recipes_per_ingredient

admin.site.register(Ingredient, IngredientAdmin)
