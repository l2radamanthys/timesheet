from django.contrib import admin
from timesheet.models.tareas_proyecto import TareaProyecto


class TareaProyectoAdmin(admin.ModelAdmin):
    model = TareaProyecto
    list_display = (
        'user',
        'proyecto',
        'tarea',
        'fecha',
        'horas',
    )
    autocomplete_fields = (
        'proyecto',
        'tarea',
        'user',
    )
    search_fields = (
        'user',
        'proyecto',
        'tarea',
    )
