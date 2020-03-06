from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User
from django.urls import reverse

# main class for Recipes
class Recipe(models.Model):

    # recipes type list
    APPETIZER = 'Antipasto'
    FIRST_COURSE = 'Primo'
    SECOND_COURSE = 'Secondo'
    SIDE_DISH = 'Contorno'
    DESSERT = 'Dessert'
    RECIPES_TYPE = [
        (APPETIZER, 'Appetizer'),
        (FIRST_COURSE, 'First Course'),
        (SECOND_COURSE, 'Second Course'),
        (SIDE_DISH, 'Side Dish'),
        (DESSERT, 'Dessert'),
    ]

    # recipes difficulty list
    EASY_DIFF = 'Bassa difficoltà'
    MIDDLE_DIFF = 'Media difficoltà'
    HARD_DIFF = 'Alta difficoltà'
    DIFFICULTY_TYPE = [
        (EASY_DIFF, 'Easy'),
        (MIDDLE_DIFF, 'Middle'),
        (HARD_DIFF, 'Hard'),
    ]

    # fields for recipes
    name = models.CharField(max_length=120)
    type = models.CharField(
        max_length=120,
        choices=RECIPES_TYPE,
        default=APPETIZER,
    )
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, editable=False)
    difficulty = models.CharField(
        max_length=120,
        choices=DIFFICULTY_TYPE,
        default=MIDDLE_DIFF,
    )
    description = models.TextField()
    image = models.ImageField(upload_to='')
    ingredients = models.ManyToManyField(Ingredient)
    nationality = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    # best practice to obtin single recipe url
    def get_absolute_url(self):
        return reverse("single", kwargs={"id": self.id, "slug": self.slug})
