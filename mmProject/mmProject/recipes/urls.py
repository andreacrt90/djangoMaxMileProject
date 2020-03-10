from django.urls import path
from . import views as recipes_views
from django.views.generic import ListView, DetailView
from . import views as recipe_views

# recipes list | homepage
# recipe single page

urlpatterns = [
    path('', recipe_views.recipe_list_view, name="list"),
    path('<int:id>/<slug:slug>/', recipe_views.recipe_detail_view, name="single"),
]