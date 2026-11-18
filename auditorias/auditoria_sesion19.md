# Bitácora de la Sesión 19 — Sanitización de Entradas, Prevención de XSS e Inyecciones

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python / FastAPI
**Fecha:** 18/11/2026

## 1. Resultado al que llegué

**Resultado esperado:** Tu API neutralizará el HTML peligroso

VERIFICACIÓN DEL RESULTADO · 3 casos · app.py
✅ 01. Un comentario normal se guarda
✅ 02. El script se neutraliza
✅ 03. El listado tampoco devuelve scriptsRESULTADO: 3/3 casos correctos. ¡Resultado logrado!


## 2. Criterios de aceptación

- [x] Un comentario normal se guarda → HTTP 201
- [x] El script se neutraliza → HTTP 201
- [x] El listado tampoco devuelve scripts → HTTP 200

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3 en Google Colab, FastAPI, verificación con `verificar.py` del repositorio del curso. |
| **Rol** | Asistente técnico para implementar sanitización de entradas y prevención de XSS, sin cambiar el contrato del verificador. |
| **Especificación** | `POST /api/comentarios` recibe `{"texto": str}` y responde 201 con `{"id": int, "texto": str}` ya escapado. `GET /api/comentarios` responde 200 con `{"comentarios": [...]}` sin etiquetas ejecutables. Un comentario normal no se altera. La respuesta nunca contiene la cadena `<script>`. |
| **Output** | Código `app.py` completo y funcional + explicación de por qué la validación no sustituye al escape. |

**Prompt que utilicé:**
> "Implementa en FastAPI el contrato de la Sesión 19: POST /api/comentarios que reciba texto y lo devuelva escapado con html.escape, y GET /api/comentarios que liste los comentarios sin que aparezca <script> en la respuesta. El comentario normal no debe alterarse. Dame el app.py completo listo para Colab."

## 4. Decisiones de diseño

**¿Qué estructura elegiste y por qué?**
Elegí un solo archivo `app.py` con una lista en memoria `comentarios = []` y un contador para el `id`. No usé base de datos porque el contrato solo pedía guardar y listar comentarios para verificar que el escape funciona. Decidí escapar al guardar y no solo al mostrar, para que ningún endpoint pueda devolver el script por error.

**¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé con Pydantic que `texto` llegue como `str` y que exista. En la lógica de negocio dejé el escape: con `html.escape(data.texto)` convierto `<`, `>`, `&` y `"` en entidades seguras antes de guardar. No rechacé el input, lo neutralicé.

**¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Guardaría el texto original en base de datos y escaparía solo al mostrar (escape de salida), para no perder información. Cambiaría la lista en memoria por SQLite, y agregaría paginación en el GET.


## 5. Errores, hallazgos y correcciones

**¿Qué caso de la verificación falló primero?**
El caso "El listado tampoco devuelve scripts".

**¿Qué aprendiste al corregirlo?**
Aprendí que si solo escapaba en la respuesta del POST pero guardaba el texto original, el GET volvía a exponer `<script>`. Ahí entendí que la validación de entrada no sustituye al escape de salida: validar solo dice si el dato es válido, pero escapar es lo que evita que el navegador lo ejecute.

**¿Qué harías distinto la próxima vez?**
Desde el inicio pensar en los dos lugares: dónde se guarda y dónde se muestra. Y probar a mano con otros payloads como `<img src=x onerror=alert(1)>`, no solo con `<script>`.

## 6. Evidencia

**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion19.md
**Cuaderno ejecutado:** https://colab.research.google.com/github/ijmarquezl/tecnm-desarrollo-web/blob/main/laboratorios/sesion19/sesion19_laboratorio.
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion19.html

**Firma digital:** MariaLA19

