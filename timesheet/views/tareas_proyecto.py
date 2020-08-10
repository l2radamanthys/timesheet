from rest_framework import viewsets
from rest_framework import permissions
from timesheet.models.tareas_proyecto import TareaProyecto
from timesheet.serializers.tareas_proyecto import TareaProyectoSerializer

class TareaProyectoViewSet(viewsets.ModelViewSet):
    queryset = TareaProyecto.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TareaProyectoSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
