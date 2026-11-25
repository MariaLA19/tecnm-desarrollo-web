# Bitácora de la Sesión 16 — OAuth2 Password Flow y Header Authorization Bearer

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 13/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu flujo OAuth2 se verá así

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

    VERIFICACIÓN DEL RESULTADO · 4 casos · app.py
    ✅ 01. El login con formulario emite un token
    ✅ 02. El token válido abre el perfil
    ✅ 03. Sin token no hay acceso
    ✅ 04. Con esquema Basic es rechazado
    RESULTADO: 4/4 casos correctos. ¡Resultado logrado!
    
    ✅ Se usa OAuth2PasswordBearer y una librería JWT
    RESULTADO: 1/1 comprobaciones correctas. ¡Resultado logrado!

## 2. Criterios de aceptación

- [x] El login con formulario emite un token → HTTP 200
- [x] El token válido abre el perfil → HTTP 200
- [x] Sin token no hay acceso → HTTP 401 + WWW-Authenticate: Bearer
- [x] Con esquema Basic es rechazado → HTTP 401
- [x] Se usa OAuth2PasswordBearer y una librería JWT


## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python / FastAPI en Google Colab, sin guardar sesión en el servidor. |
| **Rol** | Asistente técnico para implementar OAuth2 Password Flow con JWT. |
| **Especificación** | POST /token recibe formulario username y password y responde 200 con access_token y token_type. GET /api/perfil exige Authorization: Bearer y valida la firma. Sin token → 401 + WWW-Authenticate: Bearer. Con esquema Basic → 401. Token alterado o vencido → 401. |
| **Output** | Código en app.py que pase la verificación 4/4 + 1/1 en verde. |


### Prompt que utilicé
Ayúdame a implementar en FastAPI el OAuth2 Password Flow con POST /token usando OAuth2PasswordRequestForm, que emita un JWT con python-jose, y una ruta GET /api/perfil protegida con OAuth2PasswordBearer que devuelva 401 con WWW-Authenticate: Bearer si falta el token o si el esquema no es Bearer.


## 4. Decisiones de diseño

- ¿Qué estructura elegiste y por qué?
Elegí un solo archivo app.py con POST /token para emitir y GET /api/perfil para validar. Usé OAuth2PasswordBearer(tokenUrl="/token") para que FastAPI se encargue solo del 401 con WWW-Authenticate: Bearer, y OAuth2PasswordRequestForm para que lea el formulario. Para el token seguí usando python-jose con algoritmo HS256, guardar el usuario en sub y también en usuario, y poner expiración de 30 minutos con exp.

- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé que el login venga como formulario y que el perfil venga con header Authorization: Bearer. En la lógica de negocio dejé solo la validación de credenciales: usuario ana y contraseña secreta. La clave secreta la leo de la variable de entorno JWT_SECRET_KEY con un valor de práctica solo para que funcione en Colab, no la dejo quemada en el código de producción.

- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
Les daría una ruta de refresh para renovar el token sin volver a pedir contraseña y documentaría con ejemplos que el login es con formulario y el perfil es con encabezado Bearer, para que ningún equipo lo confunda con JSON.


## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
El login. Al principio lo hice con JSON como en la sesión 15 y me daba 422. Entendí que OAuth2 no usa JSON para el login, usa formulario, y por eso tuve que cambiarlo a OAuth2PasswordRequestForm.

- ¿Qué aprendiste al corregirlo?
Aprendí que la verificación me mostró que sin token debía dar 401 con WWW-Authenticate: Bearer y no 422, por eso tuve que usar OAuth2PasswordBearer, que ya pone ese header solo. También aprendí que si mando Authorization: Basic ... en lugar de Bearer, también debe dar 401, porque el esquema no es el correcto.

- ¿Qué harías distinto la próxima vez?
Probaría primero el login con formulario y el caso sin token, no solo el caso feliz. Y recordaría siempre la diferencia entre el formulario y el encabezado: el formulario es solo para el login, POST /token con Content-Type: application/x-www-form-urlencoded y cuerpo username=ana&password=secreta, ahí van las credenciales una sola vez para pedir el token. El encabezado es GET /api/perfil con Authorization: Bearer ..., ahí ya no van las credenciales, va el token en cada petición. Por eso OAuth2 usa formulario y no JSON: porque es el contrato que esperan los clientes OAuth2. Y por eso nunca se debe mandar la contraseña en el encabezado, solo el token.

## 6. Evidencia

- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion16.md
- **Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/laboratorios/sesion16/sesion16_laboratorio.ipynb
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion16.html

---
**Firma digital:** MariaLA19
