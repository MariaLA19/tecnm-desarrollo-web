# Bitácora de la Sesión 10 — Hito 1: Mock API RESTful con OpenAPI y Validation Harness
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: Mi API ya se comporta como un servicio profesional.

Salida de la verificación:
✅ 01. Listado inicial vacío
✅ 02. Creación válida
✅ 03. Consulta del libro creado
✅ 04. Actualización del libro
✅ 05. Eliminación del libro
✅ 06. El libro eliminado ya no existe
✅ 07. Validación de datos inválidos
✅ 08. Método no permitido
✅ 09. Contrato OpenAPI disponible

RESULTADO: 9/9 casos correctos. ¡Hito 1 listo!

## 2. Criterios de aceptación
- Listado inicial vacío → HTTP 200
- Creación válida → HTTP 201
- Consulta del libro creado → HTTP 200
- Actualización del libro → HTTP 200
- Eliminación del libro → HTTP 204
- El libro eliminado ya no existe → HTTP 404
- Validación de datos inválidos → HTTP 422
- Método no permitido → HTTP 405
- Contrato OpenAPI disponible → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | API profesional completa: CRUD, validación, documentación y errores semánticos. |
| Especificación | POST /api/libros da 201. GET /api/libros da 200 con {"libros": []} al inicio. GET /api/libros/1 da 200. PUT /api/libros/1 da 200. DELETE /api/libros/1 da 204 sin cuerpo. Después GET /api/libros/1 da 404. POST inválido da 422. PATCH da 405. GET /openapi.json da 200 con el esquema Libro. |
| Output | JSON del libro para éxito, sobre {"error": {"codigo", "mensaje"}} para errores, y 204 sin cuerpo para DELETE. |

**Prompt que utilicé**
Ayúdame a integrar en FastAPI una Mock API completa de libros: CRUD con ids asignados por el servidor, validación con Pydantic, middleware de tiempo y traza, handlers de 404 y 422, y modelo Libro para OpenAPI, sin definir PATCH para que dé 405.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?
Elegí juntar todo lo del Bloque 1 en un solo app.py: modelos Libro, LibroCreate y LibroUpdate, lista en memoria libros_db, middleware de la Sesión 09 y handlers de errores de la Sesión 08, para que toda la API tenga el mismo formato.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic titulo 3-80 caracteres, anio 1450-2100 y precio mayor a 0. A la lógica le dejé solo buscar, crear, actualizar y eliminar en la lista, y lanzar LibroNoEncontrado si no existe.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría la lista en memoria por una base de datos real, para que los libros no se borren al reiniciar la API, y agregaría autenticación.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?
El 04. Actualización del libro. Primero salió 8/9.

¿Qué error detectó la verificación que tú no habías previsto?
La verificación en el PUT solo mandaba el titulo, no todo el libro. Mi LibroUpdate exigía titulo, anio y precio obligatorios, por eso me daba 422 con respuesta.titulo: falta.

¿Qué aprendiste al corregirlo?
Aprendí que el PUT puede venir parcial. Lo corregí poniendo todos los campos de LibroUpdate como opcionales con | None y default=None, y en actualizar_libro solo cambio el campo si viene con datos, si no lo dejo como estaba. Con eso salió 9/9.

¿Qué harías distinto la próxima vez?
Desde el inicio pensar si la actualización es total o parcial, y poner los campos opcionales si el cliente puede mandar solo un dato.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion10.md
**Cuaderno ejecutado:** Verificado en Google Colab con 9/9 en verde
**Tag:** v0.1-hito1
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion10.html

**Firma digital:** MariaLA19
