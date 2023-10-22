# learning_FastAPI_REST
 aprendiento y mejorando mis habilidades en la programacion backent

## Tecnologias
 sqlalchemy, FastAPI, Sqlite

## Comandos
 Start app
  ~~~python
  uvicorn main:app --reload
  ~~~
 generar e Instalar las dependecias del proyecto
  ~~~
  python -m pip freeze > requirements.txt
  python -m pip install -r requirements.txt
  ~~~
  

## parte 1: Casos de Uso para API de Autenticación y Autorización
 Crea una API de autenticación y autorización que permita a los usuarios registrarse, iniciar sesión y gestionar sus perfiles. Asegúrate de implementar un sistema seguro de gestión de tokens.

- [ ] Registro de usuario: Permite a los usuarios registrarse en la aplicación proporcionando su información básica, como nombre, dirección de correo electrónico y contraseña.

- [ ] Inicio de sesión: Los usuarios pueden iniciar sesión en la aplicación proporcionando sus credenciales (correo electrónico y contraseña) para acceder a su cuenta.

- [ ] Restablecimiento de contraseña: En caso de olvidar la contraseña, los usuarios pueden solicitar un restablecimiento de contraseña a través de la API. Recibirán un enlace de restablecimiento en su correo electrónico.

- [ ] Actualización de perfil: Los usuarios pueden actualizar su perfil, lo que incluye cambiar su contraseña, actualizar su dirección de correo electrónico o editar otros detalles de su cuenta.

- [ ] Cerrar sesión: Los usuarios pueden cerrar sesión de su cuenta para proteger su privacidad.

- [ ] Gestión de tokens de acceso: La API debe emitir tokens de acceso seguros (como JWT) al usuario tras la autenticación, y gestionar la expiración y renovación de estos tokens.

- [ ] Autorización basada en roles: La API debe admitir la asignación de roles a los usuarios (por ejemplo, administrador, usuario estándar) y permitir la autorización de recursos y acciones en función de estos roles.

- [ ] Protección de rutas y recursos: La API debe proteger las rutas y recursos, asegurando que solo los usuarios autenticados y autorizados puedan acceder a ciertas partes de la aplicación.

- [ ] Registro de actividad de inicio de sesión: Registrar y notificar al usuario sobre actividades inusuales o inicios de sesión desde ubicaciones no habituales.

- [ ] Revocación de tokens: Permitir a los usuarios revocar sus tokens de acceso si consideran que su cuenta está comprometida.

- [ ] Autenticación de dos factores (2FA): Ofrecer soporte para la autenticación de dos factores, como el envío de códigos de verificación por mensaje de texto o correo electrónico.

- [ ] Integración de proveedores de inicio de sesión externos: Permitir a los usuarios iniciar sesión a través de servicios externos como Google, Facebook o Twitter.

- [ ] Restricciones de acceso por IP: Permitir o denegar el acceso basado en direcciones IP específicas o rangos de direcciones IP.

- [ ] Auditoría y registro de eventos: Registrar eventos de autenticación y autorización para fines de auditoría y seguridad.

- [ ] Políticas de seguridad personalizadas: Permitir a los administradores configurar políticas de seguridad personalizadas, como contraseñas fuertes o caducidad de contraseñas.

- [ ] Bloqueo de cuentas: Implementar un mecanismo de bloqueo de cuentas después de varios intentos fallidos de inicio de sesión para prevenir ataques de fuerza bruta.

## parte 2: Casos de Uso para API de Tareas (To-Do)

- [ ] Crear una tarea: Los usuarios pueden utilizar la API para crear nuevas tareas pendientes. Deben proporcionar un título y, opcionalmente, una descripción, una fecha de vencimiento y otras etiquetas relevantes.

- [ ] Obtener lista de tareas: Los usuarios pueden recuperar una lista de todas sus tareas pendientes. Esto les permite ver todas las tareas que tienen por hacer.

- [ ] Marcar una tarea como completada: Los usuarios pueden utilizar la API para cambiar el estado de una tarea de "pendiente" a "completada". Esto es útil cuando han terminado una tarea.

- [ ] Actualizar una tarea: Los usuarios pueden modificar una tarea existente. Pueden editar el título, la descripción, la fecha de vencimiento u otros detalles de la tarea.

- [ ] Eliminar una tarea: Los usuarios pueden eliminar una tarea de su lista si ya no es relevante o necesaria.

- [ ] Filtrar tareas por estado: Los usuarios pueden consultar la API para obtener una lista de tareas pendientes o completadas específicas. Por ejemplo, pueden buscar todas las tareas completadas en el último mes.

- [ ] Ordenar tareas: Los usuarios pueden ordenar su lista de tareas por diferentes criterios, como fecha de vencimiento, prioridad o fecha de creación.

- [ ] Agregar etiquas a tareas: Los usuarios pueden asignar etiquetas a sus tareas para organizarlas mejor. Pueden buscar tareas por etiquetas específicas.

- [ ] Establecer recordatorios: La API puede admitir la programación de recordatorios o notificaciones para tareas con fechas de vencimiento, de modo que los usuarios reciban recordatorios o alertas.

- [ ] Compartir tareas: Los usuarios pueden compartir tareas con otros usuarios a través de la API, lo que permite la colaboración en proyectos o actividades.

- [ ] Archivar tareas: Los usuarios pueden archivar tareas completadas o antiguas, de modo que no aparezcan en su lista principal de tareas pendientes, pero aún sean accesibles para referencia futura.

- [ ] Estadísticas y análisis: La API puede proporcionar estadísticas sobre la productividad del usuario, como el número de tareas completadas en un período determinado o la distribución de tareas por etiquetas.
