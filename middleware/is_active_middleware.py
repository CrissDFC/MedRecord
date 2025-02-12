from django.http import HttpResponseForbidden
from django_tenants.utils import get_tenant


class ActiveTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = get_tenant(request)

        # Verificamos si el tenant está inactivo
        if tenant and tenant.is_active is False:
            return HttpResponseForbidden('Dominio Deshabilitado, comuniquese con su proveedor')

        response = self.get_response(request)
        return response