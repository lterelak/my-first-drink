from django.shortcuts import render
from django.db.models import Q

from .models import Recipe
from .models import Ingredient

from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


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

def SignUp(request):

    template="drinks/signup.html"
    form_class = UserCreationForm
    form = form_class
    return render(request, template, {'form': form})