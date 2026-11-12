# Auditoría Sesión 03 · Headers, Content-Type y Negociación de Contenido
**Estudiante:** Martha Maria Lopez Alejandro
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201) · TecNM Cancún

## Contrato C-R-E-O
- **Contexto:** Python / FastAPI en Google Colab.
- **Rol:** API que negocia el formato de entrada y salida.
- **Especificación:** POST /api/libros solo acepta application/json, si no 415. GET /api/libros solo responde si acepta application/json, si pide XML 406. POST válido responde 201 con el libro creado.
- **Output:** Respuestas en application/json.

## ¿Qué resultado te costó más alcanzar y por qué?
El que más me costó fue entender que el POST no debía intentar adivinar el formato. Al principio pensé que si mandaban texto plano la API lo convertiría, pero aprendí que se debe revisar el header Content-Type y rechazar con 415 si no es JSON.

## ¿Qué decisión de diseño tomaste que no estaba escrita en el contrato?
Decidí revisar los headers con request.headers antes de leer el cuerpo, y guardar los libros en una lista en memoria con un contador para el id. Así el id va aumentando 1, 2, 3...

## ¿Qué error detectó la verificación que tú no habías previsto?
Al principio me salió No module named 'verificar' porque Colab había perdido el archivo. No era error de mi código. Lo arreglé volviendo a ejecutar la celda de Preparación del entorno y luego volví a correr app.py y la verificación, y ya salió 4/4 en verde.

## Resultado
Verificación: 4/4 casos correctos. ¡Resultado logrado!
