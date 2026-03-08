from sqlalchemy import Column, Integer, String, Date
from src.database.config import Base


class Periodo(Base):
    __tablename__ = "periodos"

    id_periodo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
