from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.config import get_db
from src.entities.grado import Grado
from src.schemas.grado_schema import GradoCreate, GradoResponse

router = APIRouter(prefix="/grados", tags=["Grados"])


@router.get("/", response_model=list[GradoResponse])
def obtener_grados(db: Session = Depends(get_db)):
    return db.query(Grado).all()


@router.get("/{id_grado}", response_model=GradoResponse)
def obtener_grado(id_grado: int, db: Session = Depends(get_db)):
    grado = db.query(Grado).filter(Grado.id_grado == id_grado).first()
    if not grado:
        raise NotFoundError("Grado no encontrado")
    return grado


@router.post("/", response_model=GradoResponse)
def crear_grado(grado: GradoCreate, db: Session = Depends(get_db)):
    nuevo_grado = Grado(**grado.model_dump())
    db.add(nuevo_grado)
    db.commit()
    db.refresh(nuevo_grado)
    return nuevo_grado


@router.put("/{id_grado}", response_model=GradoResponse)
def actualizar_grado(id_grado: int, grado: GradoCreate, db: Session = Depends(get_db)):
    grado_db = db.query(Grado).filter(Grado.id_grado == id_grado).first()
    if not grado_db:
        raise NotFoundError("Grado no encontrado")

    for key, value in grado.model_dump().items():
        setattr(grado_db, key, value)

    db.commit()
    db.refresh(grado_db)
    return grado_db


@router.delete("/{id_grado}")
def eliminar_grado(id_grado: int, db: Session = Depends(get_db)):
    grado_db = db.query(Grado).filter(Grado.id_grado == id_grado).first()
    if not grado_db:
        raise NotFoundError("Grado no encontrado")

    db.delete(grado_db)
    db.commit()
    return {"message": "Grado eliminado correctamente"}