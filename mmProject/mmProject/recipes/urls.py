from django.urls import path
from . import views as recipes_views
from django.views.generic import ListView, DetailView
from .models import Recipe

# recipes list | homepage
# recipe single page

urlpatterns = [
    path('', recipes_views.RecipeListView.as_view(), name="list"),

    path('<int:id>/<slug:slug>/', recipes_views.RecipeDetailView.as_view(), name="single"),
]