from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def listeIntervention(request):
    return render(request, 'interventions/listeIntervention.html')