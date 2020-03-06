from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    # TODO calculate all calories by ingredients
    list_display = ["__str__","type","difficulty"]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

    class Meta:
        model = Recipe

admin.site.register(Recipe, RecipeAdmin)
