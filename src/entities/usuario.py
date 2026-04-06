from sqlalchemy import Boolean, Column, Integer, String

from src.database.config import Base


class Usuario(Base):
    """
    Modelo de base de datos para los usuarios del sistema.
    """

    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    rol = Column(String, nullable=False, default="admin")
    activo = Column(Boolean, default=True)
