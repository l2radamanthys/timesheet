from django.contrib import admin

from timesheet.admin_class.clientes import ClienteAdmin, Cliente
from timesheet.admin_class.proyectos import ProyectoAdmin, Proyecto
from timesheet.admin_class.tareas import TareaAdmin, Tarea
from timesheet.admin_class.tareas_proyecto import TareaProyectoAdmin, TareaProyecto


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(TareaProyecto, TareaProyectoAdmin)

# Register your models here.
