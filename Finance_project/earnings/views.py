from django.shortcuts import render
from django.http import HttpResponse

def earnings(request):
    return render(request,'Homepage/pages/earnings/earnings.html')
