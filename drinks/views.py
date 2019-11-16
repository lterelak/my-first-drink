
from django.shortcuts import render
from django.db.models import Q

from .models import Recipe
from .models import Ingredient

from django.contrib import messages
from django.shortcuts import redirect


def drink_list(request):
    template = "drinks/drink_list.html"
    return render(request, template)

def search_results(besos):

    query = besos.GET.get('q')

    if not query or query == ' ' or query == '  ' or query == '   ':
        messages.error(besos, "Search field can not be empty")
        return redirect('drink_list')

    else:
        q = Q()
        for queries in query.split():
            q |= (Q(ingredients__ingredient_name__contains=queries))
            #why it look for 'sok z cytryny' and show as well sok z limonki
        results = Recipe.objects.filter(q)
        template = "drinks/search_results.html"
        context = {
        'results' : results,
        }
        return render(besos, template, context)
