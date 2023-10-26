from . import BaseTable
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Rating(BaseTable):
    __tablename__ = "producto"
    rating = Column(Integer, nullable=False)
    contador = Column(Integer)
    
    producto = relationship('Producto', back_populates='Rating')