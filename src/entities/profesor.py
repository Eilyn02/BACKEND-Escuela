"""
Modelo de base de datos para la entidad Profesor.

Representa a los profesores de la escuela y almacena
información como nombre, apellido, correo y especialidad.
"""

from sqlalchemy import Column, Integer, String
from src.database.config import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    especialidad = Column(String, nullable=False)
