# Bitácora de la Sesión 08 — Respuestas Semánticas y Excepciones HTTP Personalizadas
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: El cliente necesita saber qué corregir, y nunca debe ver un 500 con el código interno.

Salida de la verificación:
✅ 01. Un libro existente responde 200
✅ 02. Un libro inexistente responde 404 con sobre de error
✅ 03. Los datos inválidos responden 422 con sobre de error
✅ 04. Un libro válido sigue respondiendo 201

RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- Un libro existente responde 200 → HTTP 200
- Un libro inexistente responde 404 con sobre de error → HTTP 404
- Los datos inválidos responden 422 con sobre de error → HTTP 422
- Un libro válido sigue respondiendo 201 → HTTP 201

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | Traductor de errores: convierte fallos en mensajes claros con el mismo sobre. |
| Especificación | GET /api/libros/1 devuelve 200. GET /api/libros/99 lanza LibroNoEncontrado y devuelve 404 con {"error": {"codigo": "NO_ENCONTRADO", "mensaje": "El libro 99 no existe"}}. POST con titulo vacío da 422 con {"error": {"codigo": "VALIDACION", "mensaje": "Revisa los datos enviados"}}. POST válido da 201. La API inicia con el libro 1 Rayuela. Ningún caso da 500. |
| Output | Siempre el mismo sobre {"error": {"codigo": ..., "mensaje": ...}} para errores, y JSON del libro para éxito. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI una excepción LibroNoEncontrado con un handler que devuelva 404 con {"error": {"codigo": "NO_ENCONTRADO"}}, y un handler de RequestValidationError que devuelva 422 con {"error": {"codigo": "VALIDACION"}}, con titulo min_length=1, y la API iniciando con el libro 1 Rayuela.

## 4. Decisiones de diseño
**Formato de error elegido**

| Caso | Código HTTP | Cuerpo |
| --- | --- | --- |
| Libro no existe | 404 | {"error": {"codigo": "NO_ENCONTRADO", "mensaje": "El libro 99 no existe"}} |
| Datos inválidos | 422 | {"error": {"codigo": "VALIDACION", "mensaje": "Revisa los datos enviados"}} |

¿Qué estructura elegiste y por qué?**
Elegí centralizar el formato en dos handlers con @app.exception_handler, así todos los errores salen con el mismo sobre y no repito el formato en cada endpoint.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé con Pydantic que el titulo no venga vacío. A la lógica le dejé solo buscar el libro y lanzar LibroNoEncontrado si no existe.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría más códigos como DUPLICADO o SIN_PERMISO, pero siempre con el mismo sobre {"error": {"codigo", "mensaje"}}.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Ninguno, salió 4/4 a la primera.

¿Qué aprendiste al corregirlo?**
Aprendí que si no pongo el handler de RequestValidationError, FastAPI devuelve el 422 con {"detail": ...} y no con mi sobre. Por eso hay que atrapar ese error y convertirlo. Y que nunca hay que dejar que salga un 500 con el Traceback.

¿Qué harías distinto la próxima vez?**
Desde el inicio poner el handler global de errores, para que todos mis endpoints ya salgan con el mismo formato.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion08.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion08.html

**Firma digital:** MariaLA19
