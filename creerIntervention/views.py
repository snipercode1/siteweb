from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def creer_intervention(request):
    return render(request, 'interventions/creer_intervention.html')