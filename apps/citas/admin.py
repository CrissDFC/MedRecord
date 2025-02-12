from django.contrib import admin
from django_tenants.utils import get_tenant
from apps.citas.models import Citas


@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        tenant = get_tenant(request)
        return tenant.schema_name != 'public'

    def has_view_permission(self, request, obj = None):
        tenant = get_tenant(request)
        return tenant.schema_name not in ['public']

    def has_change_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name not in ["public"]

    def has_delete_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name not in ["public"]


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
