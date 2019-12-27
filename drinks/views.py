from django.shortcuts import render
from django.db.models import Q

from .models import Recipe
from .models import Ingredient

from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import RecipeForm

def drink_list(request):
    template = "drinks/drink_list.html"
    return render(request, template)

def search_results(request):

    query = request.GET.get('q')

    if not query or query.strip() == '':
        messages.error(request, "Search field can not be empty")
        return redirect('drink_list')

    #early return (else:)
    q = Q()
    for ingredient_name in query.split():
    #with point .split(',') it is not going to look for many ingredients, but "sok z cytryny" is then counted as one ingredient, how to search for many ingredients and make django know that "sok z cytryny" is only one ingredient in the same time.
        q |= (Q(ingredients__ingredient_name__contains=ingredient_name))
    results = Recipe.objects.filter(q)
    template = "drinks/search_results.html"
    context = {
    'results' : results,
    }
    return render(request, template, context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = UserCreationForm()

    return render(request, "drinks/signup.html", {"form":form})

def login_required(request):
    template = "drinks/login_required.html"
    return render(request, template)



def add_recipe(request):

     if not request.user.is_authenticated:
         return redirect('login_required')

     add_recipe = RecipeForm()
     if add_recipe.is_valid():
          print("valid form")
          add_recipe.save()
     template = "drinks/add_recipe.html"
     return render(request, template, {'RecipeForm': add_recipe})

# def post_recipe(request):
#     form = RecipeForm(request.POST)
#     if form.is_valid():
#         recipe_name = form.cleaned_data['recipe_name']
#         preparation = form.cleaned.data['preparation']
#         ingredients = form.cleaned.data['ingredients']
#         form.save()
#     template = "drinks/search_results.html"
#     return render(request, template, {'form': form, 'recipe_name': recipe_name, 'preparation': preparation, 'ingredients': ingredients})



