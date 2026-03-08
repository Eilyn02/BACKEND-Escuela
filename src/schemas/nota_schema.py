from pydantic import BaseModel


class NotaBase(BaseModel):
    clasificacion: float
    id_estudiante: int
    id_profesor: int
    id_materia: int
    id_periodo: int


class NotaCreate(NotaBase):
    pass


class NotaResponse(NotaBase):
    id_nota: int

    class Config:
        from_attributes = True