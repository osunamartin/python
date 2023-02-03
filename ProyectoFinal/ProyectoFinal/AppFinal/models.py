from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# A continuación se declaran los modelos del sistema..
# ..
# ..

# Videojuego representa videojuegos del sitio

class Videojuego(models.Model):
    nombre = models.CharField(max_length = 40)
    genero = models.CharField(max_length = 40)
    año_lanzamiento = models.IntegerField()

    def __str__(self):
        return f"VIDEOJUEGO: {self.nombre} - GENERO: {self.genero} - AÑO LANZAMIENTO: {self.año_lanzamiento}"

# Jugador representa jugadores miembros del sitio

class Jugador(models.Model):
    apodo = models.CharField(max_length = 15)
    email = models.EmailField()
    año_nacimiento = models.IntegerField()
    nivel = models.IntegerField()

    def __str__(self):
        return f"APODO: {self.apodo} - EMAIL: {self.email} - AÑO NACIMIENTO: {self.año_nacimiento} - NIVEL: {self.nivel}"


# Equipos para partidas casuales o competencias en Esports

class Equipos(models.Model):

    nombre = models.CharField(max_length=15)
    cantJugadores = models.IntegerField()
    competitivo = models.BooleanField()

    def __str__(self):
        return f"NOMBRE: {self.nombre} - CANT JUGADORES: {self.cantJugadores} - COMPETITIVO: {self.competitivo}"


# Desarrollador representa desarrolladores de los juegos del sitio

class Desarrollador(models.Model):
    nombre = models.CharField(max_length = 40)
    email = models.EmailField()
    rol = models.CharField(max_length = 40)
    años_experiencia = models.IntegerField()

    def __str__(self):
        return f"NOMBRE: {self.nombre} - EMAIL: {self.email} - ROL: {self.rol} - AÑOS EXPERIENCIA: {self.años_experiencia}"

# DesafioGamer representa desafíos para los Jugadores dentro del sitio

class DesafioGamer(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 240)
    puntos_xp = models.IntegerField()

    def __str__(self):
        return f"NOMBRE: {self.nombre} - DESCRIPCIÓN: {self.descripcion} - PUNTOS XP: {self.puntos_xp}"

# Avatar representa el modelo que permite a los usuarios tener avatares

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)