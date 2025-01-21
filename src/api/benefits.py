from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.database import get_db
from src.models.benefits import Beneficio, BeneficiosHome

class beneficios(HTTPEndpoint):
    async def get(self, request):
        with get_db() as db_session:
            benefits = db_session.query(Beneficio).all()
            # Serializar los objetos antes de retornarlos
            serialized_benefits = [beneficio.to_dict() for beneficio in benefits]
            return JSONResponse(content=serialized_benefits)

class beneficiosHome(HTTPEndpoint):
    async def get(self, request):
        with get_db() as db_session:
            benefits_home = db_session.query(BeneficiosHome).all()
            # Serializar los objetos antes de retornarlos
            serialized_benefits_home = [beneficio.to_dict() for beneficio in benefits_home]
            return JSONResponse(content=serialized_benefits_home)