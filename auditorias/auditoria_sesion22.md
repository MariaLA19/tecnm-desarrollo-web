# Bitácora de la Sesión 22 — Modelado Relacional (1:1, 1:N, N:M) con ORMs

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 13/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu relación autor → libros se verá así

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

    VERIFICACIÓN DEL RESULTADO · 4 casos · app.py
    ✅ 01. Se crea el autor
    ✅ 02. Se crea el libro asociado
    ✅ 03. El autor devuelve sus libros
    ✅ 04. El listado de libros funciona
    RESULTADO: 4/4 casos correctos. ¡Resultado logrado!
    ✅ La relación ORM está declarada
    RESULTADO: 1/1 comprobaciones correctas. ¡Resultado logrado!

## 2. Criterios de aceptación

- [x] Se crea el autor → HTTP 201
- [x] Se crea el libro asociado → HTTP 201
- [x] El autor devuelve sus libros → HTTP 200
- [x] El listado de libros funciona → HTTP 200
- [x] La relación ORM está declarada


## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3.13 en Google Colab, FastAPI, SQLAlchemy con SQLite en biblioteca.db, sin escribir JOIN a mano. |
| **Rol** | Asistente técnico para modelar relaciones 1:N con ORM y respetar la integridad referencial. |
| **Especificación** | POST /api/autores recibe {"nombre"} y responde 201 con {"id", "nombre"}. POST /api/autores/{id}/libros recibe {"titulo", "anio"} y responde 201 con {"id", "titulo", "anio", "autor_id"}. Si el autor no existe responde 404. GET /api/autores/{id} responde 200 con el autor y sus libros anidados. GET /api/libros responde 200 con {"libros": [...]}. |
| **Output** | Código app.py completo y funcional + verificación 4/4 + 1/1 en verde. |


### Prompt que utilicé
Ayúdame a modelar en FastAPI con SQLAlchemy una relación 1:N entre Autor y Libro: Autor con id y nombre, Libro con id, titulo, anio y autor_id como llave foránea, con relationship y back_populates. POST /api/autores y POST /api/autores/{id}/libros deben responder 201, GET /api/autores/{id} debe devolver el autor con sus libros anidados y GET /api/libros el listado.


## 4. Decisiones de diseño

- ¿Qué estructura elegiste y por qué?
Elegí un solo archivo app.py con dos modelos: Autor con tabla autores y Libro con tabla libros. Puse en Libro autor_id = Column(Integer, ForeignKey("autores.id")) y en Autor libros = relationship("Libro", back_populates="autor", cascade="all, delete-orphan"), y en Libro autor = relationship("Autor", back_populates="libros"). Así trabajo con objetos y el ORM escribe el JOIN por mí. Usé SQLite en biblioteca.db y Base.metadata.create_all(engine) para crear las tablas.

- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic que vengan nombre, titulo y anio. En la lógica de negocio dejé buscar al autor por id antes de crear el libro, y si no existe lanzar 404, para respetar la integridad referencial y no crear libros huérfanos. También dejé armar la respuesta con los libros anidados desde autor.libros.

- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
Agregaría la relación N:M con una tabla intermedia, por ejemplo libros y categorías, y una relación 1:1, por ejemplo autor y biografía. También usaría PostgreSQL en lugar de SQLite y separaría los modelos en un archivo models.py para que el código no quede todo en app.py.


## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
 El caso "El autor devuelve sus libros". Al principio me devolvía el autor sin libros, o me fallaba porque la tabla no existía cuando la verificación limpiaba biblioteca.db.

- ¿Qué aprendiste al corregirlo?
Aprendí que en SQLAlchemy ForeignKey("autores.id") y relationship con back_populates describen la relación, pero si no uso autor.libros no sale anidado, tengo que armarlo yo en la respuesta con [{"id": l.id, "titulo": l.titulo} for l in autor.libros]. También aprendí que hay que llamar a Base.metadata.create_all(bind=engine) en cada ruta, porque la verificación borra biblioteca.db y si no recreo las tablas, las consultas fallan. Y que el ORM mantiene la relación: yo trabajo con objetos, él escribe el JOIN.

- ¿Qué harías distinto la próxima vez?
Desde el inicio probar el GET del autor con sus libros anidados, no solo el POST, y probar con la base borrada para confirmar que las tablas se recrean solas. También revisar que el libro siempre quede ligado a un autor que sí exista, antes de correr la verificación completa.


## 6. Evidencia

- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion22.md
- **Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/laboratorios/sesion22/sesion22_laboratorio.ipynb
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion22.html

---
**Firma digital:** MariaLA19
