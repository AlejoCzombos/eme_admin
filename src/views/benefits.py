from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette_admin import StringField, FileField
from starlette.requests import Request
from sqlalchemy_file import ImageField

from sqlalchemy import text, asc, desc
from src.database import Session
from src.models.benefits import Beneficio, Localidad

class BeneficioView(ModelView):
    search_builder = False
    fields = ["titulo", "descripcion", "descuento", 
              StringField("texto_descuento", label="Texto descuento", help_text="Si se completa este campo, reemplazará al campo de descuento al momento de mostrarlo"), 
              FileField("imagen", help_text="La imagen debe estar en formato cuadrado y debe poseer un tamaño máximo de 800x800 px", accept="image/*"), "categoria", "localidad"]
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        if not data.get("titulo"):
            errors["titulo"] = "El título es requerido"
        if not data.get("descuento"):
            errors["descuento"] = "El descuento es requerido"
        if not data.get("imagen") or not data["imagen"][0]:
            errors["imagen"] = "La imagen es requerida"
        if not data.get("categoria"):
            errors["categoria"] = "La categoría es requerida"
        if not data.get("localidad"):
            errors["localidad"] = "La localidad es requerida"
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where=None,
        order_by=None,
    ):
        db_session = Session()
        try:
            query = db_session.query(Beneficio)
            
            sucursal_id = request.state.user.get("sucursal_id")
            if sucursal_id:
                query = query.filter(text("localidad_id = :localidad_id")).params(localidad_id=sucursal_id)
            
            if where:
                query = query.filter(text("titulo LIKE :titulo OR descuento LIKE :descuento OR descripcion LIKE :descripcion")).params(descuento=f"%{where}%", titulo=f"%{where}%", descripcion=f"%{where}%")

            if order_by:
                for order in order_by:
                    key, direction = order.split(maxsplit=1)
                    if direction.lower() == "asc":
                        query = query.order_by(asc(key))
                    elif direction.lower() == "desc":
                        query = query.order_by(desc(key))
            
            query = query.offset(skip).limit(limit)
            result = query.all()
            return result
        finally:
            # db_session.close()
            pass

    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]


class CategoriaBeneficioView(ModelView):
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


class LocalidadView(ModelView):
    search_builder = False
    
    # def is_accessible(self, request: Request) -> bool:
    #     return "admin" in request.state.user["roles"]
    
    def can_view_details(self, request: Request) -> bool:
        return "branch_admin" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]
    
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where = None,
        order_by = None,
    ):
        db_session = Session()
        query = db_session.query(Localidad)
    
        sucursal_id = request.state.user.get("sucursal_id")
        if sucursal_id:
            query = query.filter(text("id = :localidad_id")).params(localidad_id=sucursal_id)

        results = query.all()
        
        db_session.close()
        
        return results