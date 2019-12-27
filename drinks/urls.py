from django.urls import path
from . import views



urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('search/', views.search_results, name='search_results'),
    path('no_name/', views.drink_list, name='drink_list'),
    path('signup/', views.signup, name='signup'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('login_required/', views.login_required, name='login_required'),
]
