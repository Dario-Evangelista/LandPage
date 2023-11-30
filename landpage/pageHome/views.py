from django.shortcuts import render
from .ultis.factory import depoimentos

# Create your views here.

def home (request):
    return render(request, 'pages/home.html', context= {
        'PAGEHOMES': [depoimentos() for _ in range(10)]
    })