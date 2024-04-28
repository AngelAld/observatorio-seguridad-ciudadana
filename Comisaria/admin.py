from django.contrib import admin
from .models import Comisaria, MapaDelito, MapaRiesgo, InformeDelictivo


admin.site.register(Comisaria)
admin.site.register(MapaDelito)
admin.site.register(MapaRiesgo)
admin.site.register(InformeDelictivo)
