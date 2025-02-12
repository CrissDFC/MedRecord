from django.contrib import admin
from django_tenants.utils import get_tenant
from apps.usuarios.models import Usuario


@admin.register(Usuario)
class ModelNameAdmin(admin.ModelAdmin):
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
        'rol',
    )
    ordering = ['id']
    list_filter = ['rol']
    verbose_name = 'Rol'
    verbose_name_plural = 'Roles'
