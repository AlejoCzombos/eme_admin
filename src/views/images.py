from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette_admin import StringField, FileField, CollectionField, ListField
from starlette.requests import Request

from typing import Dict, Any
from src.database import get_db
from src.models.images import Banner

class BannerView(ModelView):
    pk_attr = "id"
    search_builder = False
    fields = [
        FileField("imagen", help_text="El banner debe poseer un tamaño de 1730 px de ancho y 497 px de alto", accept="image/*"), 
        
        StringField("titulo", help_text="El título del banner, máximo 25 caracteres"),
        StringField("descripcion", help_text="La descripción del banner, máximo 230 caracteres"),
        StringField("boton_texto", help_text="El texto del botón del banner, maximo 25 caracteres"),
        StringField("boton_url", help_text="La URL a la que redirigirá el botón del banner. Aclaración: No es necesario agregar el dominio para referenciar a partes de la página, solo la ruta de la página. ejemplo: '/beneficios' o '/servicios/familiares'"),
    ]
    
    async def validate(self, request: Request, data: Dict[str, Any]) -> None:
        id_banner = request.path_params.get("pk")
        errors = {}
        
        if not data.get("imagen") or not data["imagen"][0]:
            if not id_banner:
                errors["imagen"] = "La imagen es requerida"
            else:
                with get_db() as db_session:
                    banner = db_session.query(Banner).get(id_banner)
                    print("el banner existe con id", id_banner)
                    if not banner.imagen:
                        errors["imagen"] = "La imagen es requerida"
        
        if data.get("titulo") and data.get("descripcion") and data.get("boton_texto") and data.get("boton_url"):
            if len(data["titulo"]) > 25:
                errors["titulo"] = "El título no puede tener más de 25 caracteres"
            if len(data["descripcion"]) > 230:
                errors["descripcion"] = "La descripción no puede tener más de 230 caracteres"
            if len(data["boton_texto"]) > 25:
                errors["boton_texto"] = "El texto del botón no puede tener más de 25 caracteres"
            if len(data["boton_url"]) > 200:
                errors["boton_url"] = "La URL del botón no puede tener más de 200 caracteres"
        
        elif data.get("titulo") or data.get("descripcion") or data.get("boton_texto") or data.get("boton_url"):
            if not data.get("titulo"):
                errors["titulo"] = "El título es requerido (deben completarse todos los campos)"
            if not data.get("descripcion"):
                errors["descripcion"] = "La descripción es requerida (deben completarse todos los campos)"
            if not data.get("boton_texto"):
                errors["boton_texto"] = "El texto del botón es requerido (deben completarse todos los campos)"
            if not data.get("boton_url"):
                errors["boton_url"] = "La URL del botón es requerida (deben completarse todos los campos)"
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]