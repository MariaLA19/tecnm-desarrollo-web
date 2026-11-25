# Bitácora de la Sesión 21 — Fundamentos de Persistencia: SQLite / PostgreSQL y Drivers

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 13/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tus libros sobrevivirán al reinicio

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

    VERIFICACIÓN DEL RESULTADO · 4 casos · app.py
    ✅ 01. La base inicia sin libros
    ✅ 02. El libro se inserta en SQLite
    ✅ 03. El listado lee la base
    ✅ 04. La fila existe en el archivo SQLite
    RESULTADO: 4/4 casos correctos. ¡Resultado logrado!
    

## 2. Criterios de aceptación

- [x] La base inicia sin libros → HTTP 200
- [x] El libro se inserta en SQLite → HTTP 201
- [x] El listado lee la base → HTTP 200
- [x] La fila existe en el archivo SQLite
- [ ] 

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3 en Google Colab, FastAPI, SQLite con el módulo sqlite3, sin ORM. |
| **Rol** | Asistente técnico para implementar persistencia con SQLite y drivers. |
| **Especificación** | GET /api/libros devuelve la lista de libros desde la base, 200. POST /api/libros recibe {"titulo", "autor"} y guarda la fila en SQLite, responde 201 con {"id", "titulo", "autor"}. Al iniciar, si no existe la tabla libros, se crea. La base queda guardada en el archivo libros.db. |
| **Output** | Código app.py completo y funcional + verificación 4/4 en verde. |


### Prompt que utilicé
Ayúdame a implementar en FastAPI con sqlite3 una API de libros con persistencia: GET /api/libros que lea de la base y POST /api/libros que inserte en SQLite y responda 201. La tabla se debe crear al iniciar si no existe y los datos deben quedar guardados en el archivo libros.db para que sobrevivan al reinicio.


## 4. Decisiones de diseño
- ¿Qué estructura elegiste y por qué?
Elegí un solo archivo app.py con SQLite y el módulo sqlite3, sin ORM, porque el contrato solo pedía guardar libros en un archivo. Creé una tabla libros con id, titulo y autor, y una función que crea la tabla al iniciar si no existe, así la base siempre empieza lista.

- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
En el borde validé con Pydantic que vengan titulo y autor y que no vengan vacíos. En la lógica de negocio dejé el INSERT con parámetros, el SELECT para el listado y el commit para guardar los cambios en el archivo.

- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
Cambiaría SQLite por PostgreSQL con un driver como psycopg y variables de entorno para la conexión, agregaría paginación al listado y validaría que no se repita el mismo libro.
  

## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
El caso "El listado lee la base". El POST me daba 201, pero el GET me devolvía la lista vacía.

- ¿Qué aprendiste al corregirlo?
Aprendí que en SQLite hay que hacer conn.commit() después del INSERT, si no el dato se queda solo en memoria y no se guarda en el archivo. También aprendí que hay que usar consultas con parámetros ? en lugar de concatenar el texto, para evitar inyección SQL. Y que la diferencia con las sesiones anteriores es que antes guardaba en un diccionario y al reiniciar se borraba todo, ahora al guardar en el archivo libros.db los libros sobreviven al reinicio.

- ¿Qué harías distinto la próxima vez?
Desde el inicio verificar que el archivo libros.db sí se creó y que la fila sí quedó guardada con un SELECT directo, antes de correr la verificación completa. Y siempre hacer commit después de cada INSERT.
  

## 6. Evidencia
- **Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion21.md
- **Cuaderno ejecutado:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/laboratorios/sesion21/sesion21_laboratorio.ipynb
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion21.html

---
**Firma digital:** MariaLA19
