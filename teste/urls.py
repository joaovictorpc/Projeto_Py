from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
  

#Alunos
    path('listar_alunos',views.listar_Aluno,
           name ='listar_alunos'),


#Cursos
     path('listar_cursos',views.Listar_Cursos,
          name='listar_cursos'),
#cadastrar
     path('incluir_aluno', views.incluirAluno,
         name='incluir_aluno'),
#Editar Alunos
     path ('editar_aluno/<int:id>',views.editarAluno,
           name = 'editar_aluno'),
]