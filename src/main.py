from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from src.admin import admin
from src.database import Base, engine
from src.storage import setup_storage
from src.api.benefits import beneficios, Imagenes

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
        "/api/images/{file_id}", Imagenes
    )
]

app = Starlette(routes=routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

admin.mount_to(app)