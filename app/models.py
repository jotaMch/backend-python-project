from django.db import models

class Pratos(models.Model):
    prato = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    porcao = models.IntegerField()
