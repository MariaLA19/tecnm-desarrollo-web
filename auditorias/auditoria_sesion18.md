# Bitácora de la Sesión 18 — Rate Limiting, Throttling y Prevención de Abuso

**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python / FastAPI
**Fecha:** 17/11/2026

## 1. Resultado al que llegué

**Resultado esperado:** 

VERIFICACIÓN DEL RESULTADO · 4 casos · app.py

✅ 01. Primera petición permitida
✅ 02. Segunda petición permitida
✅ 03. Tercera petición permitida
✅ 04. La cuarta petición se limita

RESULTADO: 4/4 casos correctos. ¡Resultado logrado!

## 2. Criterios de aceptación

- [x] Primera petición permitida → HTTP 200
- [x] Segunda petición permitida → HTTP 200
- [x] Tercera petición permitida → HTTP 200
- [x] La cuarta petición se limita → HTTP 429

## 3. Mi contrato C-R-E-O

| Elemento | Definición |
| :--- | :--- |
| **Contexto** | Python 3 en Google Colab, FastAPI, verificación con `verificar.py` del repositorio del curso. Todo en memoria, sin base de datos. |
| **Rol** | Asistente técnico para implementar rate limiting por cliente, sin cambiar el contrato del verificador. |
| **Especificación** | `GET /api/recurso` permite 3 peticiones por cliente en una ventana de 60 segundos. La 1ra, 2da y 3ra devuelven 200 con `{"mensaje":"ok","peticion": n}`. La 4ta devuelve 429 con `{"error":"límite de peticiones alcanzado"}` + header `Retry-After`. El cliente se identifica por IP (X-Forwarded-For o `request.client.host`). El contador se reinicia al iniciar la aplicación. |
| **Output** | Código `app.py` completo y funcional + explicación de la diferencia entre limitar y bloquear. |

**Prompt que utilicé:**
> "Implementa en FastAPI el contrato de la Sesión 18 Rate Limiting: GET /api/recurso permite 3 peticiones por cliente en 60 segundos y la 4ta devuelve 429 con Retry-After y {"error":"límite de peticiones alcanzado"}. El contador por cliente, no global. Dame el app.py completo listo para Colab."

## 4. Decisiones de diseño

**¿Qué estructura elegiste y por qué?**
Elegí un solo archivo `app.py` con un diccionario en memoria `defaultdict(list)` con la forma `{ ip_cliente: [timestamp1, timestamp2, ...] }`. No usé base de datos porque el contrato pide que el contador se reinicie al iniciar la aplicación, y en memoria eso pasa de forma natural. Además es fácil de auditar.

**¿Qué validaste en el borde de la API y qué dejaste a la lógica de negocio?**
En el borde validé identificar al cliente, limpiar la ventana y contar las peticiones. En la lógica de negocio decidí entre permitir (200) o limitar (429) según si ya había 3 peticiones en los últimos 60 segundos.

**¿Qué cambiarías si mañana otro equipo consumiera tu API?**
Cambiaría la identificación por IP a identificación por token o API-Key, porque varias personas detrás del mismo WiFi comparten IP. También movería el contador a Redis con TTL de 60 segundos para que funcione con varias instancias, y agregaría los headers `X-RateLimit-Limit`, `X-RateLimit-Remaining` y `X-RateLimit-Reset`.

## 5. Errores, hallazgos y correcciones

**¿Qué caso de la verificación falló primero?**
El caso de la cuarta petición. Al principio pensé en usar un contador global.

**¿Qué aprendiste al corregirlo?**
Aprendí que un contador global castiga a todos por culpa de uno. Un contador por cliente protege a todos. También aprendí que el 429 sin `Retry-After` o sin el JSON exacto falla aunque el código sea correcto, porque la verificación compara headers y JSON, no solo el número.

También aprendí la diferencia entre limitar y bloquear: limitar es pausar temporalmente y decirle al cliente cuándo reintentar con `Retry-After`. Bloquear sería negarle el acceso por completo.

**¿Qué harías distinto la próxima vez?**
Desde el inicio pensar en el cliente por IP o token y probar a mano el caso 4 antes de correr la verificación completa. Y calcular el `Retry-After` con el timestamp más viejo, no poner un 60 fijo sin cálculo.

**Cálculo de la ventana:**
- Límite: 3 peticiones
- Ventana: 60 segundos
- Fórmula para limpiar: `validas = [t for t in historial if ahora - t < 60]`
- Condición de rechazo: `Si len(validas) >= 3 -> 429`
- Cálculo de espera: `Retry-After = 60 - (ahora - validas[0])`

## 6. Evidencia

**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/new/main/auditorias
**Cuaderno ejecutado:** https://colab.research.google.com/github/ijmarquezl/tecnm-desarrollo-web/blob/main/laboratorios/sesion18/sesion18_laboratorio.ipynb
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion18.html

**Firma digital:** MariaLA19
