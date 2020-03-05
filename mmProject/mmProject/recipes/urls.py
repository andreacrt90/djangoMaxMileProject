from django.urls import path
from . import views as recipes_views

# recipes list | homepage
# recipe single page

urlpatterns = [
    path('', recipes_views.recipes_list, name="list"),
    path('recipe/', recipes_views.single_recipe, name="single")
]