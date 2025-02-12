from django.contrib import admin
from apps.citas.models import Citas


@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'paciente',
        'medico',
        'fecha',
        'motivo',
        'estado',
    )
    ordering = ['-fecha']
    list_filter = ('estado',)
    search_fields = ('paciente__cedula',)
    verbose_name = 'Cita'
    verbose_name_plural = 'Citas'
