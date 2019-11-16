from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('search/', views.search_results, name='search_results'),
    path('no_name/', views.drink_list, name='drink_list'),
]
