from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'Homepage/index.html')
def expenses(request):
    return render(request,'Homepage/pages/Expenses/expenses.html')
def icon(request):
    return render(request,'Homepage/pages/icons/mdi.html')
