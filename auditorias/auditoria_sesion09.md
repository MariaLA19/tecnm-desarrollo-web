# Bitácora de la Sesión 09 — Middleware Web, Intercepción y Logging de Transacciones
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: Medir cuánto tarda cada petición sin repetir código en cada endpoint.

Salida de la verificación:
✅ 01. Una respuesta correcta trae tiempo y traza
✅ 02. El X-Request-ID del cliente se conserva
✅ 03. El middleware también cubre los 404

RESULTADO: 3/3 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- Una respuesta correcta trae tiempo y traza → HTTP 200
- El X-Request-ID del cliente se conserva → HTTP 200
- El middleware también cubre los 404 → HTTP 404

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI en Google Colab. |
| Rol | Portero que envuelve a todos los endpoints: mide antes y después, y agrega los encabezados. |
| Especificación | Toda respuesta incluye X-Process-Time con un número decimal de segundos y X-Request-ID. Si la petición trae X-Request-ID, la respuesta conserva ese valor. Si no trae, el servidor genera uno con uuid. El middleware también se aplica a 404. GET /api/libros sigue respondiendo 200 con {"libros": []}. |
| Output | Headers X-Process-Time y X-Request-ID en todas las respuestas. |

**Prompt que utilicé**
Ayúdame a crear en FastAPI un middleware con @app.middleware("http") que mida el tiempo con time.time(), tome el X-Request-ID del cliente o genere uno con uuid si no viene, y agregue X-Process-Time y X-Request-ID a todas las respuestas incluyendo los 404.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?**
Elegí un solo middleware con @app.middleware("http") que envuelve a call_next, así no tengo que repetir el código de medir tiempo en cada endpoint.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde, en el middleware, dejé solo la medición y la traza. A la lógica le dejé solo devolver {"libros": []}.

¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Agregaría un log con el request_id, el método, la ruta y el tiempo, para poder rastrear cada petición cuando algo falle.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?**
Ninguno, salió 3/3 a la primera.

¿Qué aprendiste al corregirlo?**
Aprendí que el middleware se ejecuta antes y después del endpoint: mido antes, llamo a call_next, y agrego los headers después. Por eso también cubre los 404, porque está afuera de los endpoints, no adentro.

¿Qué harías distinto la próxima vez?**
Siempre respetar el X-Request-ID que manda el cliente, porque si yo genero otro diferente, se pierde la traza.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion09.md
**Cuaderno ejecutado:** Verificado en Google Colab con 3/3 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion09.html

**Firma digital:** MariaLA19
