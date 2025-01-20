from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette_admin import StringField, FileField
from starlette.requests import Request

class BannerView(ModelView):
    fields = [FileField("imagen", help_text="El banner debe poseer un tamaño de 1730 px de ancho y 497 px de alto", accept="image/*")]
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        if not data.get("imagen") or not data["imagen"][0]:
            errors["imagen"] = "La imagen es requerida"
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    
    # def is_accessible(self, request: Request) -> bool:
    #     return "admin" in request.state.user["roles"]
    
    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

class SponsorView(ModelView):
    fields = [FileField("imagen", help_text="El logo debe estar en formato cuadrado y debe poseer un tamaño máximo de 800x800 px", accept="image/*")]
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        if not data.get("logo") or not data["logo"][0]:
            errors["logo"] = "El logo es requerido"
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    # def is_accessible(self, request: Request) -> bool:
    #     return "admin" in request.state.user["roles"]
    
    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]