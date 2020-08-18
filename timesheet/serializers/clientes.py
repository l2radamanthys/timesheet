from rest_framework import serializers
from timesheet.models.clientes import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    # model = ResourceRelatedField(many=False, read_only=True)

    class Meta:
        model = Cliente
        fields = (
            'nombre',
        )

    # included_serializers = {
    #     'user': UserSerializer,
    # }
