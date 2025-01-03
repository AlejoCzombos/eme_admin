from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

from src.models.images import Sponsor, Banner
from src.database import Session

class Sponsors(HTTPEndpoint):
    async def get(self, request):
        db_session = Session()
        try:
            Sponsors = db_session.query(Sponsor).all()
            serialized_sponsors = [sponsor.to_dict() for sponsor in Sponsors]
        finally:
            db_session.close()
        return JSONResponse(content=serialized_sponsors)

class Banners(HTTPEndpoint):
    async def get(self, request):
        db_session = Session()
        try:
            banners = db_session.query(Banner).all()
            serialized_banners = [banner.to_dict() for banner in banners]
        finally:
            db_session.close()
        return JSONResponse(content=serialized_banners)