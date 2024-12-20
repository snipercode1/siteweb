from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def modeOperatoire(request):
    return render(request, 'documentations/modeOperatoire.html')