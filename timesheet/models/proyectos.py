from django.db import models
from django.contrib.auth.models import User


class Proyecto(models.Model):
    codigo = models.CharField('Nº de servicio', max_length=50, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    descripcion = models.TextField(default='', null=True, blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'proyectos'
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre
