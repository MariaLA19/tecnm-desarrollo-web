# Bitacora de la Sesión 14 · Hashing Seguro de Contraseñas (Bcrypt)
**Materia:** Desarrollo de Aplicaciones Web (DAB-2201)
**Docente Titular:** MCC. Iván Márquez Larios (ijmarquezl)
**Estudiante:** Martha Maria Lopez Alejandro
**Matrícula:** 23531104
**Track:** Python/FastAPI
**Fecha:** 13/11/2026

## 1. Resultado
Implementé registro y login con hashing seguro usando `bcrypt` directo.
- `POST /api/registro` → 201, devuelve solo `{"usuario": "ana"}`
- `POST /api/login` con contraseña correcta → 200, `{"usuario": "ana", "autenticado": true}`
- `POST /api/login` con contraseña incorrecta → 401
- Verificación: 3/3 casos + 1/1 comprobación de archivo en verde.

## 2. ¿Qué resultado me costó más alcanzar y por qué?
El registro me costó más. Al principio usé `passlib` con `CryptContext` como dice la pista del cuaderno, pero me daba `HTTP 500` en el registro. Como no se guardaba nada, el login después me daba 401 aunque la contraseña era correcta.

## 3. ¿Qué decisión de diseño tomé que no estaba escrita en el contrato?
Decidí usar `bcrypt` directo (`bcrypt.hashpw` + `bcrypt.gensalt` + `bcrypt.checkpw`) en lugar de `passlib`, y guardar el hash como bytes en un diccionario en memoria `usuarios = {}`.
También decidí que un usuario repetido no sobrescriba la contraseña: si ya existe, devuelvo 409. Y nunca devuelvo `password` ni `hash` en ninguna respuesta.

## 4. ¿Qué error detectó la verificación que yo no había previsto?
La verificación me mostró que el error no estaba en mi lógica de login, sino en el registro: `passlib` ya no es compatible con la versión nueva de `bcrypt` y por eso fallaba con 500. Al cambiar a `bcrypt` directo, todo pasó en verde.
Aprendí que no se compara con `==`, se usa `checkpw`, porque bcrypt ya trae el salt dentro del hash.

## 5. ¿Por qué no se puede «deshashear»?
Porque el hash es de un solo sentido: bcrypt aplica el algoritmo con salt y costo, y el resultado no guarda la contraseña original, solo una huella. No existe una función inversa. Lo único que se puede hacer es tomar la contraseña que escribe el usuario, hashearla de nuevo con el mismo salt que está guardado en el hash, y comparar si da el mismo resultado con `checkpw`. Por eso si se filtra la base de datos, el atacante solo ve hashes, no contraseñas, y por eso nunca se debe guardar la contraseña tal cual ni devolver el hash al cliente.

## 6. Evidencia
**Commit:** https://github.com/MariaLA19/tecnm-desarrollo-web/blob/main/auditorias/auditoria_sesion14.md
**Cuaderno ejecutado:** Verificado en Google Colab con 3/3 + 1/1 en verde
**Presentación:** https://ijmarquezl.github.io/tecnm-desarrollo-web/presentaciones/sesion14.html

**Firma digital:** MariaLA19
