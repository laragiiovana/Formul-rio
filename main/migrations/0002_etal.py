# Generated by Django 4.1.3 on 2022-11-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.IntegerField()),
                ('data_nascimento', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=250)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=150)),
                ('curso', models.CharField(choices=[('Apicultura', 'Apicultura'), ('Alimentos', 'Alimentos'), ('Informática', 'Informática')], max_length=150)),
            ],
        ),
    ]