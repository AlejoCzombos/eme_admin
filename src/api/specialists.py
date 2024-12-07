from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse
from starlette.endpoints import HTTPEndpoint

from src.database import db_session
from src.storage import StorageManager
from src.models.specialists import Especialista

class Especialistas(HTTPEndpoint):

    async def get(self, request):
        specialists = db_session.query(Especialista).all()
        serialized_specialists = [specialist.to_dict() for specialist in specialists]
        return JSONResponse(content=serialized_specialists)