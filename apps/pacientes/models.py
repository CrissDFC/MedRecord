from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField('Nombre',max_length=50 )
    apellido = models.CharField('Apellido',max_length=50 )
    cedula = models.CharField('Cedula',max_length=10, unique=True )
    direccion = models.CharField('Direccion',max_length=100)
    telefono = models.CharField('Telefono',max_length=10)
    email = models.EmailField('Email',max_length=50, unique=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    genero = models.CharField('Genero',max_length=10)
    created_on = models.DateTimeField('Fecha de creacion',auto_now_add=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nombre + ' ' + self.apellido + '-' + self.cedula

