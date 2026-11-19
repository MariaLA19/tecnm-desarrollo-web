# Bitácora de la Sesión 21 — Fundamentos de Persistencia: SQLite / PostgreSQL y Drivers
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python / FastAPI
**Fecha:** 19/11/2026

## 1. Resultado al que llegué
**Resultado esperado:** Tus libros sobrevivirán al reinicio

VERIFICACIÓN DEL RESULTADO · 3 casos · app.py
✅ 01. La base inicia sin libros
✅ 02. El libro se inserta en SQLite
✅ 03. El listado lee la base
RESULTADO: 3/3 casos correctos. ¡Resultado logrado!✅ La fila existe en el archivo SQLite
RESULTADO: 1/1 comprobaciones correctas. ¡Resultado logrado!


## 2. Criterios de aceptación
- [x] La base inicia sin libros → HTTP 200
- [x] El libro se inserta en SQLite → HTTP 201
- [x] El listado lee la base → HTTP 200
- [x] La fila existe en el archivo SQLite

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| --- | --- |
| **Contexto** | Python en Google Colab, FastAPI, SQLite3 incluido en Python, sin instalar nada en mi computadora |
| **Rol** | Asistente técnico para implementar persistencia real en SQLite, no en listas de Python |
| **Especificación** | GET /api/libros → 200 y devuelve {"libros": []} o con libros. POST /api/libros recibe {"titulo": "Rayuela", "anio": 1963} → 201 y devuelve {"id": 1, "titulo": "Rayuela", "anio": 1963}. Tabla libros creada con CREATE TABLE IF NOT EXISTS. Usar consultas parametrizadas con ? y commit() después de insertar |
| **Producción** | Archivo app.py con la API completa y archivo biblioteca.db con la fila guardada |

**Prompt que utilicé:**
> "Implementa en FastAPI un CRUD mínimo que guarde libros en SQLite real. Que cree la tabla libros si no existe, POST /api/libros inserte y devuelva 201 con el id, GET /api/libros lea de la base y devuelva 200, y que los datos queden en biblioteca.db"

## 4. Decisiones de diseño
**¿Qué estructura elegiste y por qué?**
Elegí una sola tabla `libros` con `id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, anio INTEGER NOT NULL`. Es lo más simple y cumple el contrato. El id autoincremental sirve para identificar cada libro sin que yo lo tenga que generar.

```sql
CREATE TABLE IF NOT EXISTS libros (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo TEXT NOT NULL,
  anio INTEGER NOT NULL
);


