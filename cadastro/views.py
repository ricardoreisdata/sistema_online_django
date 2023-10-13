from django.shortcuts import render, redirect
from django.http import HttpResponse
from cadastro.models import Curso, Professor, Aluno
from cadastro.forms import CursoForm, AlunoForm, ProfessorForm

def index(request):
    return render(request, template_name='inicio.html')

def teste(request):
    return HttpResponse('Agora é só um teste!!!!')

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listar_cursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, template_name='listar_cursos.html', context={'lista':cursos})

def listar_professores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, template_name='listar_professores.html', context={'lista':professores})

def listar_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, template_name='listar_alunos.html', context={'lista':alunos})

def incluir_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listar_cursos')
            except:
                pass
    else:
        form = CursoForm()
    return render(request, template_name='incluir_curso.html', context={'form':form})

def editar_curso(request, id):
    curso = Curso.objects.get(id_curso = id)
    form = CursoForm(instance=curso)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_cursos')
            except:
                pass
    return render(request, template_name='incluir_curso.html', context={'form':form})

def excluir_curso(request, id):
    curso = Curso.objects.get(id_curso = id)
    try:
        curso.delete()
    except:
        pass
    return redirect('listar_cursos')

def incluir_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listar_alunos')
            except:
                pass
    else:
        form = AlunoForm()
    return render(request, template_name='incluir_aluno.html', context={'form':form})

def incluir_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listar_professores')
            except:
                pass
    else:
        form = ProfessorForm()
    return render(request, template_name='incluir_professor.html', context={'form':form})

def editar_aluno(request, id):
    aluno = Aluno.objects.get(id_aluno = id)
    form = AlunoForm(instance=aluno)

    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_alunos')
            except:
                pass
    return render(request, template_name='incluir_aluno.html', context={'form':form})

def editar_professor(request, id):
    professor = Professor.objects.get(id_professor = id)
    form = ProfessorForm(instance=professor)

    if request.method == "POST":
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_professores')
            except:
                pass
    return render(request, template_name='incluir_professor.html', context={'form':form})

def excluir_aluno(request, id):
    aluno = Aluno.objects.get(id_aluno = id)
    try:
        Aluno.delete()
    except:
        pass
    return redirect('listar_alunos')

def excluir_professor(request, id):
    professor = Professor.objects.get(id_professor = id)
    try:
        professor.delete()
    except:
        pass
    return redirect('listar_professores')