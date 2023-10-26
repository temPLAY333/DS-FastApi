from . import BaseTable
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Producto(BaseTable):
    __tablename__ = "producto"
    titulo = Column(String, nullable=False)
    precio_compra = Column(Integer, nullable=False)
    description = Column(String)
    categoria = Column(String)
    url_imagen = Column(String)
    
    rating = relationship('Rating', back_populates='Producto')
    