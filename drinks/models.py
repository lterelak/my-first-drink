from django.db import models


class Ingredient(models.Model):

  ingredient_name = models.CharField(max_length=250)

  def __str__(self):
    return self.ingredient_name


class Recipe(models.Model):

  recipe_name = models.CharField(max_length=250)
  preparation = models.CharField(max_length=1000)
  ingredients = models.ManyToManyField(Ingredient)
  recipe_image = models.ImageField(upload_to='images/', default='')


  def __str__(self):
    return self.recipe_name
