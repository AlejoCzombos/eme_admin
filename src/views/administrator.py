from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette.requests import Request

from src.database import Session
from src.models.administrator import Token, AdministradorActual, Administrador

class AdministradorActualView(ModelView):
    fields = ["administrador"]
    
    async def validate(self, request: Request, data: dict()) -> None:
        errors: Dict[str, str] = dict()
        
        db_session = Session()
        try:
            existing_admin = db_session.query(AdministradorActual).first()
            if existing_admin:
                errors["administrador"] = "Ya existe un administrador actual. Elimínalo antes de agregar otro."
        finally:
            db_session.close()
        
        
        # if not data.get("administrador"):
        #     errors["administrador"] = "El administrador es requerido."
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)

    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

class AdministradorView(ModelView):
    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

class TokenView(ModelView):
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        
        db_session = Session()
        try:
            existing_token = db_session.query(Token).first()
            if existing_token:
                errors["token"] = "Ya existe un token. Elimínalo antes de agregar otro."
        finally:
            db_session.close()
    
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]