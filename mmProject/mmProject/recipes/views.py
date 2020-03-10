from .models import Recipe
from .filters import RecipeFilter
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


def recipe_list_view(request, **kwargs):
    """
    The function to view and filter the recipes list in homepage.
    Parameters
    ----------
    request
        the HTTP request made

    Returns
    -------
    render
        the view to render in HTML file
    """
    queryset_list = Recipe.objects.all().order_by("-id")
    filtered = RecipeFilter(request.GET, queryset=queryset_list)
    filtered_qs = filtered.qs
    paginator = Paginator(filtered_qs, 5)
    page = request.GET.get('page', 1)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "paginator": paginator,
        "title": "list",
        "filter": filtered,
        "object_list": queryset
    }
    return render(request, "recipes.html", context)


def recipe_detail_view(request, id=None, **kwargs):
    """
    The function to view a single recipe page.
    Parameters
    ----------
    request
        the HTTP request made
    id: int
        the id of the recipe to view

    Returns
    -------
    render
        the view to render in HTML file
    """
    instance = get_object_or_404(Recipe, id=id)
    context = {
        "object": instance,
        "title": "single"
    }
    return render(request, "recipe.html", context)
