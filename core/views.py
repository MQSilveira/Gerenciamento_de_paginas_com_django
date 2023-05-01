from django.shortcuts import get_object_or_404, render
from .models import Produto


def index(request):    
    context = {
        'titulo': 'INICIO DJANGO'
    }
    
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produtos(request):     
    return render(request, 'produtos.html')


def produto(request, id):    
    produto = get_object_or_404(Produto, pk=id)
    
    context = {
        'titulo': 'PRODUTOS DJANGO',
        'produto': produto
    }
    print(produto)
    return render(request, 'produto.html', context)


def error404(request, exception):
    
    return render(request, 'error404.html')


