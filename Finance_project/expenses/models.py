from django.db import models

class Expense(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    item_name = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cash')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.item_name} ({self.date}): {self.amount}'
