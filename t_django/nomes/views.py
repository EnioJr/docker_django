from django.shortcuts import render
from .models import Nome

# Create your views here.


def home(request):
    #nomes = 'Nome Django'
    nome = Nome.objects.all()
    return render(request, 'nomes.html', {'nome': nome})
