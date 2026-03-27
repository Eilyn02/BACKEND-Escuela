import os

from sqlalchemy import text

from src.database.config import SessionLocal, create_tables

# Importar modelos para que SQLAlchemy conozca las tablas
import src.entities.profesor  # noqa: F401
import src.entities.estudiante  # noqa: F401
import src.entities.materia  # noqa: F401
import src.entities.periodo  # noqa: F401
import src.entities.grado  # noqa: F401
import src.entities.nota  # noqa: F401


MIGRATIONS_DIR = "migrations"


def ensure_migrations_table():
    """
    Crea la tabla que guarda el historial de migraciones ejecutadas.
    """
    db = SessionLocal()
    try:
        db.execute(
            text(
                """
            CREATE TABLE IF NOT EXISTS _schema_migrations (
                id SERIAL PRIMARY KEY,
                filename VARCHAR(255) UNIQUE NOT NULL,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
            )
        )
        db.commit()
    finally:
        db.close()


def get_executed_migrations():
    """
    Obtiene la lista de migraciones ya ejecutadas.
    """
    db = SessionLocal()
    try:
        result = db.execute(text("SELECT filename FROM _schema_migrations;"))
        return {row[0] for row in result.fetchall()}
    finally:
        db.close()


def apply_migration(filename):
    """
    Ejecuta una migración SQL y la registra en la tabla _schema_migrations.
    """
    path = os.path.join(MIGRATIONS_DIR, filename)

    with open(path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    db = SessionLocal()
    try:
        db.execute(text(sql_script))
        db.execute(
            text("INSERT INTO _schema_migrations (filename) VALUES (:filename);"),
            {"filename": filename},
        )
        db.commit()
        print(f"Migración aplicada: {filename}")
    finally:
        db.close()


def run_migrations():
    """
    Ejecuta todas las migraciones pendientes.
    """
    if not os.path.exists(MIGRATIONS_DIR):
        print("No existe la carpeta migrations.")
        return

    executed = get_executed_migrations()
    files = sorted(f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql"))

    for filename in files:
        if filename not in executed:
            apply_migration(filename)
        else:
            print(f"Migración ya aplicada: {filename}")


if __name__ == "__main__":
    print("Creando tablas base...")
    create_tables()

    print("Verificando tabla de migraciones...")
    ensure_migrations_table()

    print("Ejecutando migraciones pendientes...")
    run_migrations()

    print("Proceso de migración finalizado correctamente.")
