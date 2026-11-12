# Bitácora de la Sesión 03 — Headers, Content-Type y Negociación de Contenido
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: Tu API negociará el formato exactamente así

Salida de la verificación:
✅ 01. POST válido en JSON
✅ 02. POST en texto plano se rechaza con 415
✅ 03. GET que pide XML se rechaza con 406
✅ 04. GET que acepta JSON responde 200

RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- POST válido en JSON → HTTP 201
- POST en texto plano se rechaza con 415 → HTTP 415
- GET que pide XML se rechaza con 406 → HTTP 406
- GET que acepta JSON responde 200 → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI en Google Colab. |
| Rol | API que negocia el formato de entrada y salida. |
| Especificación | POST /api/libros solo acepta application/json, si no 415. GET /api/libros solo responde si acepta application/json, si pide XML 406. POST válido responde 201 con el libro creado. |
| Output | Respuestas en application/json. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI un POST /api/libros que solo acepte application/json y rechace con 415 si es texto plano, y un GET /api/libros que rechace con 406 si pide XML y responda 200 si acepta JSON.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?**
Elegí guardar los libros en una lista en memoria con un contador para el id. Así el id va aumentando 1, 2, 3... y es fácil de probar en Colab.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé los headers con `request.headers` antes de leer el cuerpo, el Content-Type y el Accept. A la lógica de negocio le dejé solo crear el libro y guardarlo.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Les daría un mensaje de error más claro en JSON y documentaría qué headers debe mandar.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Al principio me salió `No module named 'verificar'` porque Colab había perdido el archivo. No era error de mi código.

¿Qué aprendiste al corregirlo?**
Aprendí que si se pierde el archivo hay que volver a ejecutar la celda de Preparación del entorno y luego volver a correr app.py y la verificación.

¿Qué harías distinto la próxima vez?**
Ejecutar las celdas en orden desde arriba, sin saltarme la de Preparación.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion03.md 
**Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion03.md
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion03.html

**Firma digital:** MariaLA19

