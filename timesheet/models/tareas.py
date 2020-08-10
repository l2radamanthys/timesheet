from django.db import models


class Tarea(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = 'tareas'
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.nombre
