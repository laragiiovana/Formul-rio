# Generated by Django 4.1.3 on 2022-11-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_minicurso_alter_inscricao_sexo_inscricao_minicursos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], default='feminino', max_length=150),
        ),
    ]
