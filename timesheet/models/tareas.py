from django.db import models


class Tarea(models.Model):
    CLASIFICACIONES = (
        ('Tarea Campo', 'Tarea Campo'),
        ('Gabinete', 'Gabinete'),
    )

    codigo = models.CharField('tipo HH', max_length=50, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    clasificacion = models.CharField(max_length=100, default=None, blank=True, null=True, choices=CLASIFICACIONES)
    descripcion = models.TextField(default='', null=True, blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tareas'
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.nombre
