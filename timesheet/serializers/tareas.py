from django.contrib.auth.models import User
from rest_framework import serializers
from timesheet.models.tareas import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = (
            'nombre',
        )

