from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from AppFinal.forms import * 


from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# A continuación se definen todas las vistas que le dan interfaz al sitio..
# ..
# ..

# Home
# ..

# inicio representa la home del sitio
def inicio(request):
    diccionario = {}
    cantidad_de_avatares = 0

    # Se muestra siempre el último avatar del usuario
    # NOTA: A causa de esta implementación específica, los usuarios SIEMPRE tienen que tener un avatar cargado
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        for a in avatar:
            cantidad_de_avatares = cantidad_de_avatares + 1
        diccionario["avatar"] = avatar[cantidad_de_avatares -1].imagen.url

    return render(request, 'AppFinal/inicio.html', diccionario)

# Videojuegos
# ..

# videojuegos representa la página donde se muestran los videojuegos
def videojuegos(request):
    return render(request, 'AppFinal/videojuegos.html')

# videojuegosLeer representa la página donde se ven todos los videojuegos registrados
@login_required
def videojuegosLeer(request):
    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos":videojuegos}
    return render(request, "AppFinal/videojuegosLeer.html", contexto)

# videojuegosBusqueda representa la página donde se pueden buscar videojuegos ya existentes
def videojuegosBusqueda(request):
    return render(request, 'AppFinal/videojuegosBusqueda.html')

# videojuegosBusquedaResultado representa la página donde se ven los resultados de videojuegosBusqueda
def videojuegosBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        videojuegos = Videojuego.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/videojuegosBusquedaResultado.html', {"videojuegos":videojuegos, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Videojuego"
    return HttpResponse(output)

#videojuegosEditar representa la vista usada para editar un videojuego
@login_required
def videojuegosEditar(request, videojuego_a_editar):
    # Traemos al videojuego que queremos editar
    videojuego = Videojuego.objects.get(nombre=videojuego_a_editar)

     # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            videojuego.nombre=input['nombre']
            videojuego.genero=input['genero']
            videojuego.año_lanzamiento=input['año_lanzamiento']
            videojuego.save()
            return render(request, 'AppFinal/videojuegos.html') # Sustituir por una vista de "Videojuego creado" o algo así en el futuro
    else:
        formulario = VideojuegoFormulario(initial={"nombre":videojuego.nombre, "genero":videojuego.genero, "año_lanzamiento":videojuego.año_lanzamiento})
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/videojuegosEditar.html', {'formulario':formulario, "videojuego_a_editar":videojuego_a_editar})

# videojuegosEliminar representa la vista usada para eliminar a un videojuego
@login_required
def videojuegosEliminar(request, nombre_a_borrar):
    videojuego_a_borrar = Videojuego.objects.get(nombre=nombre_a_borrar)
    videojuego_a_borrar.delete()

    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos":videojuegos}
    return render(request, "AppFinal/videojuegosLeer.html", contexto)

# videojuegosFormulario representa la página donde se pueden crear nuevos videojuegos
# Recibe los valores a través de videojuegosFormulario.html
@login_required
def videojuegosFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            videojuego = Videojuego(nombre=input['nombre'], genero=input['genero'], año_lanzamiento=input['año_lanzamiento'])
            videojuego.save()
            return render(request, 'AppFinal/videojuegos.html') # Sustituir por una vista de "Videojuego creado" o algo así en el futuro
    else:
        formulario = VideojuegoFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/videojuegosFormulario.html', {'formulario':formulario})

# Desarrolladores
# ..

#About/Nosotros

def about(request):
    return render(request, 'AppFinal/about.html')

# desarrolladores representa la página donde se muestran los desarrolladores
def desarrolladores(request):
    return render(request, 'AppFinal/desarrolladores.html')

# desarrolladoresLeer representa la página donde se ven todos los desarrolladores registrados
@login_required
def desarrolladoresLeer(request):
    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores":desarrolladores}
    return render(request, "AppFinal/desarrolladoresLeer.html", contexto)

# desarrolladoresBusqueda representa la página donde se pueden buscar desarrolladores ya existentes
def desarrolladoresBusqueda(request):
    return render(request, 'AppFinal/desarrolladoresBusqueda.html')

# desarrolladoresBusquedaResultado representa la página donde se ven los resultados de desarrolladoresBusqueda
def desarrolladoresBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        desarrolladores = Desarrollador.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/desarrolladoresBusquedaResultado.html', {"desarrolladores":desarrolladores, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Desarrollador"
    return HttpResponse(output)

#desarrolladoresEditar representa la vista usada para editar un desarrollador
@login_required
def desarrolladoresEditar(request, desarrollador_a_editar):
    # Traemos al desarrollador que queremos editar
    desarrollador = Desarrollador.objects.get(nombre=desarrollador_a_editar)

     # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesarrolladorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desarrollador.nombre=input['nombre']
            desarrollador.email=input['email']
            desarrollador.rol=input['rol']
            desarrollador.años_experiencia=input['años_experiencia']
            desarrollador.save()
            return render(request, 'AppFinal/desarrolladores.html') # Sustituir por una vista de "Desarrollador creado" o algo así en el futuro
    else:
        formulario = DesarrolladorFormulario(initial={"nombre":desarrollador.nombre, "email":desarrollador.email, "rol":desarrollador.rol, "años_experiencia":desarrollador.años_experiencia})
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desarrolladoresEditar.html', {'formulario':formulario, "desarrollador_a_editar":desarrollador_a_editar})

# desarrolladoresEliminar representa la vista usada para eliminar a un desarrollador
@login_required
def desarrolladoresEliminar(request, nombre_a_borrar):
    desarrollador_a_borrar = Desarrollador.objects.get(nombre=nombre_a_borrar)
    desarrollador_a_borrar.delete()

    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores":desarrolladores}
    return render(request, "AppFinal/desarrolladoresLeer.html", contexto)

# desarrolladoresFormulario representa la página donde se pueden crear nuevos desarrolladores
# Recibe los valores a través de desarrolladoresFormulario.html
@login_required
def desarrolladoresFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesarrolladorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desarrollador = Desarrollador(nombre=input['nombre'], email=input['email'], rol=input['rol'], años_experiencia=input['años_experiencia'])
            desarrollador.save()
            return render(request, 'AppFinal/desarrolladores.html') # Sustituir por una vista de "Desarrollador creado" o algo así en el futuro
    else:
        formulario = DesarrolladorFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desarrolladoresFormulario.html', {'formulario':formulario})

# Jugadores
# ..

# jugadores representa la página donde se muestran los jugadores
def jugadores(request):
    return render(request, 'AppFinal/jugadores.html')

# jugadoresLeer representa la página donde se ven todos los jugadores registrados
@login_required
def jugadoresLeer(request):
    jugadores = Jugador.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request, "AppFinal/jugadoresLeer.html", contexto)

# jugadoresBusqueda representa la página donde se puede buscar un jugador en particular
def jugadoresBusqueda(request):
    return render(request, 'AppFinal/jugadoresBusqueda.html')

# jugadoresBusquedaResultado representa la página donde se ven los resultados de jugadoresBusqueda
def jugadoresBusquedaResultado(request):
    if request.GET["apodo"]:
        apodo = request.GET["apodo"]
        jugadores = Jugador.objects.filter(apodo__icontains=apodo)
        return render(request, 'AppFinal/jugadoresBusquedaResultado.html', {"jugadores":jugadores, "apodo":apodo})
    else:
        output = f"ERROR: No se ingresó ningún apodo de Jugador"
    return HttpResponse(output)

#jugaadoresEditar representa la vista usada para editar un jugador
@login_required
def jugadoresEditar(request, jugador_a_editar):
    # Traemos al jugador que queremos editar
    jugador = Jugador.objects.get(apodo=jugador_a_editar)

     # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            jugador.apodo=input['apodo']
            jugador.email=input['email']
            jugador.año_nacimiento=input['año_nacimiento']
            jugador.nivel=input['nivel']
            jugador.save()
            return render(request, 'AppFinal/jugadores.html') # Sustituir por una vista de "Jugador creado" o algo así en el futuro
    else:
        formulario = JugadorFormulario(initial={"apodo":jugador.apodo, "email":jugador.email, "año_nacimiento":jugador.año_nacimiento, "nivel":jugador.nivel})
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/jugadoresEditar.html', {'formulario':formulario, "jugador_a_editar":jugador_a_editar})

# jugadoresEliminar representa la vista usada para eliminar a un jugador
@login_required
def jugadoresEliminar(request, apodo_a_borrar):
    jugador_a_borrar = Jugador.objects.get(apodo=apodo_a_borrar)
    jugador_a_borrar.delete()

    jugadores = Jugador.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request, "AppFinal/jugadoresLeer.html", contexto)

# jugadoresFormulario representa la página donde se pueden crear nuevos jugadores
# Recibe los valores a través de jugadoresFormulario.html
@login_required
def jugadoresFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            jugador = Jugador(apodo=input['apodo'], email=input['email'], año_nacimiento=input['año_nacimiento'], nivel=input['nivel'])
            jugador.save()
            return render(request, 'AppFinal/jugadores.html') # Sustituir por una vista de "Jugador creado" o algo así en el futuro
    else:
        formulario = JugadorFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/jugadoresFormulario.html', {'formulario':formulario})

# Desafios Gamer
# ..

# desafiosgamer representa la página donde se muestran los desafíos gamer
def desafiosgamer(request):
    return render(request, 'AppFinal/desafiosgamer.html')

# desafiosgamerLeer representa la página donde se ven todos los desafios gamer registrados
@login_required
def desafiosgamerLeer(request):
    desafiosgamer = DesafioGamer.objects.all()
    contexto = {"desafiosgamer":desafiosgamer}
    return render(request, "AppFinal/desafiosgamerLeer.html", contexto)

# desafiosgamerBusqueda representa la página donde se pueden buscar desafíos ya existentes
def desafiosgamerBusqueda(request):
    return render(request, 'AppFinal/desafiosgamerBusqueda.html')

# desafiosgamerBusquedaResultado representa la página donde se ven los resultados de desafiosgamerBusqueda
def desafiosgamerBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        desafiosgamer = DesafioGamer.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/desafiosgamerBusquedaResultado.html', {"desafiosgamer":desafiosgamer, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Desafío Gamer"
    return HttpResponse(output)

#desafiosgamerEditar representa la vista usada para editar un desafio gamer
@login_required
def desafiosgamerEditar(request, desafiogamer_a_editar):
    # Traemos al desafio gamer que queremos editar
    desafiogamer = DesafioGamer.objects.get(nombre=desafiogamer_a_editar)

     # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesafioGamerFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desafiogamer.nombre=input['nombre']
            desafiogamer.descripcion=input['descripcion']
            desafiogamer.puntos_xp=input['puntos_xp']
            desafiogamer.save()            
            return render(request, 'AppFinal/desafiosgamer.html') # Sustituir por una vista de "Desafio Gamer creado" o algo así en el futuro
    else:
        formulario = DesafioGamerFormulario(initial={"nombre":desafiogamer.nombre, "descripcion":desafiogamer.descripcion, "puntos_xp":desafiogamer.puntos_xp})
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desafiosgamerEditar.html', {'formulario':formulario, "desafiogamer_a_editar":desafiogamer_a_editar})

# desafiosgamerEliminar representa la vista usada para eliminar un desafio gamer
@login_required
def desafiosgamerEliminar(request, nombre_a_borrar):
    desafio_a_borrar = DesafioGamer.objects.get(nombre=nombre_a_borrar)
    desafio_a_borrar.delete()

    desafiosgamer = DesafioGamer.objects.all()
    contexto = {"desafiosgamer":desafiosgamer}
    return render(request, "AppFinal/desafiosgamerLeer.html", contexto)

# desafiosgamerFormulario representa la página donde se pueden crear nuevos desafíos gamer
@login_required
def desafiosgamerFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesafioGamerFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desafiogamer = DesafioGamer(nombre=input['nombre'], descripcion=input['descripcion'], puntos_xp=input['puntos_xp'])
            desafiogamer.save()
            return render(request, 'AppFinal/desafiosgamer.html') # Sustituir por una vista de "Desafío creado" o algo así en el futuro
    else:
        formulario = DesafioGamerFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desafiosgamerFormulario.html', {'formulario':formulario})

def equipos(request):
    return render(request, 'AppFinal/equipos.html')

#Leer Equipos:
@login_required
def equiposLeer(request):
    equipos = Equipos.objects.all()
    contexto = {"equipos":equipos}
    return render(request, "AppFinal/equiposLeer.html", contexto)

#Formulario de Equipos
@login_required
def equiposFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = EquiposFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            equipoInsta = Equipos(nombre=input['nombre'], cantJugadores=input['cantJugadores'], competitivo=input['competitivo'])
            equipoInsta.save()
            return render(request, 'AppFinal/equipos.html') 
    else:
        formulario = EquiposFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/equiposFormulario.html', {'formulario':formulario})

#Buscar Equipos
def equiposBusqueda(request):
    return render(request, 'AppFinal/equiposBusqueda.html')

def equiposBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        equipos = Equipos.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/equiposBusquedaResultado.html', {"equipos":equipos, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de equipo"
    return HttpResponse(output)

#equiposEditar representa la vista usada para editar un equipo
@login_required
def equiposEditar(request, equipo_a_editar):
    # Traemos al equipo que queremos editar
    equipo = Equipos.objects.get(nombre=equipo_a_editar)

     # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = EquiposFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            equipo.nombre=input['nombre']
            equipo.cantJugadores=input['cantJugadores']
            equipo.competitivo=input['competitivo']
            equipo.save()
            return render(request, 'AppFinal/equipos.html') # Sustituir por una vista de "Equipo creado" o algo así en el futuro
    else:
        formulario = EquiposFormulario(initial={"nombre":equipo.nombre, "cantJugadores":equipo.cantJugadores, "competitivo":equipo.competitivo})
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/equiposEditar.html', {'formulario':formulario, "equipo_a_editar":equipo_a_editar})

#Eliminar equipos
@login_required
def equiposEliminar(request, nombre_a_borrar):
    equipo_a_borrar = Equipos.objects.get(nombre=nombre_a_borrar)
    equipo_a_borrar.delete()

    equipos = Equipos.objects.all()
    contexto = {"equipos":equipos}
    return render(request, "AppFinal/equiposLeer.html", contexto)

'''class EquiposDetalle(DetailView):

    model = Equipos
    template_name = "AppFinal/equipos_detalle.html"'''

#Login

def login_request(request):

    if request.method=="POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:

                login(request, user)

                return render(request, "AppFinal/inicio.html", {"mensaje":f"Bienvenido, {usuario}"})
            
            else:

                return render(request, "AppFinal/inicio.html", {"mensaje":f"Error, ingrese nuevamente."})

        else:

            return render(request, "AppFinal/inicio.html", {"mensaje":"Error de formulario."})



    form = AuthenticationForm()

    return render(request, "AppFinal/login.html", {"form":form} )

#Registro

def register(request):

    if request.method=="POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            form.save()

            return render(request, "AppFinal/inicio.html", {"mensaje": f"{username} Creado"})

    else:

        form = UserRegisterForm()

    return render(request, "AppFinal/register.html", {"form":form})

#Editar Perfil

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppFinal/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


# agregarAvatar representa la vista usada para cargar una imagen de usuario/avatar
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = User.objects.get(username=request.user)
            avatar = Avatar(user=usuario, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppFinal/inicio.html")
    else:
        formulario = AvatarFormulario()
    return render(request, "AppFinal/agregarAvatar.html", {"formulario":formulario})