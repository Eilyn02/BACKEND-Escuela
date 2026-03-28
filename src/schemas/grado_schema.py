from pydantic import BaseModel, Field


class GradoBase(BaseModel):
    nombre: str=Field (...,min_length=1)


class GradoCreate(GradoBase):
    pass


class GradoResponse(GradoBase):
    id_grado: int

    class Config:
        from_attributes = True