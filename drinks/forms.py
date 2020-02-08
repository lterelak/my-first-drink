from django.forms import ModelForm
from drinks.models import Recipe
from drinks.models import Ingredient

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'preparation', 'ingredients', 'recipe_image']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name']

