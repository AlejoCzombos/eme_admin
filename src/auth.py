from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AuthProvider, AdminConfig, AdminUser
from starlette_admin.exceptions import FormValidationError, LoginFailed
from sqlalchemy.orm import Session
from src.models.user import User 

class MyAuthProvider(AuthProvider):
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.allow_paths = ["/login", "/statics/*", "/static/*"]
        self.allow_routes = ["/login", "/statics/*", "/static/*"]
        self.login_path = "/login"
        self.logout_path = "/logout"

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        if len(username) < 3:
            raise FormValidationError(
                {"username": "Ensure username has at least 3 characters"}
            )

        user = self.db_session.query(User).filter_by(username=username).first()
        if user and user.verify_password(password):
            request.session.update({"username": username})
            return response

        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        username = request.session.get("username", None)
        if username:
            user = self.db_session.query(User).filter_by(username=username).first()
            if user:
                request.state.user = {
                    "id": user.id,
                    "username": user.username,
                    "roles": user.roles.split(","),
                    "sucursal_id": user.branch_id,
                }
                return True
        return False
    
    def get_admin_config(self, request: Request) -> AdminConfig:
        return AdminConfig(
            app_title="EME admin",
            logo_url="/admin/statics/logo.png",
        )

    def get_admin_user(self, request: Request) -> AdminUser:
        return AdminUser(username="admin", photo_url="")

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response