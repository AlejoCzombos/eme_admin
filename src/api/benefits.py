from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.database import Session
from src.models.benefits import Beneficio

class beneficios(HTTPEndpoint):
    async def get(self, request):
        db_session = Session()
        try:
            benefits = db_session.query(Beneficio).all()
            # Serializar los objetos antes de retornarlos
            serialized_benefits = [beneficio.to_dict() for beneficio in benefits]
        finally:
            db_session.close()
        return JSONResponse(content=serialized_benefits)