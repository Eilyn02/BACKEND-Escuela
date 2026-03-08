from src.database.config import create_tables

# Importar modelos para que SQLAlchemy registre las tablas
import src.entities.profesor  # noqa: F401
import src.entities.estudiante  # noqa: F401
import src.entities.materia  # noqa: F401
import src.entities.periodo  # noqa: F401
import src.entities.grado  # noqa: F401
import src.entities.nota  # noqa: F401


if __name__ == "__main__":
    create_tables()
    print("Tablas creadas correctamente en la base de datos")
