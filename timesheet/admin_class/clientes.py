from django.contrib import admin
from timesheet.models.clientes import Cliente


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = (
        'nombre',
    )
    search_fields = ('nombre', )
