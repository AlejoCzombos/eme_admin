from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD

from src.models.benefits import Base


DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


db_session = SessionLocal()