from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def generator(request):
    return render(request, 'gestion_de_energie/generator.html')