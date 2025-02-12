from django.contrib import admin
from apps.pacientes.models import Pacientes


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'cedula',
        'direccion',
        'telefono',
        'email',
        'created_on'
    )
    ordering = ['id']
    search_fields = ('cedula',)
