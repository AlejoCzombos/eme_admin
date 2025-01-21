from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.models.images import Banner
from src.database import get_db

class Banners(HTTPEndpoint):
    async def get(self, request):
        with get_db() as db_session:
            banners = db_session.query(Banner).all()
            serialized_banners = [banner.to_dict() for banner in banners]
            return JSONResponse(content=serialized_banners)