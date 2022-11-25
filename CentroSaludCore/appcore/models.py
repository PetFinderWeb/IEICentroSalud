from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    en_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Establecimiento_Sanitario(models.Model):
    HOSPITAL = 'H'
    CENTROSALUD = 'C'
    OTROS = 'O'
    TIPO = [
        (HOSPITAL, 'Hospital'),
        (CENTROSALUD, 'Centro de Salud'),
        (OTROS, 'Otros'),
    ]
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=1, choices=TIPO, default=OTROS)
    direccion = models.CharField(max_length = 150)
    codigo_postal = models.CharField(max_length=5 , null = True)
    longitud= models.FloatField()
    latitud = models.FloatField()
    telefono = models.CharField(max_length=13, null=True)
    descripcion = models.TextField(blank=True)
    # Relaciones
    en_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre