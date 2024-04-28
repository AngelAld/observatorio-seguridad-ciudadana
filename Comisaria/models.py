from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


def mapaDelitoPath(instance, filename):
    return f"archivos/imagenes/{instance.comisaria.nombre}/mapas del delito/{filename}"


def mapaRiesgoPath(instance, filename):
    return f"archivos/imagenes/{instance.comisaria.nombre}/mapas de riesgo/{filename}"


def informeDelictivoPath(instance, filename):
    return f"archivos/documentos/{instance.comisaria.nombre}/informes delictivos/{filename}"


class Comisaria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    grupo_usuario = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class MapaDelito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to=mapaDelitoPath)
    fecha = models.DateField()
    comisaria = models.ForeignKey(Comisaria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"


class MapaRiesgo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to=mapaRiesgoPath)
    fecha = models.DateField()
    comisaria = models.ForeignKey(Comisaria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"


class InformeDelictivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    archivo = models.FileField(upload_to=informeDelictivoPath)
    fecha = models.DateField()
    comisaria = models.ForeignKey(Comisaria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"
