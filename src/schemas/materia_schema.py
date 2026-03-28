from pydantic import BaseModel, Field


class MateriaBase(BaseModel):
    nombre: str=Field (...,min_length=1)
    id_profesor: int =Field (...,gt=0)


class MateriaCreate(MateriaBase):
    pass


class MateriaResponse(MateriaBase):
    id_materia: int

    class Config:
        from_attributes = True