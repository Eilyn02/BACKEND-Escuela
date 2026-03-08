from sqlalchemy import Column, Integer, String
from src.database.config import Base


class Grado(Base):
    __tablename__ = "grados"

    id_grado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
