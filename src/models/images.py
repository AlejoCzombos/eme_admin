from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.benefits import Base

from sqlalchemy_file import ImageField
from sqlalchemy_file.validators import ImageValidator

from src.utils import remove_query_params

class Banner(Base):
    __tablename__ = 'Banner'
    
    id = Column(Integer, primary_key=True)
    imagen = Column(
        ImageField(
            image_validator=ImageValidator(
                allowed_content_types=["image/jpeg", "image/png", "image/webp"],
                min_wh=(1720, 480),
                max_wh=(1730, 550),
            ),
            upload_storage="default"
        ),
        nullable=False
    )
    titulo = Column(String(25), nullable=True)
    descripcion = Column(String(230), nullable=True)
    boton_texto = Column(String(25), nullable=True)
    boton_url = Column(String(200), nullable=True)
    
    def to_dict(self):
        imagen_url = getattr(self.imagen, 'url', '')
        
        return {
            "id": self.id,
            "url": remove_query_params(imagen_url),
            "title": self.titulo,
            "description": self.descripcion,
            "button_text": self.boton_texto,
            "button_url": self.boton_url
        }