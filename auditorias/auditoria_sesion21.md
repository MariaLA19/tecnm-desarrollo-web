# Bitácora de la Sesión 21 — Fundamentos de Persistencia: SQLite / PostgreSQL y Drivers
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python / FastAPI
**Fecha:** 19/11/2026

## 1. Resultado
Implementé persistencia real con SQLite, no con una lista de Python.
- GET /api/libros con base vacía → 200, devuelve {"libros": []}
- POST /api/libros con {"titulo": "Rayuela", "anio": 1963} → 201, devuelve {"id": 1, "titulo": "Rayuela", "anio": 1963}
- GET /api/libros después de insertar → 200, devuelve {"libros": [{"id": 1, "titulo": "Rayuela"}]}
- Verificación: 3/3 casos + 1/1 comprobación de archivo en verde.

Esquema de la tabla:
CREATE TABLE IF NOT EXISTS libros (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT NOT NULL,
  anio INTEGER NOT NULL
);

## 2. ¿Qué resultado me costó más alcanzar y por qué?
El POST me costó más. Al principio pensé en guardar los libros en una lista de Python libros = [] porque era más fácil, pero así al reiniciar el proceso se perdía todo y no pasaba la verificación. Me costó entender que tenía que crear la conexión, ejecutar el INSERT y hacer commit() para que de verdad quedara guardado en el archivo biblioteca.db.

## 3. ¿Qué decisión de diseño tomé que no estaba escrita en el contrato?
Decidí llamar a init_db() en cada petición y no solo al iniciar la app, para que si el verificador borra la base, se vuelva a crear sola con CREATE TABLE IF NOT EXISTS.
También decidí usar consultas parametrizadas con ? en lugar de concatenar el texto, para evitar inyección SQL. Y usé Pydantic para validar que titulo sea texto y anio sea número antes de guardar.

## 4. ¿Qué error detectó la verificación que yo no había previsto?
La verificación me mostró que el error no estaba en mi ruta, sino en que no se estaba creando la tabla al iniciar. Si la base no existía, el GET fallaba porque no encontraba la tabla libros. Al poner init_db() al inicio y en cada petición, todo pasó en verde.
Aprendí que no basta con hacer execute(), hay que hacer commit() después de insertar, si no el dato no queda guardado en el archivo.

## 5. ¿Por qué los datos sobreviven al reinicio?
Porque la memoria se pierde al reiniciar, pero el archivo no. Cuando guardo en una lista de Python, esa lista vive solo en la RAM del proceso y al reiniciar se borra. Cuando guardo en SQLite, el INSERT + commit() escribe la fila en el archivo biblioteca.db que queda en el disco. Aunque se apague el servidor, el archivo sigue ahí, y al volver a iniciar la app, el SELECT vuelve a leer esa misma fila. Por eso el proceso puede reiniciarse y el libro Rayuela sigue existiendo.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion21.md
**Cuaderno ejecutado:** Verificado en Google Colab con 3/3 + 1/1 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion21.html
**Firma digital:** MariaLA19

