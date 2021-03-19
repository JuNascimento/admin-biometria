# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Imagem(models.Model):
    imagem = models.ImageField(upload_to='images/', default='')
    nome_da_imagem = models.CharField(max_length=200)
    adicionada_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    adicionada = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.adicionada = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_da_imagem

