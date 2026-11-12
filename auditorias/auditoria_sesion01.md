# Bitácora de la Sesión 01 — Encuadre, Diagnóstico HTTP y Servidores en la Nube

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)  
**Docente Titular:** MCC. Iván Márquez Larios (`ijmarquezl`)  
**Estudiante:** Martha Maria Lopez Alejandro  
**Matrícula:** 23531104  
**Track:** Python/FastAPI  
**Fecha:** 12/11/2026

---

## 1. Resultado al que llegué

**Resultado esperado:** Tu servidor responderá exactamente así

> Pega aquí la salida de la celda de verificación (los casos en verde) o describe exactamente qué obtuviste.

'''text
✅ 01 - El servidor está vivo y responde JSON → HTTP 200
✅ 02 - El eco devuelve el mensaje recibido → HTTP 200
✅ 03 - La ruta desconocida devuelve 404
✅ 04 - La ruta de salud responde correctamente
RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación
- [X] El servidor está vivo y responde JSON → HTTP 200
- [X] El eco devuelve el mensaje recibido → HTTP 200
- [X] La ruta desconocida devuelve 404
- [X] La ruta de salud responde correctamente


| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python con FastAPI en Google Colab |
| **Rol** | Asistente para crear el servidor |
| **Especificación** | /health, /echo, 200, 404 |
| **Output** | JSON con mensaje y verificación 4/4 |

### Prompt que utilicé

```text
Ayúdame a crear un servidor en Python con FastAPI que responda JSON en /health y /echo, con verificación 4/4
```

## 4. Decisiones de diseño

- ¿Qué estructura elegiste y por qué?
- Elegí FastAPI porque es fácil y responde en JSON.
  
- ¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?
- Validé que la ruta existiera, si no existe devuelve 404. Lo demás lo dejé a la lógica del servidor.
  
- ¿Qué cambiarías si mañana otro equipo consumiera tu API?
- Le pondría instrucciones claras de qué rutas usar, /health y /echo.

> 

## 5. Errores, hallazgos y correcciones

- ¿Qué caso de la verificación falló primero?
- Ninguno, todos pasaron 4/4 a la primera.
  
- ¿Qué aprendiste al corregirlo?
- Aprendí que si sigo el contrato paso a paso, sale en verde.
  
- ¿Qué harías distinto la próxima vez?
- Tener menos miedo de ejecutar las celdas.

> 

## 6. Evidencia

- **Commit:** [enlace al commit]
- **Cuaderno ejecutado:** [enlace al cuaderno en tu fork]
- **Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion01.html

---
**Firma digital:** MariaLA19

