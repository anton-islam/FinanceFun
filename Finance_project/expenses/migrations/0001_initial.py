# Generated by Django 4.1.7 on 2023-02-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('item_name', models.CharField(max_length=50)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('credit', 'Credit'), ('debit', 'Debit')], default='cash', max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
