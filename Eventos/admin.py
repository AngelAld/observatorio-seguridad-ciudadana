from django.contrib import admin

from .models import Entidad, TipoEvento, Evento, Documento, Imagen

admin.site.register(Entidad)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(Documento)
admin.site.register(Imagen)
