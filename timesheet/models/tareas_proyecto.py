from django.db import models
from django.contrib.auth.models import User


class TareaProyecto(models.Model):
    tarea = models.ForeignKey("Tarea", on_delete=models.CASCADE)
    proyecto = models.ForeignKey("Proyecto", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=None, null=True, blank=True)
    horas = models.FloatField(default=0, blank=True, null=True)

    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tareas_proyecto'
        verbose_name = "TareaProyecto"
        verbose_name_plural = "Tareas Proyecto"

    # def __str__(self):
    #     return self
