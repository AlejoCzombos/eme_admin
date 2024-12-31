from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.models.benefits import Base

from sqlalchemy_file import ImageField
from sqlalchemy_file.validators import ImageValidator

class Banner(Base):
    __tablename__ = 'Banner'
    
    id = Column(Integer, primary_key=True)
    imagen = Column(
        ImageField(
            image_validator=ImageValidator(
                allowed_content_types=["image/jpeg", "image/png"],
                min_wh=(100, 100),
                max_wh=(800, 800),
                max_aspect_ratio=1.0
            ),
            upload_storage="default"
        ),
        nullable=False
    )

class Sponsor(Base):
    __tablename__ = 'Sponsor'
    
    id = Column(Integer, primary_key=True)
    logo = Column(
        ImageField(
            image_validator=ImageValidator(
                allowed_content_types=["image/jpeg", "image/png"],
                min_wh=(100, 100),
                max_wh=(800, 800),
                max_aspect_ratio=1.0
            ),
            upload_storage="default"
        ),
        nullable=False
    )