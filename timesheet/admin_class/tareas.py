from django.contrib import admin
from timesheet.models.tareas import Tarea


class TareaAdmin(admin.ModelAdmin):
    model = Tarea
    list_display = (
        'nombre',
    )
    search_fields = ('nombre', )
