from django.db import models



class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=200,
                            null=False)
    
    valor = models.DecimalField(max_length=11, 
                                max_digits=11,
                                decimal_places= 2, 
                                null=False)
    
    def __str__(self):
        return self.nome
    
class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)

    id_curso = models.ForeignKey(Curso, 
                                 on_delete=models.DO_NOTHING)
    data_inicio = models.DateTimeField(null=False)

    data_termino = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.id_turma

class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,
                            null=False)
    email = models.CharField(max_length=200,
                             null=False)
    telefone = models.CharField(max_length=15,
                                null=False)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200,
                            null=False)
    data_de_nascimento = models.DateField()
    endereco = models.CharField(max_length=200,
                                null=False)
    email = models.CharField(max_length=200,
                             null=False)
    telefone = models.CharField(max_length=15,
                                null=False)
    def __str__(self):
        return self.nome