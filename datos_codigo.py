"""
Ejemplos de código para la diapositiva "Código en contexto".

Cada sesión tiene dos paneles:
  - lab: el código que se escribe en el laboratorio (dominio Biblioteca).
  - proyecto: el mismo concepto aplicado al Proyecto Integrador (dominio Tablero).

Los ejemplos son extractos ilustrativos, no aplicaciones completas. El objetivo
es que el estudiante vea la forma del código antes de escribirlo.
"""

from textwrap import dedent


def c(texto: str) -> str:
    return dedent(texto).strip()


CODIGO = {
    1: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Diagnóstico")

class Eco(BaseModel):
    mensaje: str

@app.get("/api/estado")
def estado():
    return {"servidor": "ok", "curso": "DAB-2201"}
"""),
            "mirada": [
                "`app = FastAPI()` es el servidor que atiende las peticiones.",
                "`@app.get` asocia una ruta y un verbo a una función.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
from fastapi import FastAPI

app = FastAPI(title="Proyecto Integrador DAB-2201")

@app.get("/health")
def health():
    return {"status": "ok"}
"""),
            "mirada": [
                "El proyecto empieza con un `main.py` y un endpoint de salud.",
                "La estructura crecerá en `routers/`, `services/` y `repositories/`.",
            ],
        },
        "nota": "Hoy solo compruebas que el servidor responde; el proyecto arranca formalmente en la sesión 4.",
    },
    2: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/libros", status_code=201)
def crear(libro: Libro):
    nuevo = {"id": len(libros) + 1, **libro.model_dump()}
    libros.append(nuevo)
    return nuevo

@app.get("/api/libros")
def listar():
    return {"libros": libros}

@app.delete("/api/libros/{id}", status_code=204)
def borrar(id: int):
    libros[:] = [l for l in libros if l["id"] != id]
"""),
            "mirada": [
                "El verbo HTTP define la acción: `POST` crea, `GET` lee, `DELETE` borra.",
                "`status_code=201` y `204` forman parte del contrato, no son decoración.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/tableros.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.post("/api/tableros", status_code=201)
def crear_tablero(datos: TableroCreate):
    return repositorio.crear(datos.nombre)

@router.get("/api/tableros")
def listar_tableros():
    return {"tableros": repositorio.listar()}
"""),
            "mirada": [
                "El proyecto usa `/api/tableros` en lugar de `/api/libros`.",
                "El verbo y el código HTTP no cambian: solo cambia el recurso.",
            ],
        },
        "nota": "Mismo contrato HTTP, distinto dominio. Así se traslada lo aprendido al proyecto.",
    },
    3: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.middleware("http")
async def negociar(request: Request, call_next):
    if request.url.path == "/api/libros" and request.method == "POST":
        tipo = request.headers.get("content-type", "").split(";")[0]
        if tipo != "application/json":
            return JSONResponse({"detail": "Usa JSON"}, status_code=415)
    return await call_next(request)
"""),
            "mirada": [
                "`content-type` se lee antes de procesar el cuerpo.",
                "`415` indica formato de entrada no soportado.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.middleware("http")
async def validar_formato(request: Request, call_next):
    if request.method in {"POST", "PUT"}:
        tipo = request.headers.get("content-type", "").split(";")[0]
        if tipo != "application/json":
            return JSONResponse({"error": "Content-Type inválido"}, status_code=415)
    return await call_next(request)
"""),
            "mirada": [
                "El middleware del proyecto cubre todos los `POST` y `PUT` de la API.",
                "El error usa el mismo sobre que el resto de la aplicación.",
            ],
        },
        "nota": "En el laboratorio lo aplicas a una ruta; en el proyecto, a toda la API.",
    },
    4: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.get("/api/autores/{autor_id}/libros")
def libros_autor(autor_id: int, genero: str | None = None):
    if autor_id not in autores:
        raise HTTPException(404, "Autor no encontrado")
    libros = [l for l in LIBROS if l["autor_id"] == autor_id]
    if genero:
        libros = [l for l in libros if l["genero"] == genero]
    return {"autor_id": autor_id, "libros": libros}
"""),
            "mirada": [
                "El parámetro de ruta identifica al padre; el de consulta filtra.",
                "Un padre inexistente responde `404`.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/tableros.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.get("/api/tableros/{tablero_id}/tareas")
def listar_tareas(tablero_id: int, estado: str | None = None):
    if not repositorio.existe(tablero_id):
        raise HTTPException(404, "Tablero no encontrado")
    tareas = repositorio.tareas(tablero_id)
    return {"tareas": [t for t in tareas if not estado or t.estado == estado]}
"""),
            "mirada": [
                "La relación se lee igual: padre en la ruta, filtro después del `?`.",
                "El proyecto valida que el tablero exista antes de listar sus tareas.",
            ],
        },
        "nota": "Cambia `autores/libros` por `tableros/tareas`; la jerarquía es la misma.",
    },
    5: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
class LibroEntrada(BaseModel):
    model_config = ConfigDict(extra="forbid")
    titulo: str
    anio: int
    precio: float
    disponible: bool

@app.post("/api/libros", status_code=201)
def crear(libro: LibroEntrada):
    return {"id": 1, **libro.model_dump()}
"""),
            "mirada": [
                "El DTO define qué datos entran y de qué tipo.",
                "`extra=\"forbid\"` convierte el contrato en algo cerrado.",
            ],
        },
        "proyecto": {
            "archivo": "src/schemas/tablero.py",
            "lenguaje": "python",
            "codigo": c(r"""
class TableroCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    nombre: str = Field(min_length=3, max_length=80)

class TableroOut(BaseModel):
    id: int
    nombre: str
"""),
            "mirada": [
                "El proyecto separa `Create` (entrada) de `Out` (salida).",
                "Así no filtra campos internos como `usuario_id` sin querer.",
            ],
        },
        "nota": "El DTO es el mismo patrón; en el proyecto separas entrada y salida.",
    },
    6: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
class Libro(BaseModel):
    titulo: str = Field(min_length=3, max_length=80)
    anio: int = Field(ge=1450, le=2100)
    precio: float = Field(gt=0)

@app.get("/api/libros")
def listar(limite: int = Query(default=10, ge=1, le=100)):
    return {"libros": libros[:limite]}
"""),
            "mirada": [
                "`Field` pone los límites en el contrato, no en cada función.",
                "`Query` valida el parámetro de paginación.",
            ],
        },
        "proyecto": {
            "archivo": "src/schemas/tarea.py",
            "lenguaje": "python",
            "codigo": c(r"""
class TareaCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=120)
    estado: Literal["pendiente", "en_progreso", "hecha"] = "pendiente"
    prioridad: Literal["baja", "media", "alta"] = "media"
"""),
            "mirada": [
                "`Literal` valida los estados y prioridades permitidos.",
                "El proyecto evita `if estado not in [...]` disperso por el código.",
            ],
        },
        "nota": "Las restricciones se declaran una vez y se aplican en todos los endpoints.",
    },
    7: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
app = FastAPI(
    title="Biblioteca API",
    version="1.0.0",
    description="API de libros del curso DAB-2201",
)

@app.get("/api/libros", tags=["libros"])
def listar() -> list[Libro]:
    return libros
"""),
            "mirada": [
                "`title`, `version` y `description` alimentan OpenAPI.",
                "Los `tags` agrupan las rutas en Swagger.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
app = FastAPI(
    title="Proyecto Integrador DAB-2201",
    version="0.1.0",
    description="API de tableros y tareas",
)
app.include_router(tableros.router, prefix="/api", tags=["tableros"])
"""),
            "mirada": [
                "El contrato del proyecto se publica en `/docs` desde el Hito 1.",
                "Cada router puede tener su propio tag y prefijo.",
            ],
        },
        "nota": "La documentación no se escribe aparte: se genera del mismo código.",
    },
    8: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
class LibroNoEncontrado(Exception):
    pass

@app.exception_handler(LibroNoEncontrado)
async def no_encontrado(request: Request, exc: LibroNoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"error": {"codigo": "NO_ENCONTRADO", "mensaje": str(exc)}},
    )
"""),
            "mirada": [
                "El handler centraliza el formato del error.",
                "El cliente recibe un sobre JSON, no una traza de Python.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.exception_handler(NoEncontrado)
async def manejar_no_encontrado(request: Request, exc: NoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"error": {"codigo": "NO_ENCONTRADO", "mensaje": str(exc)}},
    )
"""),
            "mirada": [
                "El proyecto usa el mismo sobre para 404 y 422.",
                "El frontend puede leer `error.codigo` sin adivinar.",
            ],
        },
        "nota": "Un formato de error uniforme es parte del contrato del proyecto.",
    },
    9: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.middleware("http")
async def trazabilidad(request: Request, call_next):
    inicio = time.perf_counter()
    respuesta = await call_next(request)
    respuesta.headers["X-Process-Time"] = f"{time.perf_counter() - inicio:.4f}"
    respuesta.headers["X-Request-ID"] = request.headers.get("X-Request-ID", "auto")
    return respuesta
"""),
            "mirada": [
                "El middleware mide antes y después de llamar al endpoint.",
                "Los encabezados se agregan a todas las respuestas.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/middleware.py",
            "lenguaje": "python",
            "codigo": c(r"""
class Trazabilidad(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        inicio = time.perf_counter()
        response = await call_next(request)
        response.headers["X-Process-Time"] = f"{time.perf_counter() - inicio:.4f}"
        return response
"""),
            "mirada": [
                "En el proyecto el middleware vive en `core/`.",
                "Se registra una vez en `main.py` y cubre toda la API.",
            ],
        },
        "nota": "La lógica es la misma; cambia el lugar donde se organiza.",
    },
    10: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/libros", status_code=201)
def crear(libro: Libro) -> Libro:
    return repo.crear(libro)

@app.get("/api/libros/{libro_id}")
def obtener(libro_id: int) -> Libro:
    libro = repo.buscar(libro_id)
    if libro is None:
        raise LibroNoEncontrado(f"Libro {libro_id}")
    return libro
"""),
            "mirada": [
                "El router delega en el repositorio; no guarda datos por su cuenta.",
                "El contrato incluye éxito y error.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/tableros.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.post("/api/tableros", status_code=201)
def crear_tablero(datos: TableroCreate) -> TableroOut:
    return servicio.crear(datos)

@router.get("/api/tableros/{tablero_id}", response_model=TableroOut)
def obtener_tablero(tablero_id: int):
    return servicio.obtener(tablero_id)
"""),
            "mirada": [
                "`response_model` documenta y filtra la salida.",
                "El Hito 1 del proyecto es este mismo CRUD.",
            ],
        },
        "nota": "El Hito 1 del proyecto es este CRUD con `Tablero` en lugar de `Libro`.",
    },
    11: {
        "lab": {
            "archivo": "router.py",
            "lenguaje": "python",
            "codigo": c(r"""
from servicio import ServicioLibros
router = APIRouter()
servicio = ServicioLibros()

@router.get("/api/libros")
def listar():
    return {"libros": servicio.listar()}

# app.py
app.include_router(router)
"""),
            "mirada": [
                "El router no conoce la base de datos ni los detalles de almacenamiento.",
                "`include_router` conecta la capa HTTP con el resto.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
from routers import tableros
app.include_router(tableros.router, prefix="/api")

# src/routers/tableros.py
@router.get("/api/tableros")
def listar(servicio=Depends(get_servicio)):
    return {"tableros": servicio.listar()}
"""),
            "mirada": [
                "El proyecto replica la separación en `routers/`, `services/` y `repositories/`.",
                "El router solo traduce HTTP; el servicio decide.",
            ],
        },
        "nota": "La arquitectura en capas del proyecto es la misma del laboratorio, con más archivos.",
    },
    12: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
def get_repositorio() -> RepositorioMemoria:
    return repositorio

@app.get("/api/libros")
def listar(repo: RepositorioMemoria = Depends(get_repositorio)):
    return {"libros": repo.listar()}

@app.get("/api/diagnostico")
def diagnostico(repo=Depends(get_repositorio)):
    return {"repositorio": type(repo).__name__}
"""),
            "mirada": [
                "El endpoint recibe la dependencia; no la construye dentro.",
                "Cambiar la implementación no obliga a tocar la ruta.",
            ],
        },
        "proyecto": {
            "archivo": "src/dependencies.py",
            "lenguaje": "python",
            "codigo": c(r"""
def get_repositorio() -> TableroRepository:
    return TableroRepository(sesion=SessionLocal())

# src/routers/tableros.py
@router.get("/api/tableros")
def listar(repo: TableroRepository = Depends(get_repositorio)):
    return {"tableros": repo.listar()}
"""),
            "mirada": [
                "En el Hito 3 el proyecto cambia el repositorio de memoria a base de datos.",
                "El router no se reescribe: solo cambia la dependencia.",
            ],
        },
        "nota": "La inyección de dependencias es lo que permite crecer sin romper los endpoints.",
    },
    13: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/login")
def login(datos: Login, response: Response):
    token = crear_sesion(datos.usuario)
    response.set_cookie("session_id", token, httponly=True, samesite="lax")
    return {"mensaje": "sesión iniciada"}

@app.get("/api/perfil")
def perfil(session_id: str | None = Cookie(default=None)):
    usuario = sesiones.get(session_id)
    if usuario is None:
        raise HTTPException(401, "no autenticado")
    return {"usuario": usuario}
"""),
            "mirada": [
                "El servidor guarda la sesión; el cliente solo lleva un identificador.",
                "`HttpOnly` y `SameSite` protegen la cookie.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/auth.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.post("/api/token")
def login(datos: LoginRequest):
    usuario = servicio.autenticar(datos.usuario, datos.password)
    token = crear_jwt(usuario)
    return {"access_token": token, "token_type": "bearer"}
"""),
            "mirada": [
                "El proyecto usa JWT: el servidor no guarda la sesión.",
                "La cookie del laboratorio te ayuda a entender qué se guarda y dónde.",
            ],
        },
        "nota": "Sesión con estado en el laboratorio; token sin estado en el proyecto. Ambos autentican.",
    },
    14: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
import bcrypt

hash_guardado = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
if bcrypt.checkpw(password.encode(), hash_guardado):
    return {"autenticado": True}
raise HTTPException(401, "credenciales inválidas")
"""),
            "mirada": [
                "La contraseña nunca se guarda en texto plano.",
                "`checkpw` compara contra el hash; no se puede \"deshashear\".",
            ],
        },
        "proyecto": {
            "archivo": "src/core/security.py",
            "lenguaje": "python",
            "codigo": c(r"""
def hashear(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verificar(password: str, hash_guardado: str) -> bool:
    return bcrypt.checkpw(password.encode(), hash_guardado.encode())
"""),
            "mirada": [
                "El proyecto centraliza el hash en `core/security.py`.",
                "Registro y login usan las mismas dos funciones.",
            ],
        },
        "nota": "El hash es una huella, no un cifrado reversible. El proyecto nunca devuelve la contraseña.",
    },
    15: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
payload = {"sub": usuario, "exp": datetime.now(timezone.utc) + timedelta(minutes=30)}
token = jwt.encode(payload, SECRET, algorithm="HS256")

@app.get("/api/perfil")
def perfil(authorization: str = Header(default="")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, "falta token")
    datos = jwt.decode(authorization[7:], SECRET, algorithms=["HS256"])
    return {"usuario": datos["sub"]}
"""),
            "mirada": [
                "El token se firma con una clave secreta y una expiración.",
                "La firma detecta cualquier alteración.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/security.py",
            "lenguaje": "python",
            "codigo": c(r"""
def crear_jwt(usuario: Usuario) -> str:
    payload = {"sub": str(usuario.id), "rol": usuario.rol, "exp": ...}
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")

def leer_jwt(token: str) -> dict:
    return jwt.decode(token, settings.secret_key, algorithms=["HS256"])
"""),
            "mirada": [
                "El proyecto incluye el rol para RBAC.",
                "La clave se lee desde `.env`, no se escribe en el código.",
            ],
        },
        "nota": "El token del proyecto es el mismo JWT, con el rol como claim adicional.",
    },
    16: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def token(form: OAuth2PasswordRequestForm = Depends()):
    usuario = autenticar(form.username, form.password)
    return {"access_token": crear_jwt(usuario), "token_type": "bearer"}

@app.get("/api/perfil")
def perfil(token: str = Depends(oauth2_scheme)):
    return {"usuario": leer_jwt(token)["sub"]}
"""),
            "mirada": [
                "OAuth2 usa formulario para el login y Bearer para las rutas.",
                "FastAPI agrega el reto `WWW-Authenticate` cuando falta el token.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/auth.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.post("/api/token")
def login(datos: LoginRequest):
    usuario = servicio.autenticar(datos.usuario, datos.password)
    return {"access_token": crear_jwt(usuario), "token_type": "bearer"}
"""),
            "mirada": [
                "El proyecto usa JSON por simplicidad.",
                "El encabezado `Authorization: Bearer` es idéntico al estándar.",
            ],
        },
        "nota": "El formato del login cambia; el Bearer y el 401 no.",
    },
    17: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
def require_admin(usuario=Depends(usuario_actual)):
    if usuario["rol"] != "admin":
        raise HTTPException(403, "permiso insuficiente")
    return usuario

@app.get("/api/admin/panel")
def panel(admin=Depends(require_admin)):
    return {"panel": "admin"}
"""),
            "mirada": [
                "401 es \"no sé quién eres\"; 403 es \"sé quién eres, pero no puedes\".",
                "La autorización se declara como dependencia.",
            ],
        },
        "proyecto": {
            "archivo": "src/dependencies.py",
            "lenguaje": "python",
            "codigo": c(r"""
def require_admin(usuario=Depends(usuario_actual)):
    if usuario.rol != "admin":
        raise HTTPException(403, "permiso insuficiente")
    return usuario

# src/routers/tableros.py
@router.delete("/api/tableros/{id}", dependencies=[Depends(require_admin)])
def eliminar(id: int):
    ...
"""),
            "mirada": [
                "El proyecto usa `require_admin` para acciones administrativas.",
                "El rol viene del JWT, no de un campo del cuerpo.",
            ],
        },
        "nota": "La diferencia entre 401 y 403 es una decisión de diseño, no un detalle.",
    },
    18: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.middleware("http")
async def limitar(request: Request, call_next):
    cliente = request.client.host
    if contador[cliente] >= 3:
        return JSONResponse(
            status_code=429,
            headers={"Retry-After": "60"},
            content={"error": "límite alcanzado"},
        )
    contador[cliente] += 1
    return await call_next(request)
"""),
            "mirada": [
                "El contador es por cliente, no global.",
                "`429` y `Retry-After` le dicen al cliente cuándo volver.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/rate_limit.py (opcional)",
            "lenguaje": "python",
            "codigo": c(r"""
class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if not limitador.permitir(request.client.host):
            return JSONResponse(status_code=429, content={"error": "límite"})
        return await call_next(request)
"""),
            "mirada": [
                "Rate limiting no es obligatorio en el proyecto.",
                "Si lo agregas, va en `core/` y cubre toda la API.",
            ],
        },
        "nota": "Concepto opcional en el proyecto; obligatorio en el laboratorio para entender el 429.",
    },
    19: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
import html

@app.post("/api/comentarios", status_code=201)
def crear(datos: Comentario):
    seguro = html.escape(datos.texto)
    comentarios.append({"id": len(comentarios) + 1, "texto": seguro})
    return comentarios[-1]
"""),
            "mirada": [
                "`html.escape` neutraliza etiquetas peligrosas.",
                "El texto se guarda ya escapado para no ejecutarse al mostrarlo.",
            ],
        },
        "proyecto": {
            "archivo": "src/schemas/tarea.py",
            "lenguaje": "python",
            "codigo": c(r"""
class TareaCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=120)

    @field_validator("titulo")
    @classmethod
    def limpiar(cls, valor: str) -> str:
        return html.escape(valor.strip())
"""),
            "mirada": [
                "El proyecto limpia el título antes de guardarlo.",
                "Escapar no es eliminar: el usuario ve el texto, el navegador no lo ejecuta.",
            ],
        },
        "nota": "En el proyecto, la validación de entrada y el escape de salida se complementan.",
    },
    20: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/token")
def token(datos: Login):
    usuario = autenticar(datos.usuario, datos.password)
    return {"access_token": crear_jwt(usuario), "token_type": "bearer"}

@app.get("/api/admin/panel")
def panel(admin=Depends(require_admin)):
    return {"panel": "admin"}
"""),
            "mirada": [
                "Registro, login, token, perfil y panel forman un solo pipeline.",
                "Cada paso se prueba por separado antes de integrarlo.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/auth.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.post("/api/token")
def login(datos: LoginRequest):
    usuario = servicio.autenticar(datos.usuario, datos.password)
    return {"access_token": crear_jwt(usuario), "token_type": "bearer"}

# src/main.py
app.include_router(auth.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
"""),
            "mirada": [
                "El Hito 2 del proyecto es este pipeline completo.",
                "Los routers de auth y admin se separan por responsabilidad.",
            ],
        },
        "nota": "El proyecto no inventa seguridad nueva: integra las piezas de las sesiones 11 a 19.",
    },
    21: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
import sqlite3

con = sqlite3.connect("biblioteca.db", check_same_thread=False)
con.execute(
    "CREATE TABLE IF NOT EXISTS libros ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "titulo TEXT NOT NULL, anio INTEGER NOT NULL)"
)
con.commit()

@app.post("/api/libros", status_code=201)
def crear(datos: Libro):
    cur = con.execute(
        "INSERT INTO libros (titulo, anio) VALUES (?, ?)", (datos.titulo, datos.anio)
    )
    con.commit()
    return {"id": cur.lastrowid, **datos.model_dump()}
"""),
            "mirada": [
                "La tabla se crea al iniciar; el dato sobrevive al reinicio.",
                "`commit()` confirma la escritura.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/database.py",
            "lenguaje": "python",
            "codigo": c(r"""
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine)

# src/main.py
@app.on_event("startup")
def iniciar():
    Base.metadata.create_all(engine)
"""),
            "mirada": [
                "El proyecto usa SQLAlchemy; el laboratorio usa `sqlite3` para ver el SQL.",
                "En el Hito 3 se cambia `create_all` por una migración.",
            ],
        },
        "nota": "El laboratorio te muestra el SQL; el proyecto lo encapsula en un ORM.",
    },
    22: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
class Autor(Base):
    __tablename__ = "autores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80))
    libros: Mapped[list["Libro"]] = relationship(back_populates="autor")

class Libro(Base):
    __tablename__ = "libros"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(80))
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor: Mapped["Autor"] = relationship(back_populates="libros")
"""),
            "mirada": [
                "`ForeignKey` conecta las tablas; `relationship` conecta los objetos.",
                "La relación 1:N se declara una vez y se usa en ambos lados.",
            ],
        },
        "proyecto": {
            "archivo": "src/models/tablero.py",
            "lenguaje": "python",
            "codigo": c(r"""
class Tablero(Base):
    __tablename__ = "tableros"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    tareas: Mapped[list["Tarea"]] = relationship(back_populates="tablero")
"""),
            "mirada": [
                "El proyecto tiene `Tablero` 1:N `Tarea`.",
                "`usuario_id` conecta el tablero con su dueño.",
            ],
        },
        "nota": "La relación del proyecto es la misma idea: un padre, muchos hijos.",
    },
    23: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/libros", status_code=201)
async def crear(datos: Libro, sesion: AsyncSession = Depends(get_sesion)):
    libro = LibroModel(**datos.model_dump())
    sesion.add(libro)
    await sesion.commit()
    await sesion.refresh(libro)
    return libro
"""),
            "mirada": [
                "`async`/`await` evita bloquear el servidor mientras espera la base.",
                "La sesión se inyecta; el endpoint no la construye.",
            ],
        },
        "proyecto": {
            "archivo": "src/repositories/tablero_repo.py",
            "lenguaje": "python",
            "codigo": c(r"""
class TableroRepository:
    def __init__(self, sesion: AsyncSession):
        self.sesion = sesion

    async def crear(self, datos: TableroCreate) -> Tablero:
        tablero = Tablero(**datos.model_dump())
        self.sesion.add(tablero)
        await self.sesion.commit()
        await self.sesion.refresh(tablero)
        return tablero
"""),
            "mirada": [
                "El repositorio encapsula la sesión y el `commit`.",
                "El router del proyecto no sabe cómo se guarda.",
            ],
        },
        "nota": "En el proyecto, la persistencia asíncrona vive en la capa de repositorio.",
    },
    24: {
        "lab": {
            "archivo": "migrations/versions/0001_crear_libros.py",
            "lenguaje": "python",
            "codigo": c(r"""
def upgrade():
    op.create_table(
        "libros",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("titulo", sa.String(80), nullable=False),
        sa.Column("anio", sa.Integer, nullable=False),
    )

def downgrade():
    op.drop_table("libros")
"""),
            "mirada": [
                "`upgrade` construye; `downgrade` deshace exactamente lo construido.",
                "La migración es un archivo versionado, no un `create_all`.",
            ],
        },
        "proyecto": {
            "archivo": "migrations/versions/0001_tableros.py",
            "lenguaje": "python",
            "codigo": c(r"""
def upgrade():
    op.create_table(
        "tableros",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.String(80), nullable=False),
        sa.Column("usuario_id", sa.Integer, sa.ForeignKey("usuarios.id")),
    )
"""),
            "mirada": [
                "El proyecto aplica `alembic upgrade head` antes de la demo.",
                "La llave foránea también forma parte de la migración.",
            ],
        },
        "nota": "Una migración bien escrita permite crear la base desde cero y revertirla.",
    },
    25: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
from sqlalchemy import select
from sqlalchemy.orm import selectinload

autores = sesion.execute(
    select(Autor).options(selectinload(Autor.libros))
).scalars().all()

return {"autores": [
    {"id": a.id, "nombre": a.nombre, "libros": [l.titulo for l in a.libros]}
    for a in autores
]}
"""),
            "mirada": [
                "`selectinload` evita una consulta por cada autor.",
                "El resultado es el mismo; cambia cuántas consultas haces.",
            ],
        },
        "proyecto": {
            "archivo": "src/repositories/tablero_repo.py",
            "lenguaje": "python",
            "codigo": c(r"""
consulta = select(Tablero).options(selectinload(Tablero.tareas))
tableros = (await sesion.execute(consulta)).scalars().all()
return [
    {"id": t.id, "nombre": t.nombre, "tareas": [x.titulo for x in t.tareas]}
    for t in tableros
]
"""),
            "mirada": [
                "El proyecto carga las tareas del tablero en una consulta adicional.",
                "Así el listado no dispara el problema N+1.",
            ],
        },
        "nota": "La carga ansiosa es una optimización que se nota cuando hay muchos registros.",
    },
    26: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
try:
    con.execute("UPDATE libros SET ejemplares = ejemplares - 1 WHERE id = ?", (libro_id,))
    cur = con.execute(
        "INSERT INTO prestamos (libro_id, usuario) VALUES (?, ?)", (libro_id, usuario)
    )
    con.commit()
    return {"prestamo_id": cur.lastrowid}
except Exception:
    con.rollback()
    raise HTTPException(409, "no se pudo registrar el préstamo")
"""),
            "mirada": [
                "Las dos escrituras se confirman juntas o no se confirma ninguna.",
                "`rollback` evita dejar el stock a medias.",
            ],
        },
        "proyecto": {
            "archivo": "src/services/tablero_service.py",
            "lenguaje": "python",
            "codigo": c(r"""
async with sesion.begin():
    tablero = await repo.obtener(tablero_id)
    if not tablero:
        raise NoEncontrado("Tablero")
    tarea = await repo.crear_tarea(tablero_id, datos)
    await repo.actualizar_contador(tablero_id)
"""),
            "mirada": [
                "El proyecto usa `async with sesion.begin()` para operaciones compuestas.",
                "Si algo falla, el contexto hace rollback automáticamente.",
            ],
        },
        "nota": "Una operación compuesta sin transacción es una fuente clásica de datos inconsistentes.",
    },
    27: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.get("/api/libros/buscar")
def buscar(titulo: str = ""):
    filas = con.execute(
        "SELECT id, titulo FROM libros WHERE titulo LIKE ?",
        (f"%{titulo}%",),
    ).fetchall()
    return {"libros": [{"id": f[0], "titulo": f[1]} for f in filas]}
"""),
            "mirada": [
                "El `?` separa la estructura de la consulta del dato del usuario.",
                "El payload `' OR '1'='1` se trata como texto, no como SQL.",
            ],
        },
        "proyecto": {
            "archivo": "src/repositories/tablero_repo.py",
            "lenguaje": "python",
            "codigo": c(r"""
async def buscar(self, texto: str) -> list[Tablero]:
    consulta = select(Tablero).where(Tablero.nombre.ilike(f"%{texto}%"))
    return list((await self.sesion.execute(consulta)).scalars().all())
"""),
            "mirada": [
                "El proyecto usa SQLAlchemy, pero el principio es el mismo: parámetros.",
                "Nunca concatenes entrada del usuario en una consulta.",
            ],
        },
        "nota": "ORM o SQL crudo: la regla es no construir la consulta pegando texto del usuario.",
    },
    28: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.ejemplo.com"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)
"""),
            "mirada": [
                "Solo el origen de la lista blanca recibe permiso.",
                "El navegador decide si muestra la respuesta; el servidor declara a quién autoriza.",
            ],
        },
        "proyecto": {
            "archivo": "src/main.py",
            "lenguaje": "python",
            "codigo": c(r"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Authorization"],
)
"""),
            "mirada": [
                "El proyecto lee los orígenes desde `.env`, no los escribe en el código.",
                "`allow_origins` nunca debería ser `*` en producción.",
            ],
        },
        "nota": "La lista blanca es una decisión de configuración; el `*` es una puerta abierta.",
    },
    29: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/logout", status_code=204)
def logout(response: Response, session: str | None = Cookie(default=None),
           x_csrf_token: str | None = Header(default=None)):
    if x_csrf_token != sesiones[session]["csrf"]:
        raise HTTPException(403, "token CSRF inválido")
    del sesiones[session]
    response.delete_cookie("session")
"""),
            "mirada": [
                "La cookie demuestra quién eres; el token demuestra que la acción la pediste tú.",
                "Sin token CSRF, la petición se rechaza con 403.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/security.py",
            "lenguaje": "python",
            "codigo": c(r"""
def crear_cookie(response: Response, token: str) -> None:
    response.set_cookie(
        "access_token",
        token,
        httponly=True,
        samesite="lax",
        secure=settings.entorno == "prod",
    )
"""),
            "mirada": [
                "El proyecto usa Bearer por defecto; si migras a cookies, aplica esta configuración.",
                "`Secure` solo en producción con HTTPS.",
            ],
        },
        "nota": "CSRF es obligatorio si usas cookies; con Bearer en el encabezado, el riesgo cambia.",
    },
    30: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.get("/health")
def health():
    con.execute("SELECT 1")
    return {"status": "ok"}

@app.get("/api/libros/buscar")
def buscar(titulo: str = ""):
    filas = con.execute(
        "SELECT * FROM libros WHERE titulo LIKE ?", (f"%{titulo}%",)
    ).fetchall()
    return {"libros": filas}
"""),
            "mirada": [
                "El hito integra persistencia, búsqueda segura y CORS.",
                "El healthcheck consulta la base, no solo el proceso.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/health.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.get("/health")
async def health(sesion: AsyncSession = Depends(get_sesion)):
    await sesion.execute(text("SELECT 1"))
    return {"status": "ok"}

# src/main.py
app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins)
"""),
            "mirada": [
                "El Hito 3 del proyecto integra DB, SQLi y CORS.",
                "El tag `v0.3-hito3` marca el cierre de esta etapa.",
            ],
        },
        "nota": "La seguridad no es un módulo aparte: es una propiedad de todo el sistema.",
    },
    31: {
        "lab": {
            "archivo": "Dockerfile",
            "lenguaje": "docker",
            "codigo": c(r"""
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""),
            "mirada": [
                "Las dependencias se copian antes del código para aprovechar la caché.",
                "El contenedor corre con un usuario sin privilegios.",
            ],
        },
        "proyecto": {
            "archivo": "Dockerfile",
            "lenguaje": "docker",
            "codigo": c(r"""
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""),
            "mirada": [
                "El proyecto solo cambia la ruta `src.main:app`.",
                "El resto del Dockerfile es el mismo patrón del laboratorio.",
            ],
        },
        "nota": "La imagen no debe copiar `.env` ni ejecutarse como root.",
    },
    32: {
        "lab": {
            "archivo": "config.py",
            "lenguaje": "python",
            "codigo": c(r"""
import os

def cargar_config():
    database_url = os.getenv("DATABASE_URL")
    secret_key = os.getenv("SECRET_KEY")
    if not database_url or not secret_key:
        raise RuntimeError("Faltan variables obligatorias")
    return {
        "database_url": database_url,
        "secret_key": secret_key,
        "entorno": os.getenv("ENTORNO", "dev"),
    }
"""),
            "mirada": [
                "Si falta una variable obligatoria, el servidor no arranca.",
                "Los secretos viven en el entorno, no en el repositorio.",
            ],
        },
        "proyecto": {
            "archivo": "src/core/config.py",
            "lenguaje": "python",
            "codigo": c(r"""
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    entorno: str = "dev"
    cors_origins: list[str] = []

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
"""),
            "mirada": [
                "El proyecto usa `pydantic-settings` para validar al arrancar.",
                "`.env.example` documenta las variables sin valores reales.",
            ],
        },
        "nota": "La configuración se lee una vez; el resto del código recibe `settings`.",
    },
    33: {
        "lab": {
            "archivo": "gunicorn_conf.py",
            "lenguaje": "python",
            "codigo": c(r"""
import multiprocessing

workers = 2 * multiprocessing.cpu_count() + 1
worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:8000"
timeout = 60
"""),
            "mirada": [
                "La fórmula de workers equilibra CPU y espera de I/O.",
                "`UvicornWorker` permite que Gunicorn hable ASGI.",
            ],
        },
        "proyecto": {
            "archivo": "nginx.conf",
            "lenguaje": "nginx",
            "codigo": c(r"""
upstream api { server 127.0.0.1:8000; }

server {
    listen 80;
    client_max_body_size 10M;
    gzip on;
    location / { proxy_pass http://api; }
}
"""),
            "mirada": [
                "Nginx recibe el tráfico y lo pasa a la aplicación.",
                "El proyecto usa Codespaces/Render; Nginx es el patrón de producción.",
            ],
        },
        "nota": "En producción no se usa `uvicorn --reload`: consume memoria y reinicia el proceso.",
    },
    34: {
        "lab": {
            "archivo": "app.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
async function cargarLibros() {
  const response = await fetch("/api/libros");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const datos = await response.json();
  document.querySelector("#lista").innerHTML =
    datos.libros.map((l) => `<li>${l.titulo}</li>`).join("");
}
"""),
            "mirada": [
                "`fetch` no falla en un 404: hay que revisar `response.ok`.",
                "`response.json()` también devuelve una promesa.",
            ],
        },
        "proyecto": {
            "archivo": "frontend/app.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
async function cargarTableros() {
  const response = await fetch("/api/tableros", {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const datos = await response.json();
  renderTableros(datos.tableros);
}
"""),
            "mirada": [
                "El proyecto agrega el token porque sus rutas están protegidas.",
                "El cliente no sabe si el error es 401 o 403; el mensaje lo explica.",
            ],
        },
        "nota": "El mismo `fetch`; el proyecto añade autenticación y una función de render.",
    },
    35: {
        "lab": {
            "archivo": "app.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
const estado = { libros: [] };

function render() {
  document.querySelector("#lista").innerHTML = estado.libros
    .map((l) => `<li>${l.titulo}</li>`)
    .join("");
}

function agregar(libro) {
  estado.libros.push(libro);
  render();
}
"""),
            "mirada": [
                "El estado es la fuente de verdad; el DOM es una consecuencia.",
                "Si cambias el DOM a mano y no el estado, el próximo render lo revive.",
            ],
        },
        "proyecto": {
            "archivo": "frontend/app.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
const estado = { tableros: [], tareas: [] };

function render() {
  document.querySelector("#tableros").innerHTML = estado.tableros
    .map((t) => `<li>${t.nombre}</li>`)
    .join("");
}
"""),
            "mirada": [
                "El proyecto mantiene dos listas en el estado.",
                "`render()` se llama después de cada cambio, no en cada clic a mano.",
            ],
        },
        "nota": "La interfaz del proyecto se reconstruye desde el estado, igual que en el laboratorio.",
    },
    36: {
        "lab": {
            "archivo": "router.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
async function renderRoute() {
  const hash = location.hash || "#/libros";
  if (hash === "#/libros") {
    const r = await fetch("/api/libros");
    const datos = await r.json();
    app.innerHTML = datos.libros.map((l) => `<p>${l.titulo}</p>`).join("");
  }
}
window.addEventListener("hashchange", renderRoute);
"""),
            "mirada": [
                "El hash no viaja al servidor; el navegador se lo entrega a JavaScript.",
                "`hashchange` permite cambiar de vista sin recargar.",
            ],
        },
        "proyecto": {
            "archivo": "frontend/router.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
async function renderRoute() {
  const hash = location.hash || "#/tableros";
  if (hash === "#/tableros") return renderTableros();
  if (hash.startsWith("#/tableros/")) return renderTareas(hash.split("/")[2]);
  app.innerHTML = "<h2>404</h2>";
}
window.addEventListener("hashchange", renderRoute);
"""),
            "mirada": [
                "El proyecto usa `#/tableros` y `#/tableros/{id}`.",
                "Una ruta desconocida muestra 404 sin recargar.",
            ],
        },
        "nota": "La SPA del proyecto tiene dos vistas: tableros y tareas.",
    },
    37: {
        "lab": {
            "archivo": "coleccion.json",
            "lenguaje": "json",
            "codigo": c(r"""
{
  "info": {
    "name": "Biblioteca E2E",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    { "name": "login", "event": [{ "listen": "test", "script": { "exec": [
      "pm.response.to.have.status(200);",
      "pm.environment.set('token', pm.response.json().access_token);"
    ] } }] }
  ]
}
"""),
            "mirada": [
                "La colección encadena peticiones: el token del login se usa después.",
                "Las aserciones validan estado y cuerpo, no solo que responda.",
            ],
        },
        "proyecto": {
            "archivo": "tests/e2e/coleccion.json",
            "lenguaje": "json",
            "codigo": c(r"""
{
  "name": "Proyecto E2E",
  "item": [
    { "name": "crear tablero",
      "request": { "method": "POST", "url": "{{base_url}}/api/tableros",
        "header": [{ "key": "Authorization", "value": "Bearer {{token}}" }] } }
  ]
}
"""),
            "mirada": [
                "El proyecto usa la misma colección con sus rutas y su dominio.",
                "La variable `{{token}}` viene del login anterior.",
            ],
        },
        "nota": "Una prueba E2E no es solo el 200: también valida el JSON y el flujo.",
    },
    38: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.post("/api/reportes", status_code=202)
def crear(datos: Reporte, bg: BackgroundTasks):
    tarea_id = str(uuid.uuid4())[:8]
    tareas[tarea_id] = {"estado": "en_proceso"}
    bg.add_task(procesar, tarea_id, datos.email)
    return {"tarea_id": tarea_id, "estado": "en_proceso"}

def procesar(tarea_id: str, email: str):
    with open("reportes.log", "a") as f:
        f.write(email + "\n")
    tareas[tarea_id]["estado"] = "completado"
"""),
            "mirada": [
                "El cliente recibe 202 antes de que termine el trabajo.",
                "`bg.add_task` ejecuta la función después de responder.",
            ],
        },
        "proyecto": {
            "archivo": "src/services/reportes.py",
            "lenguaje": "python",
            "codigo": c(r"""
async def enviar_reporte(email: str, bg: BackgroundTasks):
    bg.add_task(_enviar_email, email)

def _enviar_email(email: str):
    # aquí iría el cliente de correo
    ...
"""),
            "mirada": [
                "El proyecto puede usar `BackgroundTasks` para correos o reportes.",
                "La respuesta no espera al envío real del correo.",
            ],
        },
        "nota": "Tareas en segundo plano: la respuesta es inmediata, el efecto llega después.",
    },
    39: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.get("/health")
def health(simular_fallo: bool = False):
    if simular_fallo:
        return JSONResponse(status_code=503, content={"status": "error"})
    con.execute("SELECT 1")
    return {"status": "ok", "db": "ok", "version": "1.0.0"}

@app.get("/api/metricas")
def metricas():
    return {"uptime": 12.4, "version": "1.0.0"}
"""),
            "mirada": [
                "El healthcheck es barato: un `SELECT 1` basta.",
                "Si la dependencia falla, responde 503, no 200.",
            ],
        },
        "proyecto": {
            "archivo": "src/routers/health.py",
            "lenguaje": "python",
            "codigo": c(r"""
@router.get("/health")
async def health(sesion: AsyncSession = Depends(get_sesion)):
    await sesion.execute(text("SELECT 1"))
    return {"status": "ok", "db": "ok", "version": settings.version}
"""),
            "mirada": [
                "El proyecto expone `/health` para la demo y el monitoreo.",
                "La versión viene de la configuración, no está escrita a mano.",
            ],
        },
        "nota": "Un healthcheck que no consulta la base puede mentir sobre la salud del sistema.",
    },
    40: {
        "lab": {
            "archivo": "app.py",
            "lenguaje": "python",
            "codigo": c(r"""
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/token")
def token(datos: Login):
    usuario = autenticar(datos.usuario, datos.password)
    return {"access_token": crear_jwt(usuario), "token_type": "bearer"}

@app.get("/api/admin/panel")
def panel(admin=Depends(require_admin)):
    return {"panel": "admin"}
"""),
            "mirada": [
                "El Hito 4 une autenticación, roles, persistencia y salud.",
                "La demo no es un video: es el sistema respondiendo en vivo.",
            ],
        },
        "proyecto": {
            "archivo": "frontend/app.js",
            "lenguaje": "javascript",
            "codigo": c(r"""
async function cargar() {
  const response = await fetch("/api/tableros", {
    headers: { Authorization: `Bearer ${token}` },
  });
  const datos = await response.json();
  renderTableros(datos.tableros);
}
"""),
            "mirada": [
                "El frontend consume la API protegida con Bearer.",
                "El tag `v1.0-final` marca el commit de la demo.",
            ],
        },
        "nota": "El proyecto completo es la suma de los cuatro hitos; la demo muestra el flujo de extremo a extremo.",
    },
}
