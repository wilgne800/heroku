from django.shortcuts import render, get_object_or_404
from .models import Poduto, Cliente
from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Poduto.objects.all()
    context = {
        'outro': 'Django é massa',
        'curso': 'Curso de Django',
        'produtos': produtos
    }

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
def produto(request, pk):
    #prod = Poduto.objects.get(id=pk)
    prod = get_object_or_404(Poduto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

# Definindo a função de visualização para o erro 404
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

# Definindo a função de visualização para o erro 500
def error_500_view(request):
    return render(request, '500.html', status=500)
