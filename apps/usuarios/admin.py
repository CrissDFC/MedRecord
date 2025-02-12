from django.contrib import admin
from apps.usuarios.models import Usuario


@admin.register(Usuario)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rol',
    )
    ordering = ['id']
    list_filter = ['rol']
    verbose_name = 'Rol'
    verbose_name_plural = 'Roles'
