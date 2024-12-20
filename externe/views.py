from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def externe(request):
    return render(request, 'documentations/externe.html')
