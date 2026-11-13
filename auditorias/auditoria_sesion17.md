# Bitácora de la Sesión 17 — Control de Acceso Basado en Roles (RBAC)

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python / FastAPI
**Fecha:** 13/11/2026

## 1. Resultado al que llegué

**Resultado esperado:** Tus respuestas de autorización se verán así

Salida de la celda de verificación - todos los casos en verde:

Implementé autenticación con roles en FastAPI. El token JWT ya incluye el rol del usuario en sus claims y el panel administrativo solo se abre para rol `admin`.

## 2. Criterios de aceptación

- [x] El administrador obtiene su token → HTTP 200
- [x] El usuario normal obtiene su token → HTTP 200
- [x] El admin entra al panel → HTTP 200
- [x] El usuario normal recibe 403 → HTTP 403
- [x] Sin token recibe 401 → HTTP 401
- [x] El perfil funciona para el usuario normal → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3 en Google Colab, FastAPI, JWT con `python-jose`, verificación con `verificar.py` del repositorio del curso. |
| **Rol** | Asistente técnico para implementar autenticación y autorización con RBAC, sin cambiar el contrato del verificador. |
| **Especificación** | `POST /api/token` recibe `{"usuario", "password"}` y devuelve `{"access_token"}`. `GET /api/admin/panel` requiere rol `admin`, si no hay token devuelve 401, si el rol es `user` devuelve 403, si es `admin` devuelve 200 `{"panel":"admin"}`. `GET /api/perfil` requiere cualquier usuario autenticado y devuelve `{"usuario", "rol"}`. Usuarios de prueba: `admin/admin123` rol `admin` y `ana/secreta` rol `user`. |
| **Output** | Código `app.py` completo y funcional + explicación de la diferencia entre 401 y 403. |

**Prompt que utilicé:**
> "Implementa en FastAPI el contrato de la Sesión 17 RBAC: POST /api/token con usuarios admin/admin123 rol admin y ana/secreta rol user, el token JWT debe incluir el rol en sus claims. GET /api/admin/panel solo para admin, GET /api/perfil para cualquier autenticado. Sin token debe dar 401, no 403, y con rol user en el panel debe dar 403. Dame el app.py completo listo para Colab."

## 4. Decisiones de diseño

¿Qué estructura elegiste y por qué?
Elegí un solo archivo `app.py` con diccionario de usuarios en memoria. No usé base de datos porque el contrato solo pedía 2 usuarios de prueba. Guardé el rol dentro de los claims del JWT en el campo `rol`, junto con `sub` para el usuario, así no tengo que consultar nada en cada petición.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé que venga el token, que sea válido y que no esté expirado. En la lógica de negocio validé el permiso: la función `solo_admin` revisa si `rol == "admin"` y si no, lanza 403.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría el diccionario por una base de datos real con contraseñas hasheadas con bcrypt, la `SECRET_KEY` la pasaría a variables de entorno, y agregaría refresh token y expiración más corta.

## 5. Errores, hallazgos y correcciones

¿Qué caso de la verificación falló primero?
El caso "Sin token recibe 401". Al principio me devolvía 403.

¿Qué aprendiste al corregirlo?
Aprendí que `HTTPBearer` por defecto devuelve 403 cuando no hay token. Para controlar yo el código tuve que poner `HTTPBearer(auto_error=False)` y lanzar yo misma el 401 cuando `creds is None`. Ahí entendí la diferencia: 401 = no estás autenticado, 403 = sí estás autenticado pero tu rol no alcanza.

Qué harías distinto la próxima vez?
Desde el inicio pensar primero en autenticar (¿quién eres?) y después en autorizar (¿tu rol alcanza?), y probar a mano el caso sin token antes de correr la verificación completa.


## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion17.md
**Cuaderno ejecutado:** Verificado en Google Colab con 6/6 casos en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion17.html

**Firma digital:** MariaLA19
