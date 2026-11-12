# Bitácora de la Sesión 04 — Anatomía RESTful, URIs Nombres y Recursos
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: La URL debe describir un recurso, no una acción.

Salida de la verificación:
✅ 01. Libros del autor 1
✅ 02. Filtro por género y límite
✅ 03. Un autor inexistente produce 404
✅ 04. La colección completa de libros

RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- Libros del autor 1 → HTTP 200
- Filtro por género y límite → HTTP 200
- Un autor inexistente produce 404 → HTTP 404
- La colección completa de libros → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI en Google Colab. |
| Rol | API RESTful que expone recursos con URIs jerárquicas basadas en sustantivos. |
| Especificación | GET /api/autores/{autor_id}/libros responde 200 con los libros del autor. Parámetros opcionales genero filtra por género y limite recorta la lista. GET /api/autores/99/libros responde 404 si el autor no existe. GET /api/libros responde 200 con todos los libros. Sin verbos en las rutas. |
| Output | Respuestas en application/json. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI GET /api/autores/{autor_id}/libros con filtro por genero y limite en la query, que responda 404 si el autor no existe, y GET /api/libros con todos los libros, sin usar verbos en las rutas.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?**
Elegí un diccionario `autores` donde la llave es el autor_id y el valor es su lista de libros. Así es fácil buscar al autor y devolver sus libros.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé que el autor exista, si no existe lanzo 404 con "Autor no encontrado". A la lógica le dejé solo filtrar por genero y recortar con limite.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría también GET /api/autores para listar a los autores, para que no tengan que adivinar los ids.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Ninguno, esta vez salió 4/4 a la primera.

¿Qué aprendiste al corregirlo?**
Aprendí la diferencia: el parámetro de ruta identifica (autor_id), el parámetro de consulta filtra (genero, limite). Si la ruta responde "lo mismo pero más pequeño", es un filtro y va después del ?.

¿Qué harías distinto la próxima vez?**
Seguir pensando primero si algo es identificación o filtro antes de ponerlo en la ruta.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion04.md
**Cuaderno ejecutado:** Verificado en Google Colab con 4/4 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion04.html

**Firma digital:** MariaLA19
