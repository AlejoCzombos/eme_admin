import httpx
from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from src.database import get_db
from src.models.administrator import Token, AdministradorActualCorrientes, AdministradorActualResistencia, FormError

CRM_ENDPOINT = "https://api.clientify.net/v1/contacts/"

class FormularioEndpoint(HTTPEndpoint):
    async def post(self, request):
        data = await request.json()
        
        with get_db() as db_session:
            admin_actual = None
            if data.get("branch") == "Corrientes":
                admin_actual = db_session.query(AdministradorActualCorrientes).first()
            elif data.get("branch") == "Resistencia" or data.get("branch") == "Sáenz Peña":
                admin_actual = db_session.query(AdministradorActualResistencia).first()
            else:
                new_error = FormError(
                    tipo_de_error="Sucursal no encontrada.",
                    mensaje_error=f"La sucursal {data.get('branch')} no fue encontrada.",
                )
                db_session.add(new_error)
                db_session.commit()
                return JSONResponse({"error": "Sucursal no encontrada."}, status_code=400)
            
            if not admin_actual:
                new_error = FormError(
                    tipo_de_error="No hay administrador.",
                    mensaje_error=f"No hay administrador actual configurado para la sucursal {data.get('branch')}.",
                )
                db_session.add(new_error)
                db_session.commit()
                return JSONResponse({"error": "No hay administrador actual configurado."}, status_code=400)
            
            token_actual = db_session.query(Token).first()
            
            if not token_actual:
                new_error = FormError(
                    tipo_de_error="No hay token",
                    mensaje_error="No hay token configurado para enviar datos al CRM.",
                )
                db_session.add(new_error)
                db_session.commit()
                return JSONResponse({"error": "No hay token configurado."}, status_code=400)

            # Completar datos
            post_data = {
                "owner_id": admin_actual.administrador_id,
                "owner": admin_actual.administrador.correo,
                "owner_name": admin_actual.administrador.nombre,
                "first_name": data.get("first_name"),
                "last_name": data.get("last_name"),
                "email": data.get("email"),
                "phone": data.get("phone"),
                "tags": ["pagina_web", data.get("branch") ,*data.get("services", [])],
                "contact_type": data.get("contact_type"),
                "contact_source": "Pagina web",
                "addresses": [
                    {
                        "street": "",
                        "city": data.get("branch"),
                        "state": "Provincia",
                        "country": "Argentina",
                        "postal_code": "",
                        "type": 1,
                    }
                ],
                "custom_fields": [
                    {"field": "CUIT", "value": data.get("cuit")},
                ],
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    CRM_ENDPOINT,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Token {token_actual.token}",
                    },
                    json=post_data,
                )

            if response.status_code == 201:
                return JSONResponse({"message": "Datos enviados exitosamente."}, status_code=201)
            else:
                new_error = FormError(
                    tipo_de_error="Error al enviar datos al CRM.",
                    mensaje_error=response.text + f" ({response.status_code})",
                )
                db_session.add(new_error)
                db_session.commit()
                return JSONResponse(
                    {
                        "error": "Error al enviar los datos al CRM.",
                        "details": response.text,
                    },
                    status_code=response.status_code,
                )
            
            Response = JSONResponse({"message": "Datos enviados exitosamente."}, status_code=201)
