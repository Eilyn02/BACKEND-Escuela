from pydantic import BaseModel


class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    id_grado: int


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        from_attributes = True