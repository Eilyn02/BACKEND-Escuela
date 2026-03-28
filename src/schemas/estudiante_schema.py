from pydantic import BaseModel, EmailStr, Field


class EstudianteBase(BaseModel):
    nombre: str =Field (...,min_length=1)
    apellido: str =Field (...,min_length=1)
    correo: EmailStr
    id_grado: int =Field (...,gt=0)


class EstudianteCreate(EstudianteBase):
    pass


class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        from_attributes = True