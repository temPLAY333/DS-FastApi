from . import Base
from sqlalchemy import Column, Integer

class BaseTable(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  