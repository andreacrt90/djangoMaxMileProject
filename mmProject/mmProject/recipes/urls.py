from django.urls import path
from . import views as recipe_views

# recipes list | homepage
# recipe single page
urlpatterns = [
    path('', recipe_views.recipe_list_view, name="list"),
    path('<int:id>/<slug:slug>/', recipe_views.recipe_detail_view, name="single"),
]