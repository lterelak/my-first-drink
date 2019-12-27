from django.shortcuts import render
from django.db.models import Q

from .models import Recipe
from .models import Ingredient

from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import RecipeForm

def drink_list(request):
    return render(request, "drinks/drink_list.html")

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
    return render(request, "drinks/search_results.html", {"results":results})

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, "drinks/signup.html", {"form":form})

def login_required(request):
    return render(request, "drinks/login_required.html")

def success_added_recipe(request):
    return render(request, "drinks/success_added_recipe.html")

def add_recipe(request):

     if not request.user.is_authenticated:
         return redirect('login_required')

     add_recipe = RecipeForm(request.POST)
     if add_recipe.is_valid():
          add_recipe.save()
          return redirect('success_added_recipe')

     return render(request, 'drinks/add_recipe.html', {'RecipeForm': add_recipe})





