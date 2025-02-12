from django.contrib import admin
from apps.historias.models import Historias

@admin.register(Historias)
class HistoriasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'paciente',
        'medico',
        'fecha',
        'diagnostico',
        'tratamiento',
        'observaciones',
    )
    ordering = ['id']
    list_filter = ('fecha',)
    search_fields = ('paciente__cedula','medico__cedula')
