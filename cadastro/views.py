from django.shortcuts import render
from django.http import HttpResponse
from cadastro.models import Curso, Professor, Aluno

def index(request):
    return HttpResponse('Olá Mundo!!! Agora estou na web')

def teste(request):
    return HttpResponse('Agora é só um teste!!!!')

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listar_cursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, template_name='listar_cursos.html', context={'lista':cursos})

def listar_professores(request):
    professores = Professor.objetcs.all().order_by('nome')
    return render(request, template_name='listar_professores.html', context={'lista':professores})

def listar_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, template_name='listar_alunos.html', context={'lista':alunos})