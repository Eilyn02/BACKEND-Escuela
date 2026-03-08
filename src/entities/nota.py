from sqlalchemy import Column, Integer, Float, ForeignKey
from src.database.config import Base


class Nota(Base):
    __tablename__ = "notas"

    id_nota = Column(Integer, primary_key=True, index=True)
    clasificacion = Column(Float, nullable=False)

    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"))
    id_profesor = Column(Integer, ForeignKey("profesores.id_profesor"))
    id_materia = Column(Integer, ForeignKey("materias.id_materia"))
    id_periodo = Column(Integer, ForeignKey("periodos.id_periodo"))
