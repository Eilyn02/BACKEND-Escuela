from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.exceptions import NotFoundError
from src.database.config import get_db
from src.entities.nota import Nota
from src.schemas.nota_schema import NotaCreate, NotaResponse

router = APIRouter(prefix="/notas", tags=["Notas"])


@router.get("/", response_model=list[NotaResponse])
def obtener_notas(db: Session = Depends(get_db)):
    return db.query(Nota).all()


@router.get("/{id_nota}", response_model=NotaResponse)
def obtener_nota(id_nota: int, db: Session = Depends(get_db)):
    nota = db.query(Nota).filter(Nota.id_nota == id_nota).first()
    if not nota:
        raise NotFoundError("Nota no encontrada")
    return nota


@router.post("/", response_model=NotaResponse)
def crear_nota(nota: NotaCreate, db: Session = Depends(get_db)):
    nueva_nota = Nota(**nota.model_dump())
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota


@router.put("/{id_nota}", response_model=NotaResponse)
def actualizar_nota(id_nota: int, nota: NotaCreate, db: Session = Depends(get_db)):
    nota_db = db.query(Nota).filter(Nota.id_nota == id_nota).first()
    if not nota_db:
        raise NotFoundError("Nota no encontrada")

    for key, value in nota.model_dump().items():
        setattr(nota_db, key, value)

    db.commit()
    db.refresh(nota_db)
    return nota_db


@router.delete("/{id_nota}")
def eliminar_nota(id_nota: int, db: Session = Depends(get_db)):
    nota_db = db.query(Nota).filter(Nota.id_nota == id_nota).first()
    if not nota_db:
        raise NotFoundError("Nota no encontrada")

    db.delete(nota_db)
    db.commit()
    return {"message": "Nota eliminada correctamente"}