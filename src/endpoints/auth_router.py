from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.core.security import create_access_token, get_current_user, verify_password
from src.database.config import get_db
from src.entities.usuario import Usuario
from src.schemas.auth_schema import LoginRequest, TokenResponse
from src.schemas.usuario_schema import UsuarioResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == data.correo).first()

    if not usuario:
        raise NotFoundError("Credenciales inválidas")

    if not verify_password(data.password, usuario.password_hash):
        raise NotFoundError("Credenciales inválidas")

    access_token = create_access_token({"sub": usuario.correo})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UsuarioResponse)
def obtener_usuario_actual(usuario: Usuario = Depends(get_current_user)):
    return usuario
