from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from timesheet.models.tareas import Tarea
from timesheet.serializers.tareas import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TareaSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset
