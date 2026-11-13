# Bitácora de la Sesión 15 — Autenticación Stateless con JSON Web Tokens (JWT)

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Pista:** Python/FastAPI
**Fecha:** 13/11/2026


## 1. Resultado al que llegué
Implementé autenticación stateless con JWT.
- `POST /api/token` con `{"usuario": "ana", "password": "secreta"}` → 200, devuelve `{"access_token": "eyJ...", "token_type": "bearer"}`
- `GET /api/perfil` con token válido → 200, `{"usuario": "ana"}`
- `GET /api/perfil` con token alterado → 401
- `GET /api/perfil` sin token → 401

- Verificación: 4/4 casos + 1/1 comprobación de archivo en verde.


## 2. Criterios de aceptación
- [x] El login emite un token → HTTP 200
- [x] El token válido abre el perfil → HTTP 200
- [x] Un token alterado es rechazado → HTTP 401
- [x] Sin token no hay acceso → HTTP 401
- [x] Se usa una librería JWT

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI en Google Colab, sin guardar sesión en el servidor. |
| Rol | Asistente técnico para implementar autenticación con JWT firmado. |
| Especificación | `POST /api/token` valida usuario y contraseña y responde 200 con `access_token` y `token_type`. `GET /api/perfil` exige `Authorization: Bearer` y valida la firma. Token alterado o vencido → 401. Sin token → 401. |
| Producción | Código en `app.py` que pase la verificación 4/4 + 1/1 en verde. |

**Prompt que utilicé**
> Ayúdame a implementar en FastAPI un login que emita un JWT con python-jose, con expiración y una ruta /api/perfil protegida que valide la firma y devuelva 401 si el token está alterado o falta. La clave secreta debe venir de una variable de entorno.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?
Elegí una sola archivo `app.py` con dos rutas: `POST /api/token` para emitir y `GET /api/perfil` para validar. Usé `python-jose` con algoritmo `HS256` porque es lo que pide el contrato y es simple de verificar. Guardé el usuario en `sub` y también en `usuario`, y puse expiración de 30 minutos con `exp`.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé que exista el header `Authorization` y que empiece con `Bearer `, y que el token no esté alterado. En la lógica de negocio dejé solo la validación de credenciales: usuario `ana` y contraseña `secreta`.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Les daría una ruta de refresh para renovar el token sin volver a pedir contraseña, usaría `exp` más corto y guardaría la clave secreta solo en variables de entorno del servidor, nunca en el código. También documentaría la API con ejemplos de cómo mandar el `Bearer`.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?
El perfil con token alterado. Al principio me daba 500 en lugar de 401.

¿Qué aprendiste al corregirlo?
Aprendí que cuando `jwt.decode` falla porque la firma no coincide, lanza `JWTError` y yo debo atraparlo y responder 401, no dejar que se rompa el servidor. También aprendí que un token alterado no es un error del servidor, es un acceso no autorizado. Y que sin token también debo dar 401, no 422, por eso validé yo misma el header.

¿Qué harías distinto la próxima vez?
Desde el inicio atrapar los errores de JWT con `try/except` y probar primero el caso alterado y el caso sin token, no solo el caso feliz.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion15.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 + 1/1 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion15.html

**Firma digital:** MariaLA19
