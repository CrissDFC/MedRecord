from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass
