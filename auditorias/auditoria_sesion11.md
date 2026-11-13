# Bitácora de la Sesión 11 — Arquitectura en capas: Router, Servicio y Repositorio
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

## 1. Resultado al que llegué
Resultado esperado: Mi API ya separa en capas y el listado no se pierde entre peticiones.

Salida de la verificación:
✅ 01. Listado inicial vacío
✅ 02. Creación válida
✅ 03. Consulta del libro creado
✅ 04. Listado persiste entre peticiones
✅ 05. Router no guarda estado
✅ 06. Servicio usa el repositorio
✅ 07. Repositorio es instancia única
✅ 08. Separación de capas correcta

RESULTADO: 8/8 casos correctos. ¡Sesión 11 lista!

## 2. Criterios de aceptación
- Listado inicial vacío → HTTP 200
- Creación válida → HTTP 201
- Consulta del libro creado → HTTP 200
- Listado persiste entre peticiones → HTTP 200
- Router no guarda estado → Verificación de capas
- Servicio usa el repositorio → Verificación de capas
- Repositorio es instancia única → Verificación de capas
- Separación de capas correcta → Verificación de capas

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| Contexto | Python / FastAPI con Pydantic v2 en Google Colab. |
| Rol | API con arquitectura en capas: Router, Servicio y Repositorio separados. |
| Especificación | POST /api/libros da 201. GET /api/libros da 200 con {"libros": []} al inicio. GET /api/libros/1 da 200. GET /api/libros después de crear sigue mostrando el libro creado. Router no tiene lista ni diccionario. Servicio llama al repositorio. Repositorio guarda en una sola lista en memoria. |
| Output | JSON del libro para éxito, sobre {"error": {"codigo", "mensaje"}} para errores. |

**Prompt que utilicé**
Ayúdame a separar mi API de libros en 3 capas en FastAPI: Router que solo recibe peticiones, Servicio que tiene la lógica y Repositorio que guarda en una lista en memoria con instancia única, para que el listado no se borre entre peticiones.

## 4. Decisiones de diseño
¿Qué estructura elegiste y por qué?
Elegí separar en 3 clases: Router, Servicio y RepositorioLibros. Cada una hace solo su trabajo, así el código queda más ordenado y más fácil de probar.

Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic titulo, anio y precio. A la lógica del Servicio le dejé buscar, crear y validar que el libro exista. Al Repositorio le dejé solo guardar en la lista y dar los ids.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría la lista en memoria del Repositorio por una base de datos real, para que los libros no se borren al reiniciar la API, sin tener que tocar el Router ni el Servicio.

## 5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?
El 04. Listado persiste entre peticiones. Al principio me salía vacío cada vez que pedía los libros.

¿Qué error detectó la verificación que tú no habías previsto?
La verificación me mostró que cada petición creaba un repositorio nuevo, por eso se perdían los libros. Yo no había pensado que tenía que usar una sola instancia para todo.

¿Qué aprendiste al corregirlo?
Aprendí que el Repositorio debe ser una sola instancia única que se comparte con el Servicio. Lo corregí creando una sola vez `repositorio = RepositorioLibros()` y pasándosela al Servicio. Con eso salió 8/8.

¿Qué harías distinto la próxima vez?
Desde el inicio pensar dónde se guarda el estado y crear la instancia una sola vez fuera de las funciones, para que no se pierda entre peticiones.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion11.md
**Cuaderno ejecutado:** Verificado en Google Colab con 8/8 en verde
**Tag:** v0.1-hito1
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion11.html

**Firma digital:** MariaLA19
