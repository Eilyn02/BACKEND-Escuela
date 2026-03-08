from datetime import date
from pydantic import BaseModel


class PeriodoBase(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date


class PeriodoCreate(PeriodoBase):
    pass


class PeriodoResponse(PeriodoBase):
    id_periodo: int

    class Config:
        from_attributes = True