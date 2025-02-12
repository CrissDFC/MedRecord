from django.db import models

class Citas(models.Model):

    ESTADOS =  (
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
        ('Atendida', 'Atendida'),
    )

    paciente = models.ForeignKey('pacientes.Pacientes', on_delete=models.CASCADE)
    medico = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, limit_choices_to={'rol': 'medico'})
    fecha = models.DateTimeField()
    motivo = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente' )

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

    def __str__(self):
        return self.paciente.nombre + ' ' + self.paciente.apellido + '-' + str(self.fecha)
