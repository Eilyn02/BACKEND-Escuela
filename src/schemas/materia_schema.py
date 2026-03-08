from pydantic import BaseModel


class MateriaBase(BaseModel):
    nombre: str
    id_profesor: int


class MateriaCreate(MateriaBase):
    pass


class MateriaResponse(MateriaBase):
    id_materia: int

    class Config:
        from_attributes = True