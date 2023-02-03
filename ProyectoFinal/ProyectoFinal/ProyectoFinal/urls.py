from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Se enumeran las rutas a las URL usadas en el proyecto y la aplicación
# En AppFinal/urls.py están todas las rutas de la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppFinal/', include('AppFinal.urls')),
]

# Ruta a settings para imágenes y otros tipos de media
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)