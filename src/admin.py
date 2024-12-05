from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin import DropDown
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from src.database import engine, db_session

from src.models.benefits import *
from src.views.benefits import *
from src.auth import MyAuthProvider
from src.config import SECRET

admin = Admin(
    engine,
    title="EME admin",
    base_url="/admin",
    statics_dir="static/",
    login_logo_url="/admin/statics/logo.png",  # base_url + '/statics/' + path_to_the_file
    auth_provider=MyAuthProvider(db_session=db_session),
    middlewares=[Middleware(SessionMiddleware, secret_key=SECRET)],
)

admin.add_view(
    DropDown(
        "Beneficios",
        icon="fa fa-ticket",
        views=[
            BeneficioView(Beneficio, icon="fas fa-list"),
            CategoriaBeneficioView(CategoriaBeneficio, icon="fas fa-list"),
            LocalidadView(Localidad, icon="fas fa-list")
        ]
    )
)
