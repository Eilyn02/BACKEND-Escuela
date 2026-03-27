from datetime import date

from src.database.config import SessionLocal

from src.entities.grado import Grado
from src.entities.periodo import Periodo
from src.entities.profesor import Profesor

# Importar modelos
import src.entities.estudiante  # noqa: F401
import src.entities.materia  # noqa: F401
import src.entities.nota  # noqa: F401


def seed_grados(db):
    """
    Inserta grados iniciales si no existen.
    """
    grados_iniciales = ["Primero", "Segundo", "Tercero"]

    for nombre in grados_iniciales:
        existe = db.query(Grado).filter(Grado.nombre == nombre).first()
        if not existe:
            db.add(Grado(nombre=nombre))

    db.commit()
    print("Grados verificados correctamente.")


def seed_periodo(db):
    """
    Inserta un periodo inicial si no existe.
    """
    existe = db.query(Periodo).filter(Periodo.nombre == "2026-1").first()
    if not existe:
        db.add(
            Periodo(
                nombre="2026-1",
                fecha_inicio=date(2026, 1, 15),
                fecha_fin=date(2026, 6, 15),
            )
        )
        db.commit()

    print("Periodo verificado correctamente.")


def seed_profesor(db):
    """
    Inserta un profesor inicial si no existe.
    """
    existe = (
        db.query(Profesor).filter(Profesor.correo == "ana.lopez@escuela.com").first()
    )
    if not existe:
        db.add(
            Profesor(
                nombre="Ana",
                apellido="Lopez",
                correo="ana.lopez@escuela.com",
                especialidad="Matematicas",
                telefono="3001234567",
            )
        )
        db.commit()

    print("Profesor inicial verificado correctamente.")


def run_seed():
    """
    Ejecuta el seeder del sistema.
    """
    db = SessionLocal()
    try:
        seed_grados(db)
        seed_periodo(db)
        seed_profesor(db)
        print("Seed ejecutado correctamente.")
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
