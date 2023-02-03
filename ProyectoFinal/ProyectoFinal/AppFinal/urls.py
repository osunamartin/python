from django.urls import path
from AppFinal import views
#Para el LOGOUT:
from django.contrib.auth.views import LogoutView


# Se definen todas las URL que se usan en el sitio, junto con sus vistas y sus nombres

urlpatterns = [
    
    # Inicio
    path('inicio', views.inicio, name="Inicio"),

    # Sección Videojuegos
    path('videojuegos', views.videojuegos, name="Videojuegos"),
    path('videojuegosLeer', views.videojuegosLeer, name="VideojuegosLeer"),
    path('videojuegosBusqueda', views.videojuegosBusqueda, name="VideojuegosBusqueda"),
    path('videojuegosBusquedaResultado/', views.videojuegosBusquedaResultado, name="VideojuegosBusquedaResultado"),
    path('videojuegosEditar/<videojuego_a_editar>', views.videojuegosEditar, name="VideojuegosEditar"),
    path('videojuegosEliminar/<nombre_a_borrar>', views.videojuegosEliminar, name="VideojuegosEliminar"),
    path('videojuegosFormulario', views.videojuegosFormulario, name="VideojuegosFormulario"),

    # Sección Jugadores
    path('jugadores', views.jugadores, name="Jugadores"),
    path('jugadoresLeer', views.jugadoresLeer, name="JugadoresLeer"),
    path('jugadoresBusqueda', views.jugadoresBusqueda, name="JugadoresBusqueda"),
    path('jugadoresBusquedaResultado/', views.jugadoresBusquedaResultado, name="JugadoresBusquedaResultado"),
    path('jugadoresEditar/<jugador_a_editar>', views.jugadoresEditar, name="JugadoresEditar"),
    path('jugadoresEliminar/<apodo_a_borrar>', views.jugadoresEliminar, name="JugadoresEliminar"),
    path('jugadoresFormulario', views.jugadoresFormulario, name="JugadoresFormulario"),

    # Sección Desarrolladores
    path('desarrolladores', views.desarrolladores, name="Desarrolladores"),
    path('desarroladoresLeer', views.desarrolladoresLeer, name="DesarrolladoresLeer"),
    path('desarrolladoresBusqueda', views.desarrolladoresBusqueda, name="DesarrolladoresBusqueda"),
    path('desarrolladoresBusquedaResultado/', views.desarrolladoresBusquedaResultado, name="desarrolladoresBusquedaResultado"),
    path('desarrolladoresEditar/<desarrollador_a_editar>', views.desarrolladoresEditar, name="DesarrolladoresEditar"),
    path('desarrolladoresEliminar/<nombre_a_borrar>', views.desarrolladoresEliminar, name="DesarrolladoresEliminar"),
    path('desarrolladoresFormulario', views.desarrolladoresFormulario, name="DesarrolladoresFormulario"),

    # Sección Desafios Gamer
    path('desafiosgamer', views.desafiosgamer, name="DesafiosGamer"),
    path('desafiosgamerLeer', views.desafiosgamerLeer, name="DesafiosGamerLeer"),
    path('desafiosgamerBusqueda', views.desafiosgamerBusqueda, name="DesafiosGamerBusqueda"),
    path('desafiosgamerBusquedaResultado/', views.desafiosgamerBusquedaResultado, name="DesafiosGamerBusquedaResultado"),
    path('desafiosgamerEditar/<desafiogamer_a_editar>', views.desafiosgamerEditar, name="DesafiosGamerEditar"),
    path('desafiosgamerEliminar/<nombre_a_borrar>', views.desafiosgamerEliminar, name="DesafiosGamerEliminar"),
    path('desafiosgamerFormulario', views.desafiosgamerFormulario, name="DesafiosGamerFormulario"),

    #Sección Equipos
    path('equipos', views.equipos, name="Equipos"),
    path('equiposLeer', views.equiposLeer, name="EquiposLeer"),
    path('equiposBusqueda', views.equiposBusqueda, name="EquiposBusqueda"),
    path('equiposBusquedaResultado/', views.equiposBusquedaResultado, name="EquiposBusquedaResultado"),
    path('equiposEditar/<equipo_a_editar>', views.equiposEditar, name="EquiposEditar"),
    path('equiposEliminar/<nombre_a_borrar>', views.equiposEliminar, name="EquiposEliminar"),
    path('equiposFormulario', views.equiposFormulario, name="EquiposFormulario"),
    
    #About/Nosotros
    path('about', views.about, name="About"),
    
    #Login/Registro/Avatar
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),

]

