from django.db import models
from django.contrib.auth.models import Group

# Create your models here.


def documentoPath(instance, filename):
    return f"archivos/documentos/{instance.evento.entidad.nombre}/{instance.evento.tipo_evento.nombre}/{filename}"


def imagenPath(instance, filename):
    return f"archivos/imagenes/{instance.evento.entidad.nombre}/{instance.evento.tipo_evento.nombre}/{filename}"


class Entidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    grupo_usuario = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)
    entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)

    @property
    def descripcion_truncada(self):
        return self.descripcion[:100] + "..."

    @property
    def imagen_destacada(self):
        imagen = Imagen.objects.filter(evento=self, is_destacada=True).first()
        if imagen:
            return "http://127.0.0.1:8000" + imagen.imagen.url

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"


class Documento(models.Model):
    archivo = models.FileField(upload_to=documentoPath)
    descripcion = models.CharField(max_length=200)
    is_acta = models.BooleanField(default=False)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion} - {self.evento.titulo}"


class Imagen(models.Model):
    imagen = models.ImageField(upload_to=imagenPath)
    descripcion = models.CharField(max_length=200)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    is_destacada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion} - {self.evento.titulo}"
