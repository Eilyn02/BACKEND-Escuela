from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.config import Base


class Materia(Base):
    __tablename__ = "materias"

    id_materia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    id_profesor = Column(Integer, ForeignKey("profesores.id_profesor"))
