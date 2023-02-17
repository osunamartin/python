### Repositorio del proyecto final del Curso de Programación en Python de Coderhouse.
### LINK AL VIDEO: https://youtu.be/yjYSAyrIkng
### LINK A LOS CASOS DE PRUEBA: https://docs.google.com/document/d/1sGV3Yz8hOn9bkOrot2x4IOW5i2hBf4MD4lOE1kNC1yo/edit?usp=sharing

Este proyecto consiste de un sitio de actividades y desafíos para aficionados de los videojuegos, llamados en el proyecto como Jugadores o Gamers. Se puede visualizar los Videojuegos, Desarrolladores, Jugadores, Equipos y Desafíos Gamer registrados en la base de datos, tal como también se puede agregar nuevas entradas a cada modelo. También se pueden editar y eliminar dichas entradas. Si se quiere hacer una búsqueda específica/filtrar por una determinada cadena en lugar de visualizar todas las entradas, también es posible. Además, uno se puede registrar como usuario, logearse, editar sus datos de usuario, y cargar avatares para que se muestren en el Home.

El repositorio incluye todo el código y archivos del proyecto, incluyendo los archivos Python, los templates HTML y la misma plantilla de Bootstrap, además de la base de datos SQL. Se eligió la plantilla de Bootstrap [Simple Sidebar](https://startbootstrap.com/template/simple-sidebar) por su gran simpleza y la mayor facilidad que provee al programador estudiante para concentrarse más en Python y la pura funcionalidad back-end del proyecto que en la parte visual del sitio, léase HTML, CSS y Javascript. Aún así, se incluye una Versión 2 sin utilizar que se había seleccionado como alternativa un poco más estética y estandarizada para un sitio web común (optamos por no utilizarla más avanzado el proyecto).

## Para la navegación por el repositorio
### El repositorio incluye:
- El proyecto ProyectoFinal,
- Las plantillas de Bootstrap ya mencionadas arriba, dentro de la carpeta PlantillasBootstrap,
- Este archivo README.md

### Dentro de ProyectoFinal, se encontrará:
- La subcarpeta ProyectoFinal, contenedora de los archivos propios del proyecto de Python/Django,
- La subcarpeta AppFinal, contenedora de los archivos propios de la aplicación AppFinal desarrollada durante los Playgrounds,
- La subcarpeta media, contenedora de todos los archivos multimedia del sitio,
- La base de datos SQL,
- El manage.py,
- El requirements.txt, que describe qué paquetes usamos para el proyecto

### Dentro de AppFinal, se encontrará:
- Todos los archivos Python propios de la aplicación de Python/Django,
- La subcarpeta static, contenedora de los archivos propios del template de Bootstrap utilizado,
- La subcarpeta templates, contenedora de todas las vistas/templates HTML implementadas en la aplicación

## Vistas/Templates de AppFinal
### padre
La plantilla Bootstrap principal.

### inicio
La vista inicial o landing page del sitio. Introduce al visitante al sitio.

##### register
Para registrarse como usuario en el sitio. Solo visible si no estás logeado.

##### login
Para iniciar sesión  como usuario del sitio. Solo visible si no estás logeado.

##### logout
Para cerrar sesión. Solo visible si estás logeado.

##### editarPerfil
Para editar el email y/o la contraseña del usuario logeado. Solo visible si estás logeado.

##### agregarAvatar
Para actualizar tu avatar o agregar uno nuevo. Solo visible si estás logeado.

### about
¡Sobre nosotros!

### videojuegos
La vista relacionada con los Videojuegos.

##### videojuegosLeer
Para visualizar todos los Videojuegos en la base de datos. Desde acá también se pueden editar y eliminar (usando la view videojuegosEliminar) los Videojuegos, o bien agregar uno nuevo. Solo visible si estás logeado.

##### videojuegosEditar
Para editar un Videojuego de la base de datos. Solo visible si estás logeado.

##### videojuegosBusqueda
Para buscar Videojuegos en la base de datos usando una cadena o filtro específicos. La búsqueda filtrará los resultados y traerá los nombres de las entradas de la BDD que coincidan.

##### videojuegosBusquedaResultado
Consecuencia de videojuegosBusqueda; trae los resultados filtrados de la búsqueda realizada.

##### videojuegosFormulario
Para insertar nuevos Videojuegos a la base de datos. Si se registra correctamente, retornará a la vista videojuegos. Solo visible si estás logeado.

### desarrolladores
La vista relacionada con los Desarrolladores. 

##### desarrolladoresLeer
Para visualizar todos los Desarrolladores en la base de datos. Desde acá también se pueden editar y eliminar (usando la view desarrolladoresEliminar) los Desarrolladores, o bien agregar uno nuevo. Solo visible si estás logeado.

##### desarrolladoresEditar
Para editar un Desarrollador de la base de datos. Solo visible si estás logeado.

##### desarrolladoresBusqueda
Para buscar Desarrolladores en la base de datos usando una cadena o filtro específicos. La búsqueda filtrará los resultados y traerá los nombres de las entradas de la BDD que coincidan.

##### desarrolladoresBusquedaResultado
Consecuencia de desarrolladoresBusqueda; trae los resultados filtrados de la búsqueda realizada.

##### desarrolladoresFormulario
Para insertar nuevos Desarrolladores a la base de datos. Si se registra correctamente, retornará a la vista desarrolladores. Solo visible si estás logeado.

### jugadores
La vista relacionada con los Jugadores. 

##### jugadoresLeer
Para visualizar todos los Jugadores en la base de datos. Desde acá también se pueden editar y eliminar (usando la view jugadoresEliminar) los Jugadores, o bien agregar uno nuevo. Solo visible si estás logeado.

##### jugadoresEditar
Para editar un Jugador de la base de datos. Solo visible si estás logeado.

##### jugadoresBusqueda
Para buscar Jugadores en la base de datos usando una cadena o filtro específicos. La búsqueda filtrará los resultados y traerá los nombres de las entradas de la BDD que coincidan.

##### jugadoresBusquedaResultado
Consecuencia de jugadoresBusqueda; trae los resultados filtrados de la búsqueda realizada.

##### jugadoresFormulario
Para insertar nuevos Jugadores a la base de datos. Si se registra correctamente, retornará a la vista jugadores. Solo visible si estás logeado.

### desafiosgamer
La vista relacionada con los Desafíos Gamer.

##### desafiosgamerLeer
Para visualizar todos los Desafíos Gamer en la base de datos. Desde acá también se pueden editar y eliminar (usando la view desafiosgamerEliminar) los Desafíos Gamer, o bien agregar uno nuevo. Solo visible si estás logeado.

##### desafiosgamerEditar
Para editar un Desafío Gamer de la base de datos. Solo visible si estás logeado.

##### desafiosgamerBusqueda
Para buscar Desafíos Gamer en la base de datos usando una cadena o filtro específicos. La búsqueda filtrará los resultados y traerá los nombres de las entradas de la BDD que coincidan.

##### esafiosgamerBusquedaResultado
Consecuencia de desafiosgamerBusqueda; trae los resultados filtrados de la búsqueda realizada.

##### desafiosgamerFormulario
Para insertar nuevos Desafíos Gamer a la base de datos. Si se registra correctamente, retornará a la vista desafiosgamer. Solo visible si estás logeado.

### equipos
La vista relacionada con los Equipos.

##### equiposLeer
Para visualizar todos los Equipos en la base de datos. Desde acá también se pueden editar y eliminar (usando la view equiposEliminar) los Equipos, o bien agregar uno nuevo. Solo visible si estás logeado.

##### equiposditar
Para editar un Equipos de la base de datos. Solo visible si estás logeado.

##### equiposBusqueda
Para buscar Equipos en la base de datos usando una cadena o filtro específicos. La búsqueda filtrará los resultados y traerá los nombres de las entradas de la BDD que coincidan.

##### equiposBusquedaResultado
Consecuencia de equiposBusqueda; trae los resultados filtrados de la búsqueda realizada.

##### equiposFormulario
Para insertar nuevos Equipos a la base de datos. Si se registra correctamente, retornará a la vista equipos. Solo visible si estás logeado.

## Problemas conocidos y soluciones

### • *AssertionError at /AppFinal/inicio. Negative indexing is not supported.*
**PROBLEMA:** Este error está relacionado con la implementación de los avatares. Ocurrirá cuando intentes entrar a la vista inicio como un usuario logeado sin un avatar cargado. Si un usuario no tiene ningún avatar cargado, la implementación que vimos en clase para siempre mostrar el último avatar resulta en una iteración fuera de índice/rango o indexación negativa no soportada. Si el usuario tiene un avatar cargado, sin embargo, la página funcionará completamente.

**SOLUCIÓN:** Acceder por ruta directamente a /AppFinal/agregarAvatar y cargar un avatar para el usuario logeado.

## Para la navegación por el sitio

Para ingresar al sitio, abrir el proyecto en el editor (por defecto usamos Visual Studio Code) y correr el servidor local ejecutando en la terminal el comando `python manage.py runserver`. Una vez esté corriendo el servidor, dirigirse a http://127.0.0.1:8000/AppFinal/inicio para ingresar.

Para navegar por las distintas vistas del proyecto, simplemente utilizar el Menu Lateral. El Menu Lateral se puede activar y desactivar usando el botón azul de Ocultar/Mostrar Menu Lateral. Si una vista tiene subvistas, se podrá acceder a ellas desde la supervista o vista principal, usando el botón gris. Para volver para atrás, usar el botón gris de Volver en la parte superior de la subvista.

Se puede acceder a las secciones y vistas correspondientes de Registro, Login, Logout, Editar Perfil, y Agregar Avatar desde la barra de navegación superior.

Adicionalmente, también se puede navegar entre secciones y vistas ingresando la ruta pura en la barra de navegación del navegador.

El proyecto fue testeado usando Google Chrome, Microsoft Edge y Mozilla Firefox.

## Integrantes del equipo

**Mario Facundo Serra** tiene 22 años. Es técnico de soporte IT y estudiante de programación. Para este Proyecto Final, hizo los modelos y vistas para Videojuegos, Desarrolladores, Jugadores y Desafíos Gamer junto con sus respectivos CRUD, desarrolló la funcionalidad de avatares para los usuarios, y escribió el documento README.md y los casos de prueba.

**Martin Osuna** tiene 25 años. Es ilusionista y aspirante a programador. Se encargó de realizar el modelo Equipos con sus respectivos CRUD junto con la parte del Login/Registro/Logout/Edición de Perfil y esta pestaña de información. Es también quien grabó el video de muestra adjunto al trabajo, describiendo las funciones de la web.

# ¡Muchas gracias!
