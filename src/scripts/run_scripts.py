from src.scripts.create_users import create_users
from src.scripts.init_database import create_days, create_branches

from src.database import db_session
from sqlalchemy.exc import SQLAlchemyError

def init():
    try:
        create_days()
        create_branches()
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