from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from timesheet.models.proyectos import Proyecto
from timesheet.serializers.proyectos import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
