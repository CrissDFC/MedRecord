from django.contrib import admin
from django_tenants.utils import get_tenant
from apps.facturas.models import Facturas


@admin.register(Facturas)
class FacturasAdmin(admin.ModelAdmin):
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
        'fecha',
        'medico',
        'total',
        'estado',
    )
    ordering = ['-fecha']
    list_filter = ('estado',)
    search_fields = ('paciente__cedula',)

