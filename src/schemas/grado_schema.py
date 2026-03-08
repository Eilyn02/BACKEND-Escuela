from pydantic import BaseModel


class GradoBase(BaseModel):
    nombre: str


class GradoCreate(GradoBase):
    pass


class GradoResponse(GradoBase):
    id_grado: int

    class Config:
        from_attributes = True