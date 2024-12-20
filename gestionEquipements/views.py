from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def gestion_equipements (request):
    return render(request, 'stocks/gestion_equipements.html')
