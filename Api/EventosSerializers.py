from Eventos.models import Documento, Entidad, Evento, Imagen, TipoEvento
from rest_framework.serializers import ModelSerializer, StringRelatedField


class EventoListSerializer(ModelSerializer):

    portada = StringRelatedField(source="imagen_destacada", read_only=True)
    descripcion_truncada = StringRelatedField(read_only=True)

    class Meta:
        model = Evento
        fields = ["id", "titulo", "descripcion_truncada", "portada"]
