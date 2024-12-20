from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def equipements (request):
    return render(request, 'proprieter/equipements.html')