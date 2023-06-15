from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateField()
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.nome
    
