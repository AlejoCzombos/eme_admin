from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse
from starlette.endpoints import HTTPEndpoint

from src.database import db_session
from src.storage import StorageManager, LocalStorageDriver
from src.models.benefits import Beneficio

class beneficios(HTTPEndpoint):
    async def get(self, request):
        benefits = db_session.query(Beneficio).all()
        # Serializar los objetos antes de retornarlos
        serialized_benefits = [beneficio.to_dict() for beneficio in benefits]
        return JSONResponse(content=serialized_benefits)

class Imagenes(HTTPEndpoint):
    async def get(self, request):
        file_id = request.path_params['file_id']
        
        file = StorageManager.get_file(f"default/{file_id}")
        if isinstance(file.object.driver, LocalStorageDriver):
            return FileResponse(
                file.get_cdn_url(), media_type=file.content_type, filename=file.filename
            )
        
        return JSONResponse(content={"error": "File not found"}, status_code=404)