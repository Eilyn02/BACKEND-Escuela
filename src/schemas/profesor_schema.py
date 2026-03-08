from pydantic import BaseModel


class ProfesorBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    especialidad: str


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorResponse(ProfesorBase):
    id_profesor: int

    class Config:
        orm_mode = True