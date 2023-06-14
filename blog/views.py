from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria,Postagem
from django.shortcuts import get_object_or_404

def detalhe_postagem(request,id_postagem):
    postagem = get_object_or_404(Postagem, id=id_postagem)
    context={
        'objeto' : postagem,
    }
    return render(request,'blog/detalhe.html',context)



# Create your views here.

def index(request):
    context={'mensagem': 'Estamos felizes por tê-lo conosco. Explore nosso site para saber mais!!!!'}
    return render(request,'blog/index.html',context)

def lista_categoria(request):
    categorias = Categoria.objects.all() #pegando dados do banco.
    context={'categorias': categorias} #preparando os dados para o .html
    return render(request,'blog/categoria.html',context)

def lista_postagem(request):
    postagens = Postagem.objects.all()
    context = {
        'lista_postagens' : postagens 
    } 
    return render(request,'blog/postagem.html',context)

