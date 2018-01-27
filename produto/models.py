from django.db import models

class Produto(models.Model):
    name = models.CharField('Nome', max_length=100)
    value = models.DecimalField('Valor', max_digits=6, decimal_places=2)
    bar_code = models.CharField('Código de Barras', max_length=13, unique=True)