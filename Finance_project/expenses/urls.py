from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.expenses, name='expenses'),
    path('icon/', views.icon, name='icon'),
]
