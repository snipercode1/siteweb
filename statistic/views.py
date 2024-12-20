from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def statistic(request):
    return render (request, 'interventions/statistics.html')