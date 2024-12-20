from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def interne(request):
    return render(request, 'documentations/interne.html')
