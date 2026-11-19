Bitácora de la Sesión 22 — Modelado Relacional (1:1, 1:N, N:M) con ORMs
Materia: Desarrollo de Aplicaciones Web (DAB-2201)
Docente Titular: MCC. Iván Márquez Larios (ijmarquezl)
Estudiante: Martha María López Alejandro
Matrícula: 23531104
Track: Python / FastAPI
Fecha: 19/11/2026

1. Resultado al que llegué

VERIFICACIÓN DEL RESULTADO · 4 casos · app.py
✅ 01. Se crea el autor
✅ 02. Se crea el libro asociado
✅ 03. El autor devuelve sus libros
✅ 04. El listado de libros funciona
RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

✅ La relación ORM está declarada
RESULTADO: 1/1 comprobaciones correctas. ¡Resultado logrado!

2. Criterios de aceptación
[x] Se crea el autor → HTTP 201
[x] Se crea el libro asociado → HTTP 201
[x] El autor devuelve sus libros → HTTP 200
[x] El listado de libros funciona → HTTP 200
[x] La relación ORM está declarada

3. Mi contrato C-R-E-O
Elemento	Definición
Contexto	Python en Google Colab, FastAPI, SQLAlchemy, SQLite, sin instalar nada en mi computadora
Rol	Asistente técnico para modelar relaciones 1:N con ORM, sin escribir JOIN a mano
Especificación	POST /api/autores recibe {"nombre": "Gabriel García Márquez"} → 201 y devuelve {"id": 1, "nombre": "Gabriel García Márquez"}. POST /api/autores/1/libros recibe {"titulo": "Cien años de soledad", "anio": 1967} → 201 y devuelve {"id": 1, "titulo": "Cien años de soledad", "anio": 1967, "autor_id": 1}. GET /api/autores/1 → 200 y devuelve el autor con sus libros anidados. GET /api/libros → 200 y devuelve {"libros": [...]}. Modelo Autor con id y nombre. Modelo Libro con id, titulo, anio y autor_id como ForeignKey. Relación Autor.libros con relationship
Producción	Archivo app.py con los modelos ORM y la API completa, y base biblioteca.db con la relación guardada

Prompt que utilicé
"Implementa en FastAPI con SQLAlchemy una relación 1:N entre Autor y Libro. Autor tiene id y nombre, Libro tiene id, titulo, anio y autor_id como ForeignKey a autores.id. Usa relationship con back_populates. POST /api/autores crea autor y devuelve 201, POST /api/autores/{id}/libros crea libro asociado y devuelve 201, GET /api/autores/{id} devuelve autor con sus libros anidados y devuelve 200, GET /api/libros devuelve el listado y devuelve 200"

4. Decisiones de diseño
¿Qué estructura elegiste y por qué?
Elegí dos modelos: Autor con id y nombre, y Libro con id, titulo, anio y autor_id como llave foránea a autores.id. La relación es 1:N porque un autor puede tener muchos libros, pero un libro solo tiene un autor. Usé relationship("Libro", back_populates="autor") en Autor y relationship("Autor", back_populates="libros") en Libro, así el ORM mantiene la relación y yo trabajo con objetos.

Diagrama entidad-relación:
Autor (1) ----< Libro (N)
Autor: id PK, nombre
Libro: id PK, titulo, anio, autor_id FK -> autores.id

¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic que nombre y titulo sean texto y que anio sea número. En la lógica dejé la creación de las tablas con Base.metadata.create_all, la búsqueda del autor y el guardado de la relación con autor_id.

¿Qué cambiarías si mañana otro equipo consumiera tu API?
Agregaría la relación N:M con una tabla intermedia para libros con varios autores, la relación 1:1 para perfil del autor, validación de que el autor exista antes de crear el libro con 404, y las rutas de PUT y DELETE para completar el CRUD.

5. Errores, hallazgos y correcciones
¿Qué caso de la verificación falló primero?
El GET /api/autores/1 falló primero porque devolvía al autor sin sus libros anidados.

¿Qué aprendiste al corregirlo?
Aprendí que no hay que escribir el JOIN a mano. Basta con declarar ForeignKey('autores.id') y relationship('Libro', back_populates='autor'). Cuando pido autor.libros, SQLAlchemy hace el JOIN por mí. También aprendí que tengo que leer la relación antes de cerrar la sesión, si no me da error.

¿Qué harías distinto la próxima vez?
Probar primero el GET con libros anidados antes de dar por terminado el POST, y poner create_all en cada endpoint para que si el verificador borra la base, se vuelva a crear sola.

6. Evidencia
Commit: https://github.com/MariaLA19/tecnm-desarrollo-web/new/main/auditorias
Cuaderno ejecutado: https://github.com/MariaLA19/tecnm-desarrollo-web/new/main/auditorias
Presentación: https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion22.html
Firma digital: MariaLA19
