from django.urls import path
from . import views as recipes_views
from django.views.generic import ListView, DetailView
from .models import Recipe

# recipes list | homepage
# recipe single page

urlpatterns = [
    path('', ListView.as_view(
        queryset = Recipe.objects.all().order_by("-id"),
        template_name = "recipes.html",
        paginate_by = 5
    ), name="list"),

    path('<int:id>/<slug:slug>/', DetailView.as_view(
        model = Recipe,
        template_name="recipe.html"
    ), name="single"),
]