# Bitácora de la Sesión 07 — Especificación OpenAPI (Swagger) y ReDoc
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: La documentación no se escribe aparte, se genera del mismo código que atiende las peticiones.

Salida de la verificación:
✅ 01. OpenAPI responde con metadatos
✅ 02. Swagger UI está disponible
✅ 03. ReDoc está disponible
✅ 04. El endpoint documentado responde

RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- OpenAPI responde con metadatos → HTTP 200
- Swagger UI está disponible → HTTP 200
- ReDoc está disponible → HTTP 200
- El endpoint documentado responde → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | API que se documenta sola a partir de su código. |
| Especificación | App llamada Biblioteca API, versión 1.0.0, descripción API de libros del curso DAB-2201. GET /openapi.json con paths /api/libros y components.schemas Libro. GET /docs y GET /redoc en 200. GET /api/libros devuelve {"libros": []}. |
| Output | JSON de OpenAPI 3.1.0, Swagger UI y ReDoc generados automáticamente. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI una app con title Biblioteca API, version 1.0.0, description API de libros del curso DAB-2201, con un modelo Libro con id, titulo, anio, precio, y GET /api/libros y POST /api/libros con summary Listar libros y Crear un libro.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?**
Elegí un solo modelo llamado Libro para que aparezca en components.schemas. Si le ponía otro nombre, el verificador no lo encontraba.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde dejé que FastAPI genere sola la documentación desde el título, la versión y el modelo. A la lógica le dejé solo devolver la lista.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría summary y description en cada endpoint para que la documentación sea más clara para el cliente.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Ninguno, salió 4/4 a la primera.

¿Qué aprendiste al corregirlo?**
Aprendí que no hay que escribir la documentación aparte: si pongo bien el title, version, description y el modelo Pydantic, FastAPI genera sola /openapi.json, /docs y /redoc. Si el contrato y el código se contradicen, el contrato miente.

¿Qué harías distinto la próxima vez?**
Revisar siempre que el nombre del modelo sea exactamente el que pide el contrato, porque ahí está el truco.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion07.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion07.html

**Firma digital:** MariaLA19
