from django.db import models

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.nome

# Create your models here.

LISTA_SEXO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

LISTA_CURSO = [
    ('Apicultura', 'Apicultura'),
    ('Alimentos', 'Alimentos'),
    ('Informática', 'Informática'),
]

class Inscricao(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    data_nascimento = models.DateTimeField()
    email = models.EmailField()
    endereco = models.CharField(max_length=250)
    sexo = models.CharField(max_length=150, choices=LISTA_SEXO, default="feminino")
    curso = models.CharField(max_length=150, choices=LISTA_CURSO)
    minicursos = models.ManyToManyField(MiniCurso)
    
    def __str__(self) -> str:
        return self.nome
