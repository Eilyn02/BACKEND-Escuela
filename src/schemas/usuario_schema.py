from pydantic import BaseModel, EmailStr, Field


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    correo: EmailStr
    rol: str = Field(..., min_length=1)
    activo: bool


class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True
