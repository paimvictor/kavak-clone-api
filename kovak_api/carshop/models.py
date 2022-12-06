from django.db import models


class Car(models.Model):
    # id, nome, marca, modelo, foto, valor
    criado_em = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, blank=True, default="")
    modelo = models.CharField(max_length=100, blank=True, default="")
    foto = models.ImageField()
    ano = models.CharField(max_length=4, blank=True, default="")
    valor = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        ordering = ["valor"]
