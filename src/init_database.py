import os
from passlib.hash import bcrypt
from src.models.user import User
from src.config import ADMIN_PASSWORD
from src.models.benefits import Localidad # Asegúrate de tener un modelo para sucursales
from src.models.specialists import Dia # Asegúrate de tener un modelo para días
from src.database import db_session
from sqlalchemy.exc import SQLAlchemyError


def create_days():
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
    branches = [
        "Resistencia",
        "Corrientes",
        "Sáenz Peña"
    ]
    for branch in branches:
        db_session.add(Localidad(nombre=branch))
    print("Sucursales añadidas correctamente.")


def create_user():
    password = ADMIN_PASSWORD
    if not password:
        raise ValueError("Variable de entorno 'ADMIN_PASSWORD' no encontrada.")

    new_user = User(
        username="admin",
        password_hash=bcrypt.hash(password),
        name="Administrator",
        roles="read,create,edit,delete,admin,action_make_published",
    )
    db_session.add(new_user)
    print("Usuario añadido correctamente.")


def main():
    try:
        create_days()
        create_branches()
        create_user()
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
