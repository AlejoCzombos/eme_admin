from starlette_admin.contrib.sqla import ModelView
from starlette_admin.exceptions import FormValidationError
from starlette.requests import Request

from sqlalchemy import text, asc, desc
from sqlalchemy.orm import joinedload
from src.database import get_db
from src.models.specialists import Dia, Especialidad, Especialista

from typing import Any, Dict, List, Optional, Sequence, Union

class EspecialidadView(ModelView):
    search_builder = False
    fields = ["nombre"]
    
    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

class EspecialistaView(ModelView):
    search_builder = False
    sortable_fields = ["nombre", "matricula", "localidad", "especialidad", "dias"]
    fields = ["nombre", "matricula", "localidad", "especialidad", "dias"]
    
    async def validate(self, request: Request, data) -> None:
        errors: Dict[str, str] = dict()
        
        if not data.get("nombre"):
            errors["nombre"] = "El título es requerido"
        if not data.get("matricula"):
            errors["matricula"] = "La matricula es requerida"
        if not data.get("localidad"):
            errors["localidad"] = "La sucursal es requerida"
        if not data.get("especialidad"):
            errors["especialidad"] = "La especialidad es requerida"
        if not data.get("dias"):
            errors["dias"] = "El dia es requerido"
        
        if len(errors) > 0:
            raise FormValidationError(errors)
        return await super().validate(request, data)
    
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where = None,
        order_by = None,
    ):
        with get_db() as db_session:
            query = db_session.query(Especialista).options(joinedload(Especialista.localidad), joinedload(Especialista.especialidad), joinedload(Especialista.dias))
            
            sucursal_id = request.state.user.get("sucursal_id")
            if sucursal_id:
                query = query.filter(text("localidad_id = :localidad_id")).params(localidad_id=sucursal_id)
            
            # Where is the input from the search bar
            if where:
                query = query.filter(text("nombre LIKE :nombre OR matricula LIKE :matricula")).params(nombre=f"%{where}%", matricula=f"%{where}%")

            if order_by:
                for order in order_by:
                    key, direction = order.split(maxsplit=1)
                    if key == "nombre":
                        key = Especialista.nombre
                    if key == "id":
                        key = Especialista.id
                    elif key == "matricula":
                        key = Especialista.matricula
                    elif key == "localidad":
                        key = Especialista.localidad_id
                    elif key == "especialidad":
                        key = Especialista.especialidad_id
                    elif key == "dias":
                        key = Especialista.dias
                    if direction.lower() == "asc":
                        query = query.order_by(asc(key))
                    elif direction.lower() == "desc":
                        query = query.order_by(desc(key))

            query = query.offset(skip).limit(limit)
            result = query.all()
            
            return result
    
    def can_view_details(self, request: Request) -> bool:
        return "read" in request.state.user["roles"]

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]

class DiaView(ModelView):
    search_builder = False
    fields = ["nombre"]
    
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