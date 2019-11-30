from django.shortcuts import render
from rapidog.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def produtos(request):
    alimentacao = Produto.objects.filter(categoria='alimentacao').order_by('-id')[:5]
    higiene = Produto.objects.filter(categoria='higiene').order_by('-id')[:5]
    brinquedos = Produto.objects.filter(categoria='brinquedos').order_by('-id')[:5]

    context = {
        'alimentacao': alimentacao,
        'higiene': higiene,
        'brinquedos': brinquedos
    }

    return render(request, 'produtos.html', context)