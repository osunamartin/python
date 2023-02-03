from django.contrib import admin
from .models import *

# Se registran los modelos que necesitamos administrar
admin.site.register(Videojuego)
admin.site.register(Jugador)
admin.site.register(Desarrollador)
admin.site.register(DesafioGamer)
admin.site.register(Equipos)
admin.site.register(Avatar)