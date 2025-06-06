# Generated by Django 5.2.1 on 2025-05-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Título')),
                ('description', models.TextField(blank=True, default='', verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Horário de Criação')),
                ('pub_expiration_date', models.DateTimeField(blank=True, null=True, verbose_name='Prazo da Tarefa')),
                ('priority', models.CharField(blank=True, choices=[('A', 'Alta'), ('M', 'Média'), ('B', 'Baixa'), ('', '-----')], default='', max_length=1, verbose_name='Prioridade')),
                ('type', models.CharField(blank=True, choices=[('L', 'Lembrete'), ('E', 'Evento'), ('N', 'Nota'), ('M', 'Meta'), ('', '-----')], default='', max_length=1, verbose_name='Tipo da Tarefa')),
                ('status', models.CharField(blank=True, choices=[('C', 'Criado'), ('E', 'Em andamento'), ('F', 'Finalizado'), ('', '-----')], default='', max_length=1, verbose_name='Status')),
            ],
        ),
    ]
