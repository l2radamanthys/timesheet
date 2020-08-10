from rest_framework import serializers
from timesheet.models.proyectos import Proyecto


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'nombre',
        )
