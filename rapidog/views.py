from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def produtos(request):
    # secao_produtos = Produto.objects.filter(disponivel=True).order_by('-id')

    # context = {
    #     'produtos': secao_produtos
    # }
    return render(request, 'produtos.html')