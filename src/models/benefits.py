from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_file import ImageField, FileField
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_file.validators import ImageValidator
from starlette_admin.contrib.sqla import ModelView

Base = declarative_base()

class Beneficio(Base):
    __tablename__ = 'beneficio'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    descuento = Column(Integer, nullable=False)
    imagen = Column(
        ImageField(
            image_validator=ImageValidator(
                allowed_content_types=["image/jpeg", "image/png"],
                min_wh=(200, 200),
                max_wh=(600, 600),
                max_aspect_ratio=1.0
            )
        ),
        nullable=False
    )
    categoria_id = Column(Integer, ForeignKey('categoria_beneficio.id'))
    categoria = relationship('CategoriaBeneficio')
    localidad_id = Column(Integer, ForeignKey('localidad.id'))
    localidad = relationship('Localidad')


class CategoriaBeneficio(Base):
    __tablename__ = 'categoria_beneficio'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


class Localidad(Base):
    __tablename__ = 'localidad'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


class BeneficioView(ModelView):
    column_list = ['titulo', 'descripcion', 'descuento', 'imagen', 'categoria.nombre', 'localidad.nombre']
    


class CategoriaBeneficioView(ModelView):
    column_list = ['nombre']


class LocalidadView(ModelView):
    column_list = ['nombre']
