from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin import DropDown
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from src.database import engine

from src.models.benefits import *
from src.views.benefits import *
from src.models.specialists import *
from src.views.specialists import *
from src.models.administrator import *
from src.views.administrator import *
from src.models.images import *
from src.views.images import *
from src.auth import MyAuthProvider
from src.config import SECRET

admin = Admin(
    engine,
    title="EME admin",
    base_url="/admin",
    statics_dir="static/",
    login_logo_url="/admin/statics/logo.png",  # base_url + '/statics/' + path_to_the_file
    auth_provider=MyAuthProvider(),
    middlewares=[Middleware(SessionMiddleware, secret_key=SECRET)],
    debug=False
)

admin.add_view(
    DropDown(
        "Beneficios",
        icon="fa fa-ticket",
        views=[
            BeneficioView(Beneficio, icon="fas fa-list", label="Beneficios"),
            CategoriaBeneficioView(CategoriaBeneficio, icon="fas fa-list", label="Categorías de beneficios")
        ]
    )
)

admin.add_view(
    DropDown(
        "Policonsultorios",
        icon="fa fa-user-md",
        views=[
            EspecialistaView(Especialista, icon="fas fa-list", label="Especialistas"),
            EspecialidadView(Especialidad, icon="fas fa-list", label="Especialidades"),
        ]
    )
)

admin.add_view(
    DropDown(
        "Administradores",
        icon="fa fa-user",
        views=[
            FormErrorsView(FormError, icon="fas fa-list", label="Errores de formularios"),
            AdministradorView(Administrador, icon="fas fa-list", label="Administradores"),
            TokenView(Token, icon="fas fa-list", label="Token actual (único)"),
            AdministradorActualCorrientesView(AdministradorActualCorrientes, icon="fas fa-list", label="Admin actual Corrientes (único)"),
            AdministradorActualResistenciaView(AdministradorActualResistencia, icon="fas fa-list", label="Admin actual Resistencia (único)"),
            AdministradorActualSaenzPeñaView(AdministradorActualSaenzPeña, icon="fas fa-list", label="Admin actual Sáenz Peña (Sin implementar)"),
        ]
    )
)

admin.add_view(
    DropDown(
        "Imágenes",
        icon="fa fa-image",
        views=[
            BannerView(Banner, icon="fas fa-list", label="Banners"),
            BeneficiosHomeView(BeneficiosHome, icon="fas fa-list", label="Comercios adheridos visibles en el home")
        ]
    )
)

admin.add_view(
    DropDown(
        "Otros",
        icon="fa fa-list",
        views=[
            LocalidadView(Localidad, icon="fas fa-list", label="Localidades"),
            DiaView(Dia, icon="fas fa-list", label="Días")
        ]
    )
)