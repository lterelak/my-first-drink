from django.urls import path
from . import views



urlpatterns = [
    path('', views.main_side, name='main_side'),
    path('search/', views.search_results, name='search_results'),
    path('signup/', views.signup, name='signup'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('login-required/', views.login_required, name='login_required'),
    path('success/', views.success_added_recipe, name='success_added_recipe'),
    path('add-ingredient/', views.add_ingredient, name='add_ingredient'),
    path('success1/', views.success_added_ingredient, name='success_added_ingredient'),
    path('sms/', views.send_sms, name='send_sms'),
    path('drink-list/', views.drink_list, name='drink_list'),
    path('recipe-details/<int:pk>', views.recipe_details, name='recipe_details'),

]
