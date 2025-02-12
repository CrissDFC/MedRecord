from django.contrib import admin
from django_tenants.utils import get_tenant
from shared.models import Tenant, Domain




@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        tenant = get_tenant(request)
        return tenant.schema_name == 'public'

    def has_view_permission(self, request, obj = None):
        tenant = get_tenant(request)
        return tenant.schema_name in ['public']

    def has_change_permission(self, request, obj=None):
        """Evitar modificaciones fuera del esquema 'public'."""
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    def has_add_permission(self, request):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    def has_delete_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    list_display = (
        'id',
        'name',
        'schema_name',
        'on_trial',
        'created_on',
        'is_active'
    )
    ordering = ['id']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        tenant = get_tenant(request)
        return tenant.schema_name == "public"

    def has_view_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    def has_change_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    def has_add_permission(self, request):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    def has_delete_permission(self, request, obj=None):
        tenant = get_tenant(request)
        return tenant.schema_name in ["public"]

    list_display = (
        'id',
        'domain',
        'tenant',
    )
    ordering = ['id']