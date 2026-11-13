# Bitácora de la Sesión 12 — Inyección de Dependencias (FastAPI Depends / Contenedor IoC)
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: Mi endpoint ya no crea el repositorio, lo recibe inyectado con Depends.

Salida de la verificación:
✅ 01. El diagnóstico revela el repositorio inyectado
✅ 02. El endpoint inyectado crea un libro
✅ 03. El repositorio conserva el estado
✅ 04. La validación sigue en el borde
✅ 05. El endpoint usa Depends
✅ 06. Existe la función de inyección

RESULTADO: 6/6 casos correctos. ¡Sesión 12 lista!

## 2. Criterios de aceptación
- El diagnóstico revela el repositorio inyectado → HTTP 200
- El endpoint inyectado crea un libro → HTTP 201
- El repositorio conserva el estado → HTTP 200
- La validación sigue en el borde → HTTP 422
- El endpoint usa Depends → Verificación de archivo
- Existe la función de inyección → Verificación de archivo

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | API con inyección de dependencias: el endpoint recibe el repositorio, no lo crea. |
| Especificación | GET /api/diagnostico da 200 con {"repositorio": "RepositorioMemoria"}. POST /api/libros da 201 con el libro creado. GET /api/libros da 200 con el libro guardado. POST con anio inválido da 422. Existe get_repositorio() y los endpoints usan Depends(get_repositorio). |
| Output | JSON del libro para éxito, sobre {"error": {"codigo", "mensaje"}} para errores. |

**Prompt que utilicé**
Ayúdame a implementar en FastAPI un RepositorioMemoria y a inyectarlo en los endpoints con Depends(get_repositorio), para que el endpoint no cree el repositorio dentro de la función y el diagnóstico muestre qué implementación se está usando.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?
Elegí crear una clase RepositorioMemoria con lista y contador, una instancia única, y una función get_repositorio() que la devuelve. Así todos los endpoints comparten el mismo estado.

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic titulo y anio. A la lógica del Repositorio le dejé solo crear y listar. Al endpoint le dejé solo recibir el repositorio inyectado y llamar al método.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría la función get_repositorio() para que devolviera un repositorio con base de datos real, sin tener que tocar ningún endpoint, porque ya todos dependen de la inyección.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?
Ninguno en la segunda corrida, pero al principio pensé que tenía que poner RepositorioMemoria() dentro del endpoint.

¿Qué error detectó la verificación que tú no habías previsto?
La verificación me recordó que si hago RepositorioMemoria() dentro del endpoint no estoy inyectando, estoy acoplando. La dependencia debe llegar como parámetro con Depends.

¿Qué aprendiste al corregirlo?
Aprendí que con Depends el endpoint no sabe qué implementación usa, solo la recibe. Así puedo cambiar de repositorio en un solo lugar, en get_repositorio(), sin reescribir los endpoints. Con eso salió 6/6.

¿Qué harías distinto la próxima vez?
Desde el inicio pensar en qué dependencia necesita el endpoint y pasarla como parámetro con Depends, en vez de crearla adentro.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion12.md
**Cuaderno ejecutado:** Verificado en Google Colab con 6/6 en verde
**Tag:** v0.1-hito1
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion12.html

**Firma digital:** MariaLA19
