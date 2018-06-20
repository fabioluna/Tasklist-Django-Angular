from django.db import models
from datetime import date


class Task(models.Model):

    titulo = models.CharField(
        max_length=50, help_text="Título da tarefa")
    concluido = models.BooleanField(
        default=False)
    descricao = models.TextField(
        blank=True, null=True,
        help_text="Descrição da tarefa.")
    data_criacao = models.DateField(
        blank=True, null=True)
    data_edicao = models.DateField(
        blank=True, null=True)
    data_conclusao = models.DateField(
        blank=True, null=True)
