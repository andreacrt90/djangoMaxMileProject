from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["__str__","type", "difficulty", "total_calories"]
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    def total_calories(self, obj):
        calories = 0
        for ingredient in obj.ingredients.all():
            calories = calories + ingredient.calories
        return calories


    class Meta:
        model = Recipe

admin.site.register(Recipe, RecipeAdmin)
