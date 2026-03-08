from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.periodo import Periodo
from src.schemas.periodo_schema import PeriodoCreate, PeriodoResponse

router = APIRouter(prefix="/periodos", tags=["Periodos"])


@router.get("/", response_model=list[PeriodoResponse])
def obtener_periodos(db: Session = Depends(get_db)):
    return db.query(Periodo).all()


@router.get("/{id_periodo}", response_model=PeriodoResponse)
def obtener_periodo(id_periodo: int, db: Session = Depends(get_db)):
    periodo = db.query(Periodo).filter(Periodo.id_periodo == id_periodo).first()
    if not periodo:
        raise HTTPException(status_code=404, detail="Periodo no encontrado")
    return periodo


@router.post("/", response_model=PeriodoResponse)
def crear_periodo(periodo: PeriodoCreate, db: Session = Depends(get_db)):
    nuevo_periodo = Periodo(**periodo.model_dump())
    db.add(nuevo_periodo)
    db.commit()
    db.refresh(nuevo_periodo)
    return nuevo_periodo


@router.put("/{id_periodo}", response_model=PeriodoResponse)
def actualizar_periodo(id_periodo: int, periodo: PeriodoCreate, db: Session = Depends(get_db)):
    periodo_db = db.query(Periodo).filter(Periodo.id_periodo == id_periodo).first()
    if not periodo_db:
        raise HTTPException(status_code=404, detail="Periodo no encontrado")

    for key, value in periodo.model_dump().items():
        setattr(periodo_db, key, value)

    db.commit()
    db.refresh(periodo_db)
    return periodo_db


@router.delete("/{id_periodo}")
def eliminar_periodo(id_periodo: int, db: Session = Depends(get_db)):
    periodo_db = db.query(Periodo).filter(Periodo.id_periodo == id_periodo).first()
    if not periodo_db:
        raise HTTPException(status_code=404, detail="Periodo no encontrado")

    db.delete(periodo_db)
    db.commit()
    return {"message": "Periodo eliminado correctamente"}