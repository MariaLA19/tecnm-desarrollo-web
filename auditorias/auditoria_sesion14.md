# Bitácora de la Sesión 14 — Hashing Seguro de Contraseñas (Bcrypt / Argon2)

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 13/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu registro y login se verán así

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

    VERIFICACIÓN DEL RESULTADO · 3 casos · app.py
    ✅ 01. El registro responde sin filtrar la contraseña
    ✅ 02. El login correcto autentica
    ✅ 03. La contraseña incorrecta se rechaza
    RESULTADO: 3/3 casos correctos. ¡Resultado logrado!
    
    ✅ Se usa un algoritmo de hashing para contraseñas
    RESULTADO: 1/1 comprobaciones correctas. ¡Resultado logrado!

## 2. Criterios de aceptación

- [x] El registro responde sin filtrar la contraseña → HTTP 201
- [x] El login correcto autentica → HTTP 200
- [x] La contraseña incorrecta se rechaza → HTTP 401
- [x] Se usa un algoritmo de hashing para contraseñas

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python / FastAPI en Google Colab, con bcrypt. |
| **Rol** | API de registro y login que guarda solo el hash, nunca la contraseña. |
| **Especificación** | POST /api/registro recibe usuario y password, guarda solo el hash y responde 201 sin devolver password ni hash. POST /api/login compara con el hash y responde 200 si es correcta o 401 si no. Si el usuario ya existe no lo sobrescribe, responde 409. |
| **Output** | Respuestas en JSON, sin password ni hash. Ejemplo registro: {"usuario":"ana"}. Ejemplo login correcto: {"usuario":"ana","autenticado":true} |

### Prompt que utilicé
Ayúdame a crear en FastAPI un POST /api/registro que guarde solo el hash con bcrypt y responda 201 sin devolver password ni hash, y un POST /api/login que verifique la contraseña con checkpw y responda 200 si es correcta o 401 si es incorrecta.

## 4. Decisiones de diseño

- ¿Qué estructura elegiste y por qué?
Elegí guardar los usuarios en un diccionario en memoria `usuarios = {}` donde la llave es el usuario y el valor es el hash en bytes. Así es fácil buscar al usuario en el login y no se guarda la contraseña en ningún lado.

- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic que vengan usuario y password. A la lógica le dejé crear el hash con `bcrypt.hashpw` + `bcrypt.gensalt()`, verificar con `bcrypt.checkpw` y no devolver nunca password ni hash.

- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
Guardaría los usuarios en base de datos en vez de en memoria, para que no se borren al reiniciar, y agregaría mensajes de error más claros sin decir si el usuario existe o no.


## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
Ninguno falló, salió 3/3 en verde a la primera y 1/1 en la revisión del archivo. Lo que sí me costó entender al principio fue que no se puede comparar con `==`, hay que usar `checkpw`.

- ¿Qué aprendiste al corregirlo?
Aprendí que bcrypt mete el salt dentro del mismo hash, por eso cada vez que registro la misma contraseña sale un hash diferente, pero `checkpw` sí la puede verificar. Y que el hash es de un solo sentido, no se puede deshashear para recuperar la contraseña original.

- ¿Qué harías distinto la próxima vez?
Revisar desde el inicio que la respuesta no contenga la palabra `password` ni `hash`, porque si se filtra, aunque el login funcione, la verificación lo marca como mal.

## 6. Evidencia

- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion14.md
- **Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/laboratorios/sesion14/sesion14_laboratorio.ipynb
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion14.html

---
**Firma digital:** MariaLA19
