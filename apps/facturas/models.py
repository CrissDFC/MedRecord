from django.db import models

class Facturas(models.Model):

    ESTADO_FACTURA =  (
        ('Pendiente', 'Pendiente'),
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
    )

    paciente = models.ForeignKey('pacientes.Pacientes', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    medico = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, limit_choices_to={'rol': 'medico'})
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_FACTURA, default='Pendiente')

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return str(self.id) + '-' +self.paciente.nombre + ' ' + self.paciente.apellido + '-' + str(self.fecha)
