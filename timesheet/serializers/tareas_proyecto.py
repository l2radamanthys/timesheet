from rest_framework import serializers
from timesheet.models.tareas_proyecto import TareaProyecto


class TareaProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaProyecto
        fields = (
            'user',
            'proyecto',
            'tarea',
            'fecha',
            'horas_facturables',
            'horas_no_facturables',
        )
