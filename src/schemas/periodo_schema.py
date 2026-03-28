from datetime import date
from pydantic import BaseModel, Field


class PeriodoBase(BaseModel):
    nombre: str =Field (...,min_length=1)
    fecha_inicio: date 
    fecha_fin: date


class PeriodoCreate(PeriodoBase):
    pass


class PeriodoResponse(PeriodoBase):
    id_periodo: int

    class Config:
        from_attributes = True