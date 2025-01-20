from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.models.benefits import Base, Localidad

especialista_dia = Table(
    'especialista_dia', Base.metadata,
    Column('especialista_id', Integer, ForeignKey('especialista.id'), primary_key=True),
    Column('dia_id', Integer, ForeignKey('dia.id'), primary_key=True)
)

class Especialista(Base):
    __tablename__ = 'especialista'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    matricula = Column(Integer, nullable=False)
    localidad_id = Column(Integer, ForeignKey('localidad.id'))
    localidad = relationship('Localidad')
    especialidad = relationship('Especialidad')
    especialidad_id = Column(Integer, ForeignKey('especialidad.id'))
    dias = relationship('Dia', secondary=especialista_dia, backref='especialistas')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.nombre,
            'license': self.matricula,
            'locality': self.localidad.nombre,
            'specialty': self.especialidad.nombre,
            'days': [dia.nombre for dia in self.dias]
        }
    
    async def __admin_repr__(self, request):
        return f"{self.nombre}"

class Especialidad(Base):
    __tablename__ = 'especialidad'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    
    async def __admin_repr__(self, request):
        return f"{self.nombre}"

class Dia(Base):
    __tablename__ = 'dia'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    
    async def __admin_repr__(self, request):
        return f"{self.nombre}"