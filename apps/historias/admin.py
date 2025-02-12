from django.contrib import admin
from django_tenants.utils import get_tenant
from apps.historias.models import Historias

@admin.register(Historias)
class HistoriasAdmin(admin.ModelAdmin):
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
        'diagnostico',
        'tratamiento',
        'observaciones',
    )
    ordering = ['id']
    list_filter = ('fecha',)
    search_fields = ('paciente__cedula','medico__cedula')
