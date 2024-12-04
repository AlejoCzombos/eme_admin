from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles

from src.admin import admin
from src.database import Base, engine
from src.storage import setup_storage

Base.metadata.create_all(engine)

setup_storage()

app = Starlette(
    routes=[
        Mount(
            "/static", app=StaticFiles(directory="static"), name="static"
        ),
        Route(
            "/",
            lambda r: HTMLResponse('<a href="/admin/">Click me to get to Admin!</a>'),
        ),
    ]
)

admin.mount_to(app)