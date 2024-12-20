from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def stocks_equipements(request):
    return render(request, 'stocks/stocks_equipements.html')