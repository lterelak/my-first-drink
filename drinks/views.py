from django.shortcuts import render
from django.db.models import Q

from .models import Recipe
from .models import Ingredient

from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm

from .forms import RecipeForm
from .forms import IngredientForm

from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

from django.shortcuts import get_list_or_404, get_object_or_404

def drink_list(request):
    return render(request, "drinks/drink_list.html")

def search_results(request):
    query = request.GET.get('q')

    if not query or query.strip() == '':
        messages.error(request, "Search field can not be empty")
        return redirect('drink_list')
    #early return (else:)
    q = Q()
    for ingredient_name in query.split(','):
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
         return render(request, 'drinks/login_required.html')

     add_recipe = RecipeForm(request.POST, request.FILES)

     if add_recipe.is_valid():
          add_recipe.save()
          return redirect('success_added_recipe')

     return render(request, 'drinks/add_recipe.html', {'RecipeForm': add_recipe})


def add_ingredient(request):
    if not request.user.is_authenticated:
        return render(request, 'drinks/login_required.html')

    add_ingredient = IngredientForm(request.POST)

    if add_ingredient.is_valid():
        add_ingredient.save()
        return redirect('success_added_ingredient')

    return render(request, 'drinks/add_ingredient.html', {'IngredientForm': add_ingredient})

def success_added_ingredient(request):
    return render(request, 'drinks/success_added_ingredient.html')

def drink_list1(request):
    drinks = Recipe.objects.all()
    return render(request, 'drinks/drink_list1.html', {'drinks': drinks})

def recipe_details(request, pk):
    recipe_details = get_object_or_404(Recipe, pk=pk)
    return render(request, 'drinks/recipe_details.html', {'recipe_details': recipe_details})

def send_sms(request):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    if "username" in request.POST and "sendto" in request.POST and "message" in request.POST:
        username = request.POST["username"]
        sendto = request.POST["sendto"]
        message=request.POST["message"]
        client.messages.create(to=sendto,
                               from_=settings.TWILIO_NUMBER,
                               body=message)
        return HttpResponse("Send")
    return render(request, 'drinks/send_sms.html', {'send_sms': send_sms})






