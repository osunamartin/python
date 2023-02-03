from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Se declaran los formularios que vamos a usar en el sitio - uno para cada modelo

class DesafioGamerFormulario(forms.Form):

    nombre = forms.CharField(max_length = 20)
    descripcion = forms.CharField(max_length = 240)
    puntos_xp = forms.IntegerField()

class DesarrolladorFormulario(forms.Form):

    nombre = forms.CharField(max_length = 40)
    email = forms.EmailField()
    rol = forms.CharField(max_length = 40)
    años_experiencia = forms.IntegerField()

class JugadorFormulario(forms.Form):

    apodo = forms.CharField(max_length = 15)
    email = forms.EmailField()
    año_nacimiento = forms.IntegerField()
    nivel = forms.IntegerField()

class VideojuegoFormulario(forms.Form):

    nombre = forms.CharField(max_length = 40)
    genero = forms.CharField(max_length = 40)
    año_lanzamiento = forms.IntegerField()

class EquiposFormulario(forms.Form):

    nombre = forms.CharField(max_length=15)
    cantJugadores = forms.IntegerField()
    competitivo = forms.BooleanField(required=False)

# Para registrar usuarios

class UserRegisterForm(UserCreationForm):
    
    #Necesarios
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    #Opcionales
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']

# Para editar usuarios

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']

# Para cargar un avatar

class AvatarFormulario(forms.Form):

    imagen = forms.ImageField(required=True)