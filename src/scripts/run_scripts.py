from src.scripts.create_users import create_users
from src.scripts.init_database import create_days, create_branches

from src.database import get_db
from sqlalchemy.exc import SQLAlchemyError

def init():
    with get_db() as db_session:
        try:
            create_days(db_session)
            create_branches(db_session)
            create_users(db_session)
            db_session.commit()
            print("Proceso completado con exito scripts.")
        except SQLAlchemyError as e:
            db_session.rollback()
            print(f"Error de la base de datos: {e}")
        except Exception as e:
            db_session.rollback()
            print(f"Error: {e}")

if __name__ == "__main__":
    init()