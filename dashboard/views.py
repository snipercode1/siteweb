from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard (request, *args, **kwargs):
    return render(request, 'index.html')