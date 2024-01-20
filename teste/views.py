from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm
from teste.models import Aluno, Cursos
# Create your views here.
def index (request):
    return HttpResponse("Olá Mundo! Agora e na Web.")

def listar_Aluno(request):
     alunos = Aluno.objects.all() 
     return render(request,'listar_aluno.html',
                  {'alunos': alunos}) 

def Listar_Cursos(request):
     cursos = Cursos.objects.all()
     return render(request,'listar_cursos.html',
                   {'cursos': cursos})
def incluirAluno(request):
    if request.method == 'POST':
       form = AlunoForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('listar_alunos')
    else:
        form = AlunoForm()   
    return render(request, 'incluir_aluno.html',
                  {'form': form})
def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
        
    return render(request,'incluir_aluno.html',
                  {'form':form})

