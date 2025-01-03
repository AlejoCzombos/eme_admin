from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from src.admin import admin
from src.database import Base, engine
from src.storage import setup_storage
from src.api.benefits import beneficios
from src.api.images import Banners, Sponsors
from src.api.specialists import Especialistas
from src.api.form import FormularioEndpoint 

Base.metadata.create_all(engine)

setup_storage()

routes = [
    Mount(
        "/static", app=StaticFiles(directory="static"), name="static"
    ),
    Route(
        "/",
        RedirectResponse(url="/admin"),
    ),
    Route(
      "/api/beneficios", beneficios
    ),
    Route(
        "/api/especialistas", Especialistas
    ),
    Route(
        "/api/sponsors", Sponsors
    ),
    Route(
        "/api/banners", Banners
    ),
    Route(
        "/api/form", FormularioEndpoint, methods=["POST"]
    ),
]

app = Starlette(routes=routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

admin.mount_to(app)