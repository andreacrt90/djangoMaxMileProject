from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from .filters import RecipeFilter


class RecipeListView(ListView):
    model = Recipe
    queryset = Recipe.objects.all().order_by("-id")
    template_name = "recipes.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name="recipe.html"
