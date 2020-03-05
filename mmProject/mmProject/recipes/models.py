from django.db import models

# main class for Recipes
class Recipe(models.Model):

    # recipes type list
    APPETIZER = 'AP'
    FIRST_COURSE = 'FC'
    SECOND_COURSE = 'SC'
    SIDE_DISH = 'SD'
    DESSERT = 'DT'
    RECIPES_TYPE = [
        (APPETIZER, 'Appetizer'),
        (FIRST_COURSE, 'First Course'),
        (SECOND_COURSE, 'Second Course'),
        (SIDE_DISH, 'Side Dish'),
        (DESSERT, 'Dessert'),
    ]

    # recipes difficulty list
    EASY_DIFF = 'ED'
    MIDDLE_DIFF = 'MD'
    HARD_DIFF = 'HD'
    DIFFICULTY_TYPE = [
        (EASY_DIFF, 'Easy'),
        (MIDDLE_DIFF, 'Middle'),
        (HARD_DIFF, 'Hard'),
    ]

    # fields for recipes
    name = models.CharField(max_length=120)
    type = models.CharField(
        max_length=2,
        choices=RECIPES_TYPE,
        default=APPETIZER,
    )
    author = models.CharField(max_length=120)
    difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY_TYPE,
        default=MIDDLE_DIFF,
    )
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    nationality = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name
