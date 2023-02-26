from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'item_name', 'payment_method', 'amount', 'description')
