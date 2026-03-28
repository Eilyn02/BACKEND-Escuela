from pydantic import BaseModel, Field


class NotaBase(BaseModel):
    clasificacion: float =Field (...,gt=0, le=5)
    id_estudiante: int =Field (...,gt=0)
    id_profesor: int =Field (...,gt=0)
    id_materia: int =Field (...,gt=0)
    id_periodo: int =Field (...,gt=0)


class NotaCreate(NotaBase):
    pass


class NotaResponse(NotaBase):
    id_nota: int

    class Config:
        from_attributes = True