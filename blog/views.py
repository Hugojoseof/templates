from django.shortcuts import render
from .models import Curso
from django.shortcuts import get_object_or_404





# Create your views here.

def index(request):
    context={'mensagem': 'Estamos felizes por tê-lo conosco. Explore nosso site para saber mais!!!!'}
    return render(request,'blog/index.html',context)


def curso(request,id):
    curso = get_object_or_404(Curso,id=id)
    context = {'curso' : curso } 
    return render(request,'blog/curso.html',context)


