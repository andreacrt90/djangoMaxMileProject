from django.urls import path
from . import views as recipes_views
from django.views.generic import ListView, DetailView
from .models import Recipe

# recipes list | homepage
# recipe single page

urlpatterns = [
    path('', ListView.as_view(
        queryset = Recipe.objects.all().order_by("-id"),
        template_name = "recipes.html"
    ), name="list"),
    path('recipe/', recipes_views.single_recipe, name="single")
]