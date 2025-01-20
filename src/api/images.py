from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.models.images import Sponsor, Banner
from src.database import get_db

class Sponsors(HTTPEndpoint):
    async def get(self, request):
        with get_db() as db_session:
            Sponsors = db_session.query(Sponsor).all()
            serialized_sponsors = [sponsor.to_dict() for sponsor in Sponsors]
            return JSONResponse(content=serialized_sponsors)

class Banners(HTTPEndpoint):
    async def get(self, request):
        with get_db() as db_session:
            banners = db_session.query(Banner).all()
            serialized_banners = [banner.to_dict() for banner in banners]
            return JSONResponse(content=serialized_banners)