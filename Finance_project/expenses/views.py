from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import JsonResponse

def expense_list_view(request):
        expenses = Expense.objects.all()
        form = ExpenseForm()
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('expenses')

        context = {
            'expenses': expenses,
            'form': form,
        }
        return render(request, 'Homepage/pages/Expenses/expenses.html', context)


def edit_expense(request, expense_id):
    if request.method == 'GET':
        # Get the expense data from the database
        expense = Expense.objects.get(id=expense_id)

        # Convert the expense data to a JSON response
        data = {
            'date': expense.date.strftime('%Y-%m-%d'),
            'item_name': expense.item_name,
            'payment_method': expense.payment_method,
            'amount': expense.amount,
            'description': expense.description
        }

        return JsonResponse(data)

    elif request.method == 'POST':
        # Update the expense data in the database
        expense = Expense.objects.get(id=expense_id)
        expense.date = request.POST['date']
        expense.item_name = request.POST['item_name']
        expense.payment_method = request.POST['payment_method']
        expense.amount = request.POST['amount']
        expense.description = request.POST['description']
        expense.save()

        return JsonResponse({})


def delete_expense(request, expense_id):
    if request.method == 'POST':
        # Delete the expense data from the database
        expense = Expense.objects.get(id=expense_id)
        expense.delete()

        return JsonResponse({})

"""class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ['date','item_name', 'amount', 'description']
    template_name_suffix = 'expense_update_form.html'

class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = reverse_lazy('expenses')"""

