from rest_framework.viewsets import ModelViewSet
from Eventos.models import Evento
from .EventosSerializers import EventoListSerializer


class EventoListViewSet(ModelViewSet):
    serializer_class = EventoListSerializer
    queryset = Evento.objects.all()
    http_method_names = ["get"]
