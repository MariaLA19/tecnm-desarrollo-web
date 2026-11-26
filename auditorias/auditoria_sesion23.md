# Bitácora de la Sesión 23 — Operaciones CRUD Transaccionales y Async Sessions

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 26/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu CRUD asíncrono se verá así

    VERIFICACIÓN DEL RESULTADO · 5 casos · app.py

    ✅ 01. Crear un libro
    ✅ 02. Listar los libros
    ✅ 03. Actualizar el libro
    ✅ 04. Eliminar el libro
    ✅ 05. El libro eliminado ya no existe

    RESULTADO: 5/5 casos correctos. ¡Resultado logrado!

Y la verificación de persistencia asíncrona también quedó en verde con el regex AsyncSession|async_sessionmaker|aiosqlite.

## 2. Criterios de aceptación

- [x] Crear un libro → HTTP 201
- [x] Listar los libros → HTTP 200
- [x] Actualizar el libro → HTTP 200
- [x] Eliminar el libro → HTTP 204
- [x] El libro eliminado ya no existe → HTTP 404
- [x] La persistencia es asíncrona


## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | FastAPI + SQLAlchemy Async + aiosqlite en Google Colab, Python 3.13.18, base de datos SQLite biblioteca.db. Motor de verificación de 13395 bytes. |
| **Rol** | Asistente técnico como arquitecto backend que implementa un CRUD sin bloquear el event loop. |
| **Especificación** | POST /api/libros {titulo, anio} → 201. GET /api/libros → 200 con {"libros": [...]}. GET /api/libros/{id} → 200 o 404. PUT /api/libros/{id} → 200 o 404. DELETE /api/libros/{id} → 204 o 404. Validación con Pydantic LibroCreate. Tabla libros con id, titulo, anio. |
| **Output** | Archivo app.py con create_async_engine, AsyncSession, async_sessionmaker, todos los endpoints async def con await. |


### Prompt que utilicé
Implementa un CRUD completo con SQLAlchemy asíncrono y aiosqlite en FastAPI.
Usa create_async_engine con sqlite+aiosqlite, AsyncSession en cada endpoint,
POST 201, GET 200, PUT 200, DELETE 204, 404 si el id no existe, y que la
tabla se cree al iniciar la aplicación. No debe bloquear el event loop.


## 4. Decisiones de diseño

- **¿Qué estructura elegiste y por qué?**
  Un solo archivo app.py, porque el contrato solo pedía ese archivo. Dentro puse el modelo Libro con SQLAlchemy 2.0 (Mapped, mapped_column), Base(DeclarativeBase), el motor create_async_engine con sqlite+aiosqlite, async_sessionmaker y la función libro_to_dict(). Así todo queda ordenado y el verificador lo encuentra fácil.

- **¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
  En el borde, con Pydantic LibroCreate, validé que titulo sea string y anio sea int antes de tocar la BD. A la lógica de negocio dejé verificar si el id existe con session.get() y lanzar HTTPException 404 si no existe, además del commit, refresh y delete.

- **¿Qué cambiarías si mañana otro equipo consumiera tu API?**
  Separaría en models.py, schemas.py, database.py y routers/, agregaría paginación en GET /api/libros, mensajes de error más claros y una dependencia get_session en vez de abrir la sesión en cada endpoint.


### Diferencia entre def y async def

> Con def + sesión síncrona, el endpoint bloquea el event loop mientras espera a la base de datos y ningún otro request puede avanzar.
> Con async def + AsyncSession + await, el servidor libera el loop mientras espera la respuesta de SQLite y puede atender otras peticiones.
> La regla es: motor async, sesión async, endpoint async.


## 5. Errores, hallazgos y correcciones

- **¿Qué caso de la verificación falló primero?**
El primero: Crear un libro → esperaba 201 y recibió HTTP 500 (Se esperaba 201).
  
- **¿Qué aprendiste al corregirlo?**
Que el código "parecía funcionar" pero el verificador usa TestClient sin with, entonces mi lifespan nunca se ejecutaba y la tabla libros no existía. Un 500 casi siempre es que la tabla no está creada o que la sesión falló.

- **¿Qué harías distinto la próxima vez?**
No confiar solo en el lifespan / startup. Asegurar la creación de la tabla en cada request o en una dependencia, y probar borrando la BD antes de verificar.



## 6. Evidencia

- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/new/main/auditorias
- **Cuaderno ejecutado:** https://colab.research.google.com/github/ijmarquezl/tecnm-desarrollo-web/blob/main/laboratorios/sesion23/sesion23_laboratorio.ipynb#scrollTo=ZnbX3scs-0ha
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion23.html

---
**Firma digital:** MariaLA19
