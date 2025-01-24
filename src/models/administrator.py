from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from src.models.benefits import Base

class Administrador(Base):
    __tablename__ = 'administrador'
    
    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, nullable=False)
    correo = Column(String(150), nullable=False)
    nombre = Column(String(100), nullable=False)
    
    async def __admin_repr__(self, request):
        return f"{self.nombre} ({self.correo})"

class AdministradorActualResistencia(Base):
    __tablename__ = 'administrador_actual_resistencia'
    
    id = Column(Integer, primary_key=True)
    administrador_id = Column(Integer, ForeignKey('administrador.id'), nullable=False, unique=True)
    administrador = relationship('Administrador')


class AdministradorActualCorrientes(Base):
    __tablename__ = 'administrador_actual_corrientes'
    
    id = Column(Integer, primary_key=True)
    administrador_id = Column(Integer, ForeignKey('administrador.id'), nullable=False, unique=True)
    administrador = relationship('Administrador')

class AdministradorActualSaenzPeña(Base):
    __tablename__ = 'administrador_actual_saenz_pena'
    
    id = Column(Integer, primary_key=True)
    administrador_id = Column(Integer, ForeignKey('administrador.id'), nullable=False, unique=True)
    administrador = relationship('Administrador')

class Token(Base):
    __tablename__ = 'token'
    
    id = Column(Integer, primary_key=True)
    token = Column(String(250), nullable=False)
    
    async def __admin_repr__(self, request):
        return f"{self.token}"

class FormError(Base):
    __tablename__ = 'form_errors'
    
    id = Column(Integer, primary_key=True)
    tipo_de_error = Column(String(250), nullable=False)
    mensaje_error = Column(String(250), nullable=False)
    fecha_hora = Column(DateTime(timezone=True), server_default=func.now())