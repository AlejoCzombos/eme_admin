from src.models.benefits import Localidad
from src.models.specialists import Dia
from src.database import get_db
from sqlalchemy.exc import SQLAlchemyError

def create_days(db_session):
    if db_session.query(Dia).count() > 0:
        print("Dias ya existen en la base de datos.")
        return
    
    days = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo",
    ]
    for day in days:
        db_session.add(Dia(nombre=day))
    print("Dias añadidos correctamente.")


def create_branches(db_session):
    if db_session.query(Localidad).count() > 0:
        print("Sucursales ya existen en la base de datos.")
        return
    
    branches = [
        "Resistencia",
        "Corrientes",
        "Sáenz Peña"
    ]
    for branch in branches:
        db_session.add(Localidad(nombre=branch))
    print("Sucursales añadidas correctamente.")


def main():
    with get_db() as db_session:
        try:
            create_days(db_session)
            create_branches(db_session)
            db_session.commit()
            print("Proceso completado con exito init db.")
        except SQLAlchemyError as e:
            db_session.rollback()
            print(f"Error de la base de datos: {e}")
        except Exception as e:
            db_session.rollback()
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
