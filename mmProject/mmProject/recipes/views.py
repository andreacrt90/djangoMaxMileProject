from django.shortcuts import render

# Create your views here.

def single_recipe(request):
    return render(request, "recipe.html")