from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from passlib.hash import bcrypt
from src.models.benefits import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(150), nullable=False)
    roles = Column(String(255), nullable=False)
    branch_id = Column(Integer, nullable=True)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.password_hash)
