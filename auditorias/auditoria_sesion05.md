# Bitácora de la Sesión 05 — Pydantic v2 / DTOs
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:**23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: El DTO debe aceptar lo válido, convertir lo convertible y rechazar con 422 lo inválido o extra.

Salida de la verificación:
✅ 01. Un libro válido se crea con 201
✅ 02. La cadena numérica se convierte a entero
✅ 03. Un año no numérico produce 422
✅ 04. Un campo extra produce 422
✅ 05. El listado devuelve los libros creados

RESULTADO: 5/5 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- Un libro válido se crea con 201 → HTTP 201
- La cadena numérica se convierte a entero → HTTP 201
- Un año no numérico produce 422 → HTTP 422
- Un campo extra produce 422 → HTTP 422
- El listado devuelve los libros creados → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | Portero que valida el JSON antes de guardar. DTO de entrada estricto y DTO de salida con id. |
| Especificación | POST /api/libros recibe titulo (str), anio (int), precio (float), disponible (bool). Con extra="forbid" rechaza campos desconocidos con 422. Pydantic convierte "1966" a 1966, pero "mil novecientos" falla con 422. GET /api/libros devuelve {"libros": [...]}. |
| Output | JSON con id y datos del libro, sin campos inventados. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI con Pydantic v2 un LibroCreate con titulo, anio, precio, disponible y extra="forbid", que convierta "1966" a 1966, rechace con 422 un año no numérico y un campo extra, y un LibroOut con id, con POST /api/libros 201 y GET /api/libros.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?**
Elegí dos modelos separados: LibroCreate para lo que entra y LibroOut para lo que sale con id. Así el cliente no manda el id, lo genera el servidor.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé con Pydantic el tipo y que no vengan campos extra. A la lógica le dejé solo asignar el id y guardar en la lista.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría validación de que anio no sea negativo y titulo no venga vacío, para que el contrato sea más claro.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Al inicio me salió "Demasiadas sesiones" en Colab, no era error del código. Cerré las sesiones viejas y volvió a funcionar.

¿Qué aprendiste al corregirlo?**
Aprendí que Pydantic hace coerción: "1966" sí lo convierte a 1966, pero "mil novecientos" no lo puede convertir y por eso da 422. Y que sin extra="forbid" el campo extra pasaría y no daría 422.

¿Qué harías distinto la próxima vez?**
Cerrar los cuadernos viejos antes de empezar uno nuevo y siempre poner extra="forbid" cuando el contrato es cerrado.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion05.md
**Cuaderno ejecutado:** Verificado en Google Colab con 5/5 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion05.html

**Firma digital:** MariaLA19
