from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
import json
from timesheet.serializers.tareas_proyecto import TareaProyectoSerializer
from timesheet.models.tareas_proyecto import TareaProyecto
from timesheet.models.proyectos import Proyecto
from timesheet.models.tareas import Tarea
from django.contrib.auth.models import User


class TareaProyectoViewSet(viewsets.ModelViewSet):
    queryset = TareaProyecto.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TareaProyectoSerializer

    def get_queryset(self):
        queryset = self.queryset
        desde = self.request.query_params.get('desde', None)
        hasta = self.request.query_params.get('hasta', None)
        user_id = self.request.query_params.get('user_id', None)

        if user_id:
            queryset = queryset.filter(user__id=user_id)

        if desde:
            queryset = queryset.filter(fecha__gte=desde)

        if hasta:
            queryset = queryset.filter(fecha__lte=hasta)

        return queryset

    @action(detail=False, methods=['post'], url_path='actualizar')
    def agregar_tareas_proyecto(self, request, *args, **kwargs):
        datos = json.loads(request.body)
        tareas = json.loads(datos.get('tareas', None))
        # print(tareas)
        agregadas = 0
        actualizadas = 0
        borradas = 0

        for tarea in tareas:
            try:
                tarea_proy = TareaProyecto.objects.get(
                    user__id=tarea.get('user_id', None),
                    proyecto__id=tarea.get('proyecto_id', None),
                    tarea__id=tarea.get('tarea_id', None),
                    fecha=tarea.get('fecha', None)
                )
                if tarea.get('horas', 0) != 0:
                    tarea_proy.horas = tarea.get('horas', None)
                    tarea_proy.save()
                    actualizadas += 1
                else:
                    tarea_proy.delete()
                    borradas += 1

            except TareaProyecto.DoesNotExist:
                if tarea.get('horas', 0) != 0:
                    proyecto = Proyecto.objects.get(id=tarea.get('proyecto_id', None))
                    tarea_ = Tarea.objects.get(id=tarea.get('tarea_id', None))
                    user = User.objects.get(id=tarea.get('user_id', None))

                    TareaProyecto.objects.create(
                        user=user,
                        tarea=tarea_,
                        proyecto=proyecto,
                        fecha=tarea.get('fecha', None),
                        horas=tarea.get('horas', None)
                    )
                    agregadas += 1

        return Response({
            'ok': True,
            'agregadas': agregadas,
            'actualizadas': actualizadas,
            'borradas': borradas
        })
