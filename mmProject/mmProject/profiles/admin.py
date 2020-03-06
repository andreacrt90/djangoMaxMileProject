from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # TODO calculate all recipes done by user
    # TODO calculate all ingredients used by user
    list_display = ["user","birthdate","gender"]

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)
