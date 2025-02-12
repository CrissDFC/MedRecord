from django.db import models

class Historias(models.Model):
    paciente = models.ForeignKey('pacientes.Pacientes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, limit_choices_to={'rol': 'medico'})
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'

    def __str__(self):
        return self.paciente.nombre + ' ' + self.paciente.apellido + '-' + str(self.fecha)