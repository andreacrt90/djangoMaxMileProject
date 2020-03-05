from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    # TODO calculate all calories by ingredients
    list_display = ["__str__","type","difficulty"]

    class Meta:
        model = Recipe

admin.site.register(Recipe, RecipeAdmin)
