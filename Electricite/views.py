from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def electricite (request):
    return render(request, 'gestion_de_energie/electricite.html')
