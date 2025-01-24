from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette.requests import Request
from datetime import datetime, timedelta

from src.database import get_db
from src.models.administrator import Token, Administrador, AdministradorActualCorrientes, AdministradorActualResistencia, AdministradorActualSaenzPeña, FormError

class AdministradorActualCorrientesView(ModelView):
    fields = ["administrador"]
    search_builder = False
    
    async def validate(self, request: Request, data: dict()) -> None:
        errors: Dict[str, str] = dict()
        
        with get_db() as db_session:
            existing_admin = db_session.query(AdministradorActualCorrientes).first()
            if existing_admin:
                errors["administrador"] = "Ya existe un administrador actual. Elimínalo antes de agregar otro."
        
        
        # if not data.get("administrador"):
        #     errors["administrador"] = "El administrador es requerido."
        
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

class AdministradorActualResistenciaView(ModelView):
    fields = ["administrador"]
    search_builder = False
    
    async def validate(self, request: Request, data: dict()) -> None:
        errors: Dict[str, str] = dict()
        
        with get_db() as db_session:
            existing_admin = db_session.query(AdministradorActualSaenzPeña).first()
            if existing_admin:
                errors["administrador"] = "Ya existe un administrador actual. Elimínalo antes de agregar otro."
        
        
        # if not data.get("administrador"):
        #     errors["administrador"] = "El administrador es requerido."
        
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

class AdministradorActualSaenzPeñaView(ModelView):
    fields = ["administrador"]
    search_builder = False
    
    async def validate(self, request: Request, data: dict()) -> None:
        errors: Dict[str, str] = dict()
        
        with get_db() as db_session:
            existing_admin = db_session.query(AdministradorActualCorrientes).first()
            if existing_admin:
                errors["administrador"] = "Ya existe un administrador actual. Elimínalo antes de agregar otro."
        
        
        # if not data.get("administrador"):
        #     errors["administrador"] = "El administrador es requerido."
        
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

class AdministradorView(ModelView):
    search_builder = False
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

class TokenView(ModelView):
    search_builder = False
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        
        with get_db() as db_session:
            existing_token = db_session.query(Token).first()
            if existing_token:
                errors["token"] = "Ya existe un token. Elimínalo antes de agregar otro."
    
        
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

class FormErrorsView(ModelView):
    fields = ["fecha_hora", "tipo_de_error", "mensaje_error"]
    search_builder = False
    sortable_fields = ["fecha_hora", "tipo_de_error", "mensaje_error"]
    
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where=None,
        order_by=None,
    ):
        with get_db() as db_session:
            query = db_session.query(FormError)

            if order_by:
                for order in order_by:
                    key, direction = order.split(maxsplit=1)
                    if key == "fecha_hora":
                        key = FormError.fecha_hora
                    elif key == "tipo_de_error":
                        key = FormError.tipo_de_error
                    elif key == "mensaje_error":
                        key = FormError.mensaje_error
                    
                    if direction.lower() == "asc":
                        query = query.order_by(asc(key))
                    elif direction.lower() == "desc":
                        query = query.order_by(desc(key))
            
            query = query.offset(skip).limit(limit)
            result : list = query.all()
            
            one_week_ago = datetime.now() - timedelta(weeks=1)
            for error in result:
                if error.fecha_hora < one_week_ago:
                    result.remove(error)
                    db_session.delete(error)
                    db_session.commit()
            
            return result
    
    def can_create(self, request: Request) -> bool:
        return False

    def can_edit(self, request: Request) -> bool:
        return False

    def can_delete(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]
    