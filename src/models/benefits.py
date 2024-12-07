from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_file import ImageField
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_file.validators import ImageValidator

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
                min_wh=(100, 100),
                max_wh=(800, 800),
                max_aspect_ratio=1.0
            )
        ),
        nullable=False
    )
    categoria_id = Column(Integer, ForeignKey('categoria_beneficio.id'))
    categoria = relationship('CategoriaBeneficio')
    localidad_id = Column(Integer, ForeignKey('localidad.id'))
    localidad = relationship('Localidad')
    
    def to_dict(self):
        imagen_path = getattr(self.imagen, 'path', '')
        # Procesa la ruta de la imagen
        imagen_url = imagen_path.replace('./static\\', '').replace('\\', '/').replace('default/', '')
        
        return {
            "id": self.id,
            "title": self.titulo,
            "description": self.descripcion,
            "discount": self.descuento,
            "category": self.categoria.nombre,
            "locality": self.localidad_id,
            "imagen_url": f"/api/images/{imagen_url}"
        }


class CategoriaBeneficio(Base):
    __tablename__ = 'categoria_beneficio'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    
    def get_name(self):
        return self.nombre


class Localidad(Base):
    __tablename__ = 'localidad'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    
    def get_name(self):
        return self.nombre