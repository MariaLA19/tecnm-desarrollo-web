# Bitácora de la Sesión 20 — Hito 2: API con Inyección de Dependencias, Auth JWT y RBAC

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 18/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** La seguridad de tu API resiste una auditoría

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

    VERIFICACIÓN DEL RESULTADO · 7 casos · app.py
    ✅ 01. Registro sin filtrar contraseñas
    ✅ 02. Login del usuario registrado
    ✅ 03. El usuario accede a su perfil
    ✅ 04. El usuario no entra al panel admin
    ✅ 05. El administrador obtiene su token
    ✅ 06. El administrador entra al panel
    ✅ 07. Sin token no hay acceso
    RESULTADO: 7/7 casos correctos. ¡Resultado logrado!
    

## 2. Criterios de aceptación

- [x] Registro sin filtrar contraseñas → HTTP 201
- [x] Login del usuario registrado → HTTP 200
- [x] El usuario accede a su perfil → HTTP 200
- [x] El usuario no entra al panel admin → HTTP 403
- [x] El administrador obtiene su token → HTTP 200
- [x] El administrador entra al panel → HTTP 200
- [x] Sin token no hay acceso → HTTP 401


## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3 en Google Colab, FastAPI, JWT con python-jose, verificación con verificar.py del repositorio del curso. |
| **Rol** | Asistente técnico para integrar registro, JWT y RBAC en un solo flujo, sin cambiar el contrato del verificador. |
| **Especificación** | POST /api/registro recibe {"usuario", "password"} y responde 201 sin devolver password ni hash. POST /api/token recibe {"usuario", "password"} y responde 200 con {"access_token", "token_type"}. GET /api/perfil requiere Bearer y responde 200 con {"usuario", "rol"}. GET /api/admin/panel solo para rol admin: sin token 401, con rol user 403, con rol admin 200. Admin precargado: admin/admin123 rol admin. Usuario de prueba: ana/secreta rol user. |
| **Output** | Código app.py completo y funcional + explicación de la diferencia entre 401 y 403 y por qué nunca se filtra la contraseña. |


### Prompt que utilicé

    Implementa en FastAPI el Hito 2: POST /api/registro con contraseña hasheada que no devuelva password ni hash, POST /api/token que emita JWT con rol, GET /api/perfil para cualquier autenticado y GET /api/admin/panel solo para admin. Sin token debe dar 401, no 403, y con rol user en el panel debe dar 403. Admin precargado admin/admin123. Dame el app.py completo listo para Colab.


## 4. Decisiones de diseño
- ¿Qué estructura elegiste y por qué?
Elegí un solo archivo app.py con diccionario de usuarios en memoria y dependencias de FastAPI. Usé Depends para no repetir la validación del token en cada ruta: get_usuario_actual autentica y solo_admin autoriza. Guardé la contraseña solo como hash con hashlib.sha256, así nunca queda en texto plano.

- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic que vengan usuario y password, y con la dependencia que venga el header Authorization: Bearer. En la lógica de negocio validé que el usuario exista, que la contraseña coincida con el hash y que el rol alcance para entrar al panel.

- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría el diccionario por una base de datos real con bcrypt y salt por usuario, la SECRET_KEY la pasaría a variables de entorno, agregaría refresh token y expiración más corta, y documentaría el flujo registro → login → perfil → panel.


## 5. Errores, hallazgos y correcciones
- ¿Qué caso de la verificación falló primero?
En las sesiones anteriores el caso "Sin token recibe 401" me fallaba porque me daba 403. En esta ya lo tenía previsto.

- ¿Qué aprendiste al corregirlo?
Aprendí que HTTPBearer por defecto devuelve 403 cuando no hay token. Para controlar yo el código tuve que poner HTTPBearer(auto_error=False) y lanzar yo misma el 401 cuando creds is None. También aprendí que el registro no debe devolver nunca la palabra password ni hash, ni siquiera en el nombre de un campo, porque el verificador revisa no_contiene. Ahí entendí que la seguridad no es una capa al final: es una propiedad de todo el flujo, desde el registro hasta el panel.

- ¿Qué harías distinto la próxima vez?
Desde el inicio ordenar el flujo como lo vive el cliente: registro, login, token, perfil, panel. Y probar primero el caso sin token y el caso del usuario normal en el panel, no solo el caso feliz del admin.


## 6. Evidencia

- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion20.md
- **Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/laboratorios/sesion20/sesion20_laboratorio.ipynb
- **Tag:** v0.2-hito2
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion20.html

---
**Firma digital:** MariaLA19
