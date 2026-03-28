from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError, ConflictError
from src.database.config import get_db
from src.entities.profesor import Profesor
from src.schemas.profesor_schema import ProfesorCreate, ProfesorResponse

router = APIRouter(prefix="/profesores", tags=["Profesores"])


@router.get("/", response_model=list[ProfesorResponse])
def obtener_profesores(db: Session = Depends(get_db)):
    return db.query(Profesor).all()


@router.get("/{id_profesor}", response_model=ProfesorResponse)
def obtener_profesor(id_profesor: int, db: Session = Depends(get_db)):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if not profesor:
        raise NotFoundError("Profesor no encontrado")
    return profesor


@router.post("/", response_model=ProfesorResponse)
def crear_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db)):
    existe_correo = db.query(Profesor).filter(Profesor.correo == profesor.correo).first()
    if existe_correo:
        raise ConflictError("Ya existe un profesor con ese correo")

    nuevo_profesor = Profesor(**profesor.model_dump())
    db.add(nuevo_profesor)
    db.commit()
    db.refresh(nuevo_profesor)
    return nuevo_profesor


@router.put("/{id_profesor}", response_model=ProfesorResponse)
def actualizar_profesor(id_profesor: int, profesor: ProfesorCreate, db: Session = Depends(get_db)):
    profesor_db = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if not profesor_db:
        raise NotFoundError("Profesor no encontrado")

    for key, value in profesor.model_dump().items():
        setattr(profesor_db, key, value)

    db.commit()
    db.refresh(profesor_db)
    return profesor_db


@router.delete("/{id_profesor}")
def eliminar_profesor(id_profesor: int, db: Session = Depends(get_db)):
    profesor_db = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if not profesor_db:
        raise NotFoundError("Profesor no encontrado")

    db.delete(profesor_db)
    db.commit()
    return {"message": "Profesor eliminado correctamente"}