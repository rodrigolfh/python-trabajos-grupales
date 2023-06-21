# python-trabajos-grupales
Ejercicios Grupales

Cada ejercicio está en la carpeta correspondiente según el módulo.

Telovendo

Nuestro proyecto Telovendo es una aplicación básica de testeo de funcionalidades de django base.
La mayor parte de las funcionalidades vienen de la app 'account':

Se crean 3 tipos de usuario: Invitado, Usuario y Administrador
Se les asignan al menos 4 permisos a cada uno. De los permisos que dispone Django, se determina que si, por necesidad, deben otorgarse al menos 4 permisos, se les dará acceso a solo 4 permisos de solo lectura. 

----------------------------------------------------------------
Pregunta Tarea Grupal 6:
¿Cómo agregar usuarios de forma dinámica, sin usar de por medio el panel de administración?

Para lograrlo, empleamos los formularios creados para estos fines.
Para crear un formulario de creación de usuario estándar (es decir, el base de django), necesitamos 4 cosas:
-Un formulario HTML (forms.py) almacenado en la app del proyecto, este estará basado en el recurso .UserCreationForm de django y tendrá los campos que nosotros determinemos, los cuales irán a parar a la vista para ser procesados.
-Modificar nuestro archivo views.py para que contenga el código necesario para procesar el request entrante mediante ese formulario enviado

----------------------------------------------------------------

Views:
    index: Muestra una página de inicio con una lista de usuarios.

    pg2: Muestra una página que requiere inicio de sesión y muestra una lista de usuarios.

    crear_proveedor: Permite crear un proveedor utilizando un formulario y guarda la información ingresada en la base de datos.

    login_view: Permite a los usuarios iniciar sesión y redirige a la página de bienvenida si las credenciales son válidas.

    bienvenida_view: Muestra una página de bienvenida después de que el usuario ha iniciado sesión.

    logout_view: Cierra la sesión del usuario y muestra una página de cierre de sesión.

    forms: Permite a los administradores crear usuarios a través de un formulario y los asigna a un grupo específico.

    cliente_form_view: Permite a los usuarios crear un cliente a través de un formulario y los asigna a un grupo específico.


Restricciones

-Se incluyeron dos restricciones, que se utilizaron en más de un view:

    @login_required: Requiere que el usuario haya iniciado sesión para acceder a la vista.

    @permission_required('Administradores'): Requiere que el usuario tenga el permiso de "Administradores" para acceder a la vista.


Contraseñas:

admin:admin (superusuario)

test:contraseña1 (Cliente)



STATIC & BOOTSTRAP:

- Se dispuso un archivo /css/estilos.css en la carpeta estática ubicada en account/static, en adición al CDN de bootstrap en el template base.html.



