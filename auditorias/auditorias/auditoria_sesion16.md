# Bitácora de la Sesión 16 — OAuth2 Password Flow y Header Authorization Bearer

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Pista:** Python/FastAPI
**Fecha:** 13/11/2026

## 1. Resultado al que llegué
Implementé el OAuth2 Password Flow con FastAPI.
- `POST /token` con formulario `username=ana&password=secreta` → 200, devuelve `{"access_token": "eyJ...", "token_type": "bearer"}`
- `GET /api/perfil` con token Bearer válido → 200, `{"usuario": "ana"}`
- `GET /api/perfil` sin token → 401 + `WWW-Authenticate: Bearer`
- `GET /api/perfil` con esquema `Basic` → 401
- Verificación: 4/4 casos + 1/1 comprobación de archivo en verde.

## 2. ¿Qué resultado me costó más alcanzar y por qué?
Me costó más el login. Al principio lo hice con JSON como en la sesión 15 y me daba 422. Entendí que OAuth2 no usa JSON para el login, usa formulario, y por eso tuve que cambiarlo a `OAuth2PasswordRequestForm`.

## 3. ¿Qué decisión de diseño tomé que no estaba escrita en el contrato?
Decidí usar `OAuth2PasswordBearer(tokenUrl="/token")` para que FastAPI se encargue solo del 401 con `WWW-Authenticate: Bearer`, y `OAuth2PasswordRequestForm` para que lea el formulario. Para el token seguí usando `python-jose` con algoritmo `HS256`, guardar el usuario en `sub` y también en `usuario`, y poner expiración de 30 minutos con `exp`.
La clave secreta la leo de la variable de entorno `JWT_SECRET_KEY` con un valor de práctica solo para que funcione en Colab, no la dejo quemada en el código de producción.

## 4. ¿Qué error detectó la verificación que yo no había previsto?
La verificación me mostró que sin token debía dar 401 con `WWW-Authenticate: Bearer` y no 422. Por eso tuve que usar `OAuth2PasswordBearer`, que ya pone ese header solo. También aprendí que si mando `Authorization: Basic ...` en lugar de `Bearer`, también debe dar 401, porque el esquema no es el correcto.

## 5. ¿Cuál es la diferencia entre el formulario y el encabezado?
Porque el formulario es solo para el login y el encabezado es para las rutas protegidas. 
El formulario es `POST /token` con `Content-Type: application/x-www-form-urlencoded` y cuerpo `username=ana&password=secreta`. Ahí van las credenciales una sola vez para pedir el token.
El encabezado es `GET /api/perfil` con `Authorization: Bearer ...`. Ahí ya no van las credenciales, va el token en cada petición. 
Por eso OAuth2 usa formulario y no JSON: porque es el contrato que esperan los clientes OAuth2, y así cualquier cliente sabe cómo pedir el token y cómo mandarlo después. Y por eso nunca se debe mandar la contraseña en el encabezado, solo el token.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion16.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 + 1/1 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion16.html
**Firma digital:** MariaLA19

## Ejemplo (sin datos reales)
**Formulario login:** `username=ana&password=secreta`
**Encabezado perfil:** `Authorization: Bearer eyJhbGciOiJIUzI1NiIs...`
**Respuesta sin token:** `401 Unauthorized` + `WWW-Authenticate: Bearer`
