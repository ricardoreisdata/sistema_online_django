from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    path('listar_cursos', views.listar_cursos),
    path('listar_professores', views.listar_professores),
    path('listar_alunos', views.listar_alunos)
]