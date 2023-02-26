from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', views.expense_list_view, name='expenses'),
    path('icon/', views.icon, name='icon'),
]
