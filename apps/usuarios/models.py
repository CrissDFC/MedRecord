from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(models.Model):
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('medico', 'Médico'),
        ('recepcionista', 'Recepcionista'),
    ]
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=500, choices=ROL_CHOICES)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.primer_nombre} ({self.rol})"

