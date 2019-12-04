from django.shortcuts import render
from django.db.models import Q
from rapidog.models import *
from rapidog.forms import NewsletterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def produtos(request):
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')[:5]
    higiene = Produto.objects.filter(disponivel=True, categoria='higiene').order_by('-id')[:5]
    brinquedos = Produto.objects.filter(disponivel=True, categoria='brinquedos').order_by('-id')[:5]

    context = {
        'alimentacao': alimentacao,
        'higiene': higiene,
        'brinquedos': brinquedos
    }

    return render(request, 'produtos.html', context)

def alimentacao(request):
    query = request.GET.get('q','')
    alimentacao = Produto.objects.filter(disponivel=True, categoria='alimentacao').order_by('-id')


    if query:
            queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
            resultados = Produto.objects.filter(queryset, categoria='alimentacao').order_by('-id')
    else:
        resultados = []

    context = {
        'query': query,
        'resultados': resultados,
        'alimentacao': alimentacao,
    }

    return render(request, 'alimentacao.html', context)

def higiene(request):
    query = request.GET.get('q','')
    higiene = Produto.objects.filter(disponivel=True, categoria='higiene').order_by('-id')

    if query:
            queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
            resultados = Produto.objects.filter(queryset, categoria='higiene').order_by('-id')
    else:
        resultados = []

    context = {
        'query': query,
        'resultados': resultados,
        'higiene': higiene,
    }

    return render(request, 'higiene.html', context)

def brinquedos(request):
    query = request.GET.get('q','')
    brinquedos = Produto.objects.filter(disponivel=True, categoria='brinquedos').order_by('-id')

    if query:
            queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
            resultados = Produto.objects.filter(queryset, categoria='brinquedos').order_by('-id')
    else:
        resultados = []

    context = {
        'query': query,
        'resultados': resultados,
        'brinquedos': brinquedos,
    }

    return render(request, 'brinquedos.html', context)

def lojas(request):
    anunciar = Loja.objects.filter(anunciar=True)[:3]
    jdPaulista = Loja.objects.filter(bairro='Jd Paulista').order_by('-id')[:4]
    consolacao = Loja.objects.filter(bairro='Consolação').order_by('-id')[:4]

    context = {
        'anuncios': anunciar,
        'jdPaulista': jdPaulista,
        'consolacao': consolacao,
    }

    return render(request, 'petshops.html', context)

def busca(request):
    query = request.GET.get('q','')

    if query:
        queryset = (Q(nome_produto__icontains=query)) | (Q(marca__icontains=query))
        resultados = Produto.objects.filter(queryset).order_by('-id')
            
    else:
        resultados = []

    context = {
        'query': query,
        'resultados': resultados,
    }

    return render(request, 'busca.html', context)

def render_newsletter(request):
    newsletter = NewsletterForm(request.POST or None)

    if newsletter.is_valid():
        newsletter.save()

    return render(request, 'sucesso.html')