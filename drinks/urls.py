from django.urls import path
from . import views



urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('search/', views.search_results, name='search_results'),
    path('no_name/', views.drink_list, name='drink_list'),
    path('signup/', views.signup, name='signup'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('login_required/', views.login_required, name='login_required'),
    path('success/', views.success_added_recipe, name='success_added_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('success1/', views.success_added_ingredient, name='success_added_ingredient'),
    path('sms/', views.sms_response),
]
