from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm

def home(request):
    return render(request,'Homepage/index.html')
def expense_form_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Homepage/pages/Expenses/expenses.html')
    else:
        form = ExpenseForm()
    return render(request, 'Homepage/pages/Expenses/expenses.html', {'form': form})

def expense_list_view(request):
    expenses = Expense.objects.all()
    return render(request, 'Homepage/pages/Expenses/expenses.html', {'expenses': expenses})

def icon(request):
    return render(request,'Homepage/pages/icons/mdi.html')
