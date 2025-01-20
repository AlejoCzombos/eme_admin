from src.models.benefits import Localidad
from src.models.specialists import Dia
from src.database import db_session
from sqlalchemy.exc import SQLAlchemyError

def create_days():
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


def create_branches():
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
    try:
        create_days()
        create_branches()
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
