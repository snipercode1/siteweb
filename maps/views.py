from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def maps(request):
    return render(request, 'maps/maps.html')