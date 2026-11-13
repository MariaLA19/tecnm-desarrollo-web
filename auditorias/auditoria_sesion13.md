# Bitácora de la Sesión 13 — Manejo de Sesiones Stateful vs Stateless Tokens

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 13/11/2026

## 1. Resultado al que llegué

**Resultado esperado:** Mi login crea una sesión en el servidor y la devuelve en una cookie HttpOnly.

**Salida de la verificación:**
✅ 01. Login correcto y cookie HttpOnly
✅ 02. El perfil se obtiene con la cookie
✅ 03. El logout cierra la sesión
✅ 04. Después del logout el perfil es 401

**RESULTADO: 4/4 casos correctos. ¡Sesión 13 lista!**

## 2. Criterios de aceptación

- Login correcto y cookie HttpOnly → HTTP 200
- El perfil se obtiene con la cookie → HTTP 200
- El logout cierra la sesión → HTTP 204
- Después del logout el perfil es 401 → HTTP 401

## 3. Mi contrato C-R-E-O

- **Contexto:** FastAPI en Colab, sesiones en memoria.
- **Rol:** Backend que guarda la sesión en el servidor, no en el cliente.
- **Especificación:** POST /api/login, GET /api/perfil, POST /api/logout. Usuario de prueba ana / secreta.
- **Output:** Login 200 + cookie, Perfil 200, Logout 204, después del logout Perfil 401.

## 4. Diferencia entre sesión y token

- **Sesión Stateful:** El servidor guarda todo (usuario, permisos) en memoria y el cliente solo guarda un `session_id` opaco en una cookie. Para cerrar sesión, el servidor solo borra ese id de su diccionario.
- **Token Stateless (JWT):** El servidor no guarda nada. Toda la info va dentro del token que el cliente guarda y manda en cada petición. No se puede "borrar" del servidor, solo esperar a que expire.

## 5. Cierre

¿Qué resultado te costó más alcanzar y por qué?
Entender que la cookie viaja sola y no tenía que copiar el session_id a mano en cada petición.

¿Qué decisión de diseño tomaste que no estaba escrita en el contrato?
Guardar las sesiones en un diccionario `sesiones = {}` en memoria, donde la llave es el session_id y el valor es el usuario. Y usar `secrets.token_urlsafe(32)` para que el id no se pueda adivinar.

¿Qué error detectó la verificación que tú no habías previsto?
Ninguno, quedó en verde a la primera. Pero aprendí que si la cookie no tiene HttpOnly y SameSite=Lax, el verificador la marca como incorrecta aunque el login funcione.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion13.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion13.html

**Firma digital:** MariaLA19
