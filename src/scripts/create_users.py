from passlib.hash import bcrypt
from src.models.user import User
from src.config import RCIA_ADMIN_NAME, RCIA_ADMIN_PASSWORD, CTES_ADMIN_NAME, CTES_ADMIN_PASSWORD, RSP_ADMIN_NAME, RSP_ADMIN_PASSWORD, SUPER_ADMIN_NAME, SUPER_ADMIN_PASSWORD
from src.database import get_db
from sqlalchemy.exc import SQLAlchemyError

def create_users():
    with get_db() as db_session:
        if db_session.query(User).count() > 0:
            print("Usuarios ya existe en la base de datos.")
            return
    
        create_user(SUPER_ADMIN_NAME, SUPER_ADMIN_PASSWORD, "Super Admin")
        create_user(RCIA_ADMIN_NAME, RCIA_ADMIN_PASSWORD, "Admin Resistencia", 1)
        create_user(CTES_ADMIN_NAME, CTES_ADMIN_PASSWORD, "Admin Corrientes", 2)
        create_user(RSP_ADMIN_NAME, RSP_ADMIN_PASSWORD, "Admin Saenz Peña", 3)

def create_user(username, password, name, branch_id = None):
    if not password:
        raise ValueError("Variable de entorno 'ADMIN_PASSWORD' no encontrada.")
    if not username:
        raise ValueError("Variable de entorno 'ADMIN_NAME' no encontrada.")

    new_user = User(
        username=username,
        password_hash=bcrypt.hash(password),
        name=name,
        branch_id=branch_id,
        roles="read,create,edit,delete,branch_admin",
    )
    with get_db() as db_session:
        db_session.add(new_user)
        print(f"Usuario {name} añadido correctamente.")

def main():
    with get_db() as db_session:
        try:
            create_users()
            db_session.commit()
            print("Proceso completado.")
        except SQLAlchemyError as e:
            db_session.rollback()
            print(f"Error de la base de datos: {e}")
        except Exception as e:
            db_session.rollback()
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
