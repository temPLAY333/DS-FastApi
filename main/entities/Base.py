from . import Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase

class Base1(DeclarativeBase):
    pass
class BaseTable(Base1):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)