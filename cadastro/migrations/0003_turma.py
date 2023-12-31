# Generated by Django 4.2.6 on 2023-10-08 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_alter_curso_id_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('data_inicio', models.DateTimeField()),
                ('data_termino', models.DateTimeField()),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.curso')),
            ],
        ),
    ]
