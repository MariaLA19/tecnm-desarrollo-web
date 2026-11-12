# Bitácora de la Sesión 02 — Gestión en GitHub Web y Métodos HTTP (GET, POST, PUT, DELETE)

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 12/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu CRUD de libros responderá exactamente así

> Obtuve 8/8 casos correctos. ¡Resultado logrado!

```text
✅ 01. La colección inicia vacía
✅ 02. POST crea el libro con id 1
✅ 03. GET lista el libro creado
✅ 04. GET por id encuentra el libro
✅ 05. PUT reemplaza el libro
✅ 06. DELETE elimina el libro
✅ 07. El libro eliminado ya no existe
✅ 08. PATCH no está implementado: 405, no 404

## 2. Criterios de aceptación

- [X] La colección inicia vacía → HTTP 200
- [X] POST crea el libro con id 1 → HTTP 201
- [X] GET lista el libro creado → HTTP 200
- [X] GET por id encuentra el libro → HTTP 200
- [X] PUT reemplaza el libro → HTTP 200
- [X] DELETE elimina el libro → HTTP 204
- [X] El libro eliminado ya no existe → HTTP 404
- [X] PATCH no está implementado: 405, no 404 → HTTP 405

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python con FastAPI, en Google Colab, para un CRUD de libros |
| **Rol** | Asistente que me ayuda paso a paso a escribir y verificar el código  |
| **Especificación** | Rutas GET, POST, PUT, DELETE para libros, con códigos HTTP 200, 201, 204, 404 y 405 |
| **Output** | Código que pase 8/8 casos de verificación  |

### Prompt que utilicé

```text
Ayúdame paso a paso a crear un CRUD de libros con Python y FastAPI, con GET, POST, PUT y DELETE, y que al final verifique que pase 8/8 casos.
```

## 4. Decisiones de diseño

- ¿Qué estructura elegiste y por qué?
- Elegí una lista que inicia vacía para guardar los libros en orden, y que el id se asigne automáticamente con el siguiente número.
  
- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
- En el borde validé que si el libro no existe regrese 404 y que si el método no está implementado regrese 405. La lógica de crear, buscar, reemplazar y eliminar la dejé en las funciones.
  
- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
- Agregaría mensajes más claros cuando hay un error y una documentación para que el otro equipo sepa cómo usar cada ruta.

> 

## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
- Al principio me confundí con PATCH, porque yo pensé que debía dar 404 como si no existiera el libro.
  
- ¿Qué aprendiste al corregirlo?
- Aprendí que 404 es cuando no existe el libro, y 405 es cuando el método no está implementado. Son dos cosas diferentes.
  
- ¿Qué harías distinto la próxima vez?
- Aprendí que 404 es cuando no existe el libro, y 405 es cuando el método no está implementado. Son dos cosas diferentes.

> 

## 6. Evidencia

- **Commit:** se agrega después de guardar
- **Cuaderno ejecutado:** enlace al cuaderno en tu fork
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion02.html

---
**Firma digital:** MariaLA19
