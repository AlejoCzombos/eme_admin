from starlette_admin.contrib.sqla import ModelView
from starlette.requests import Request
from src.models.specialists import Dia, Especialidad, Especialista

class EspecialidadView(ModelView):
    column_list = ['nombre']
    
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

class EspecialistaView(ModelView):
    column_list = ['nombre', 'matricula', 'sucursal', 'especialidad', 'dia']
    
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

class DiaView(ModelView):
    column_list = ['nombre']
    
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