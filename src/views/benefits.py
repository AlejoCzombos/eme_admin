from starlette_admin.contrib.sqla import ModelView
from starlette.requests import Request
from sqlalchemy_file import ImageField
from sqlalchemy import text

from src.database import Session
from src.models.benefits import Beneficio 

class BeneficioView(ModelView):
    column_list = ['titulo', 'descripcion', 'descuento', 'imagen', 'categoria.nombre', 'localidad.nombre']
    
    # async def after_create(self, request, obj):
    #     db_session = Session()
    #     try:
    #         # Recuperar el objeto desde la base de datos
    #         image_url = obj.imagen.url
    #         if not image_url:
    #             print("Error: No se encontró la URL en la imagen")
    #             return

    #         # Limpiar la URL
    #         # cleaned_url = image_url.replace("//", "/").split("?")[0]
    #         cleaned_url = image_url.replace("//", "/")
    #         print("URL limpia:", cleaned_url)

    #         # Actualizar la URL en la base de datos
    #         query = text("""
    #             UPDATE beneficio
    #             SET imagen = JSON_SET(imagen, '$.url', :new_url)
    #             WHERE id = :beneficio_id
    #         """)

    #         db_session.execute(query, {"new_url": cleaned_url, "beneficio_id": obj.id})
    #         db_session.commit()
    #         print("URL actualizada exitosamente:", cleaned_url)

    #     except Exception as e:
    #         print("Error al modificar la URL:", str(e))
    #         db_session.rollback()
    #     finally:
    #         db_session.close()
    
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


class CategoriaBeneficioView(ModelView):
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


class LocalidadView(ModelView):
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
