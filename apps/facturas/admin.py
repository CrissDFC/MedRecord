from django.contrib import admin
from apps.facturas.models import Facturas


@admin.register(Facturas)
class FacturasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'paciente',
        'fecha',
        'medico',
        'total',
        'estado',
    )
    ordering = ['-fecha']
    list_filter = ('estado',)
    search_fields = ('paciente__cedula',)

