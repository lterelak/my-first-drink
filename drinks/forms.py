from django.forms import ModelForm
from drinks.models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'preparation', 'ingredients', 'recipe_image']

