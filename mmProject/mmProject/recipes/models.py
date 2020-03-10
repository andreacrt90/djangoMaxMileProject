from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User
from django.urls import reverse


# main class for Recipes
class Recipe(models.Model):
    """
    model for Recipe
    """
    """
    A class used to represent model for recipes.
    ...

    Attributes
    ----------
    name : char
        represent the name of the recipe
    type : char
        represent the type of recipe
    author : User
        represent the user that created the recipe
    difficulty : char
        represent the difficulty of recipe
    description : text
        a long description for recipe
    image : image
        the upload image for recipe
    ingredients : array
        a list of ingredients that make recipe
    nationality : char
        represent the origin country of the recipe
    slug : char
        a short url for the recipe page
    """

    APPETIZER = 'Antipasto'
    FIRST_COURSE = 'Primo'
    SECOND_COURSE = 'Secondo'
    SIDE_DISH = 'Contorno'
    DESSERT = 'Dessert'
    RECIPES_TYPE = [
        (APPETIZER, APPETIZER),
        (FIRST_COURSE, FIRST_COURSE),
        (SECOND_COURSE, SECOND_COURSE),
        (SIDE_DISH, SIDE_DISH),
        (DESSERT, DESSERT),
    ]

    # recipes difficulty list
    EASY_DIFF = 'Bassa difficoltà'
    MIDDLE_DIFF = 'Media difficoltà'
    HARD_DIFF = 'Alta difficoltà'
    DIFFICULTY_TYPE = [
        (EASY_DIFF, EASY_DIFF),
        (MIDDLE_DIFF, MIDDLE_DIFF),
        (HARD_DIFF, HARD_DIFF),
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

    # obtain single recipe url
    def get_absolute_url(self):
        """
        Parameters
        ----------
        self : Recipe
            the instance of this recipe

        Returns
        -------
        url: char
            represent the absolute url of the recipe page
        """
        return reverse("single", kwargs={"id": self.id, "slug": self.slug})
