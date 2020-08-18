from django.contrib import admin
from timesheet.models.proyectos import Proyecto


class ProyectoAdmin(admin.ModelAdmin):
    model = Proyecto
    list_display = (
        'nombre',
        'cliente',
    )
    search_fields = ('nombre', 'cliente',)
    autocomplete_fields = ('cliente',)
