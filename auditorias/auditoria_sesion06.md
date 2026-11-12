# Bitácora de la Sesión 06 — Validación Estricta, Constraints y Params Query/Body
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: El servidor debe poner los límites de negocio, no el cliente. Si un dato está fuera de rango, debe dar 422.

Salida de la verificación:
✅ 01. Un libro dentro de los límites se crea
✅ 02. Un título demasiado corto produce 422
✅ 03. Un año fuera de rango produce 422
✅ 04. Un precio no positivo produce 422
✅ 05. El límite de paginación debe ser al menos 1
✅ 06. Un límite válido responde 200

RESULTADO: 6/6 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- Un libro dentro de los límites se crea → HTTP 201
- Un título demasiado corto produce 422 → HTTP 422
- Un año fuera de rango produce 422 → HTTP 422
- Un precio no positivo produce 422 → HTTP 422
- El límite de paginación debe ser al menos 1 → HTTP 422
- Un límite válido responde 200 → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | Validador de reglas de negocio en el servidor. No confía en lo que manda el cliente. |
| Especificación | POST /api/libros con titulo 3-80 caracteres, anio 1450-2100, precio > 0. GET /api/libros?limite= entre 1 y 100. Si algo no cumple, 422. Si cumple, 201 o 200. |
| Output | JSON con id, titulo, anio, precio. Listado paginado con {"libros": [...]}. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI con Pydantic v2 un LibroCreate con titulo Field(min_length=3, max_length=80), anio Field(ge=1450, le=2100), precio Field(gt=0) y un GET /api/libros con Query limite ge=1 le=100, que devuelva 422 si algo está fuera de rango y 201 si es válido.

## 4. Decisiones de diseño
**Tabla de restricciones**

| Campo | Restricción | Código |
| --- | --- | --- |
| titulo | min_length=3, max_length=80 | Field |
| anio | ge=1450, le=2100 | Field |
| precio | gt=0 | Field |
| limite | ge=1, le=100, default 10 | Query |

¿Qué estructura elegiste y por qué?**
Elegí poner todas las reglas en el DTO con Field y en el Query, así no repito la validación en cada endpoint.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé longitudes, rangos y que el precio sea positivo. A la lógica le dejé solo asignar id y cortar la lista con limite.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría también max_length y mensajes de error más claros para el cliente.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Ninguno, esta vez salió 6/6 a la primera porque ya venía del aprendizaje de la sesión 05.

¿Qué aprendiste al corregirlo?**
Aprendí la diferencia entre ge y gt: ge=1450 sí permite 1450, pero gt=0 NO permite 0. Por eso el precio 0 da 422.

¿Qué harías distinto la próxima vez?**
Revisar siempre si el límite incluye o no incluye el valor, porque ahí está el truco del 422.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion06.md
**Cuaderno ejecutado:** Verificado en Google Colab con 6/6 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion06.html

**Firma digital:** MariaLA19
