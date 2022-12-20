from django.db import models
from django.db.models import Q

# Create your models here.


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    def natural_key(self):
        return (self.nombre,)


class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    en_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def natural_key(self):
        return (self.nombre, )# + self.en_provincia.natural_key()
    natural_key.dependencies = ['appcore.provincia']


class EstablecimientosManager(models.Manager):
    def buscar_por_tipo(self, tipo, provincia, cp, localidad):
        result = self.none()
        if provincia != '':
            result = result.union(super().get_queryset().filter(en_localidad__en_provincia__nombre=provincia))
        if cp != '':
            result = result.union(super().get_queryset().filter(codigo_postal=cp))
        if localidad != '':
            result = result.union(super().get_queryset().filter(en_localidad__nombre=localidad))
        if provincia == '' and cp == '' and localidad == '':
            result = super().get_queryset()
        if tipo != 'T':
            result = result.filter(tipo=tipo)
        
        return result



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
    direccion = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=5, null=True)
    longitud = models.FloatField(null=True)
    latitud = models.FloatField(null=True)
    telefono = models.CharField(max_length=13, null=True)
    descripcion = models.TextField(blank=True)
    # Relaciones
    en_localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

    def __str__(self):
        if self.latitud == None:
            lat = "X"
        else:
            lat = self.latitud
        if self.longitud == None:
            lang = "X"
        else:
            lang = self.longitud
        if self.codigo_postal == None:
            postal = "X"
        else:
            postal = self.codigo_postal

        return self.nombre + ". LAT: " + str(lat) + ". LONG:" + str(lang) + ". POSTALCOODE: " + postal

    establecimientos = EstablecimientosManager()