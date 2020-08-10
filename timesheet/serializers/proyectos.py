from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from rest_framework_json_api.relations import ResourceRelatedField

from timesheet.models.proyectos import Proyecto


class ProyectoSerializer(ModelSerializer):
    # model = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Proyecto
        fields = (
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
