from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = 'clientes'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
