from django.db import models

# Create your models here.
class  Aluno(models.Model):
    nome = models.CharField(max_length=200,null=False)
    cpf = models.CharField(max_length=14,null=False)
    email = models.EmailField()

    def __str__(self):
        return self.nome + "-" + self.email

class Cursos(models.Model):
    nome_cursos = models.CharField(max_length= 100, null =False)
    