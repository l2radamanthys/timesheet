from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'proyectos'
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombre
