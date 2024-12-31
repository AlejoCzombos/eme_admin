from starlette_admin.contrib.sqla import ModelView
from starlette.requests import Request

from src.database import Session
from src.models.administrator import Token, AdministradorActual

# Define tu vista personalizada
class AdministradorActualView(ModelView):
    async def before_create(self, request, data, obj):
        db_session = Session()
        try:
            existing_admin = db_session.query(AdministradorActual).first()
            if existing_admin:
                raise ValueError("Ya existe un administrador actual. Elimínalo antes de agregar otro.")
        finally:
            db_session.close()
        
    async def before_edit(self, request, data, obj):
        db_session = Session()
        try:
            existing_admin = db_session.query(AdministradorActual).first()
            if existing_admin:
                raise ValueError("Ya existe un administrador actual. Elimínalo antes de agregar otro.")
        finally:
            db_session.close()

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
    
    async def before_create(self, request, data, obj):
        db_session = Session()
        try:
            existing_token = db_session.query(Token).first()
            if existing_token:
                raise ValueError("Ya existe un token. Elimínalo antes de agregar otro.")
        finally:
            db_session.close()
        
    async def before_edit(self, request, data, obj):
        db_session = Session()
        try:
            existing_token = db_session.query(Token).first()
            if existing_token:
                raise ValueError("Ya existe un token. Elimínalo antes de agregar otro.")
        finally:
            db_session.close()
    
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