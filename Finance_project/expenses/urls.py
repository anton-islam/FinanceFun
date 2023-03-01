from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.expense_list_view, name='expenses'),
]
