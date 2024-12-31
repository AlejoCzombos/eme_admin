from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.models.benefits import Base

class Administrador(Base):
    __tablename__ = 'administrador'
    
    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, nullable=False)
    correo = Column(String(150), nullable=False)
    nombre = Column(String(100), nullable=False)

class AdministradorActual(Base):
    __tablename__ = 'administrador_actual'
    
    id = Column(Integer, primary_key=True)
    administrador_id = Column(Integer, ForeignKey('administrador.id'), nullable=False, unique=True)
    administrador = relationship('Administrador')

class Token(Base):
    __tablename__ = 'token'
    
    id = Column(Integer, primary_key=True)
    token = Column(String(250), nullable=False)