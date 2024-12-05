from starlette_admin.contrib.sqla import ModelView
from starlette.requests import Request

class BeneficioView(ModelView):
    column_list = ['titulo', 'descripcion', 'descuento', 'imagen', 'categoria.nombre', 'localidad.nombre']
    
    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]

    def can_view_details(self, request: Request) -> bool:
        # return "read" in request.state.user["roles"]
        return True

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]


class CategoriaBeneficioView(ModelView):
    column_list = ['nombre']
    
    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]
    
    def can_view_details(self, request: Request) -> bool:
        # return "read" in request.state.user["roles"]
        return True

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]


class LocalidadView(ModelView):
    column_list = ['nombre']
    
    def is_accessible(self, request: Request) -> bool:
        return "admin" in request.state.user["roles"]
    
    # return "read" in request.state.user["roles"]
        return True

    def can_create(self, request: Request) -> bool:
        return "create" in request.state.user["roles"]

    def can_edit(self, request: Request) -> bool:
        return "edit" in request.state.user["roles"]

    def can_delete(self, request: Request) -> bool:
        return "delete" in request.state.user["roles"]
