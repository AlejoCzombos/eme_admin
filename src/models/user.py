from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from passlib.hash import bcrypt
from src.models.benefits import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    roles = Column(String, nullable=False)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)
