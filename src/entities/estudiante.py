"""
Modelo de base de datos para la entidad Estudiante.

Cada estudiante pertenece a un grado dentro del sistema.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from src.database.config import Base


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    id_grado = Column(Integer, ForeignKey("grados.id_grado"))
