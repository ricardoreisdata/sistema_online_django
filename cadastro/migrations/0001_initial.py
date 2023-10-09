# Generated by Django 4.2.6 on 2023-10-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=11, max_length=11)),
            ],
        ),
    ]
