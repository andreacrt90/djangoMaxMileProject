from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    # TODO calculate all recipes done by user
    # TODO calculate all ingredients used by user
    list_display = ["name","surname"]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)
