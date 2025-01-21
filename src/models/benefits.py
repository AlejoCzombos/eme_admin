from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_file import ImageField
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_file.validators import ImageValidator

from src.utils import remove_query_params

Base = declarative_base()

class Beneficio(Base):
    __tablename__ = 'beneficio'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    descuento = Column(Integer, nullable=False)
    texto_descuento = Column(String(255))
    imagen = Column(
        ImageField(
            image_validator=ImageValidator(
                allowed_content_types=["image/jpeg", "image/png", "image/webp"],
                min_wh=(100, 100),
                max_wh=(800, 800),
                min_aspect_ratio=1.0,
                max_aspect_ratio=1.0
            ),
            upload_storage="default"
        ),
        nullable=False
    )
    categoria_id = Column(Integer, ForeignKey('categoria_beneficio.id'))
    categoria = relationship('CategoriaBeneficio')
    localidad_id = Column(Integer, ForeignKey('localidad.id'))
    localidad = relationship('Localidad')
    
    def to_dict(self):
        imagen_url = getattr(self.imagen, 'url', '')
        
        return {
            "id": self.id,
            "title": self.titulo,
            "description": self.descripcion,
            "discount": self.descuento,
            "text_discount": self.texto_descuento,
            "category": self.categoria.nombre,
            "locality": self.localidad_id,
            "imagen_url": remove_query_params(imagen_url),
        }
    
    async def __admin_repr__(self, request):
        return f"{self.titulo} {self.descuento}%"


class CategoriaBeneficio(Base):
    __tablename__ = 'categoria_beneficio'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    
    def get_name(self):
        return self.nombre

    async def __admin_repr__(self, request):
        return f"{self.nombre}"


class BeneficiosHome(Base):
    __tablename__ = 'beneficios_home'

    id = Column(Integer, primary_key=True)
    beneficio_id = Column(Integer, ForeignKey('beneficio.id'))
    beneficio = relationship('Beneficio')
    
    def to_dict(self):
        return {
            "id": self.id,
            "url": remove_query_params(self.beneficio.imagen.url),
        }


class Localidad(Base):
    __tablename__ = 'localidad'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    
    def get_name(self):
        return self.nombre

    async def __admin_repr__(self, request):
        return f"{self.nombre}"