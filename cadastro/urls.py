from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    
    path('listar_cursos', views.listar_cursos, name='listar_cursos'),
    path('incluir_curso', views.incluir_curso, name='incluir_curso'),
    path('editar_curso/<int:id>', views.editar_curso, name='editar_curso'),
    path('excluir_curso/<int:id>', views.excluir_curso,name='excluir_curso'),
    

    path('listar_professores', views.listar_professores, name='listar_professores'),
    path('incluir_professor', views.incluir_professor, name='incluir_professor'),
    path('editar_professor/<int:id>', views.editar_professor, name='editar_professor'),
    path('excluir_professor/<int:id>', views.excluir_professor,name='excluir_professor'),

    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    path('incluir_aluno', views.incluir_aluno, name='incluir_aluno'),
    path('editar_aluno/<int:id>', views.editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:id>', views.excluir_aluno,name='excluir_aluno'),

    path('listar_turmas', views.listar_turmas, name='listar_turmas'),
    path('incluir_turma', views.incluir_turma, name='incluir_turma'),
    path('editar_turma/<int:id>', views.editar_turma, name='editar_turma'),
    path('excluir_turma/<int:id>', views.excluir_turma,name='excluir_turma'),
    
    
    
    
    
    
]