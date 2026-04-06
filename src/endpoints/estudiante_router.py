from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError, ConflictError
from src.database.config import get_db
from src.entities.estudiante import Estudiante
from src.schemas.estudiante_schema import EstudianteCreate, EstudianteResponse
from src.core.security import get_current_user
from src.entities.usuario import Usuario

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


@router.get("/", response_model=list[EstudianteResponse])
def obtener_estudiantes(db: Session = Depends(get_db)):
    return db.query(Estudiante).all()


@router.get("/{id_estudiante}", response_model=EstudianteResponse)
def obtener_estudiante(id_estudiante: int, db: Session = Depends(get_db)):
    estudiante = (
        db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()
    )
    if not estudiante:
        raise NotFoundError("Estudiante no encontrado")
    return estudiante


@router.post("/", response_model=EstudianteResponse)
def crear_estudiante(
    estudiante: EstudianteCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    existe_correo = (
        db.query(Estudiante).filter(Estudiante.correo == estudiante.correo).first()
    )
    if existe_correo:
        raise ConflictError("Ya existe un estudiante con ese correo")

    nuevo_estudiante = Estudiante(**estudiante.model_dump())

    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return nuevo_estudiante


@router.put("/{id_estudiante}", response_model=EstudianteResponse)
def actualizar_estudiante(
    id_estudiante: int,
    estudiante: EstudianteCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    estudiante_db = (
        db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()
    )
    if not estudiante_db:
        raise NotFoundError("Estudiante no encontrado")

    for key, value in estudiante.model_dump().items():
        setattr(estudiante_db, key, value)

    db.commit()
    db.refresh(estudiante_db)
    return estudiante_db


@router.delete("/{id_estudiante}")
def eliminar_estudiante(
    id_estudiante: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user),
):
    estudiante_db = (
        db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()
    )
    if not estudiante_db:
        raise NotFoundError("Estudiante no encontrado")

    db.delete(estudiante_db)
    db.commit()
    return {"message": "Estudiante eliminado correctamente"}
