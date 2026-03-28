from pydantic import BaseModel, EmailStr, Field


class ProfesorBase(BaseModel):
    nombre: str = Field (...,min_length=1)
    apellido: str  = Field (...,min_length=1)
    correo: EmailStr
    especialidad: str = Field (...,min_length=1)
    telefono: str | None = None


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorResponse(ProfesorBase):
    id_profesor: int

    class Config:
        orm_mode = True
