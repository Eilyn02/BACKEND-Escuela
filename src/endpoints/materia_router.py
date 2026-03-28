from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.config import get_db
from src.entities.materia import Materia
from src.schemas.materia_schema import MateriaCreate, MateriaResponse

router = APIRouter(prefix="/materias", tags=["Materias"])


@router.get("/", response_model=list[MateriaResponse])
def obtener_materias(db: Session = Depends(get_db)):
    return db.query(Materia).all()


@router.get("/{id_materia}", response_model=MateriaResponse)
def obtener_materia(id_materia: int, db: Session = Depends(get_db)):
    materia = db.query(Materia).filter(Materia.id_materia == id_materia).first()
    if not materia:
        raise NotFoundError("Materia no encontrada")
    return materia


@router.post("/", response_model=MateriaResponse)
def crear_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    nueva_materia = Materia(**materia.model_dump())
    db.add(nueva_materia)
    db.commit()
    db.refresh(nueva_materia)
    return nueva_materia


@router.put("/{id_materia}", response_model=MateriaResponse)
def actualizar_materia(id_materia: int, materia: MateriaCreate, db: Session = Depends(get_db)):
    materia_db = db.query(Materia).filter(Materia.id_materia == id_materia).first()
    if not materia_db:
        raise NotFoundError("Materia no encontrada")

    for key, value in materia.model_dump().items():
        setattr(materia_db, key, value)

    db.commit()
    db.refresh(materia_db)
    return materia_db


@router.delete("/{id_materia}")
def eliminar_materia(id_materia: int, db: Session = Depends(get_db)):
    materia_db = db.query(Materia).filter(Materia.id_materia == id_materia).first()
    if not materia_db:
        raise NotFoundError("Materia no encontrada")

    db.delete(materia_db)
    db.commit()
    return {"message": "Materia eliminada correctamente"}