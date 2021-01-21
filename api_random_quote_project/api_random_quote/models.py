from django.db import models

# Create your models here.
class Cita(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha = models.CharField(max_length=50)