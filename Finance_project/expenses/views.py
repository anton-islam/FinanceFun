from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

def expense_list_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            expense = Expense.objects.all()
            return render(request, 'Homepage/pages/Expenses/expenses.html', {'form': form, 'expenses': expense})
    else:
        form = ExpenseForm()
    return render(request, 'Homepage/pages/Expenses/expenses.html', {'form': form})

"""class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ['date','item_name', 'amount', 'description']
    template_name_suffix = 'expense_update_form.html'

class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expenses')"""

def icon(request):
    return render(request,'Homepage/pages/icons/mdi.html')
