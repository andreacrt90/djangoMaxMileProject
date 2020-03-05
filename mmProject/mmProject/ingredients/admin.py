from django.contrib import admin

# Register your models here.
from .models import Ingredient

class IngredientAdmin(admin.ModelAdmin):
    # TODO calculate all recipes that use the ingredient
    list_display = ["__str__","calories"]

    class Meta:
        model = Ingredient

admin.site.register(Ingredient, IngredientAdmin)
