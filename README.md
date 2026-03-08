# BACKEND-Escuela
Sistema de Información para una Escuela
## Estructura inicial del proyecto

Se creó la estructura base del proyecto siguiendo una organización por carpetas para:

- entities (modelos de base de datos)
- schemas (validación con Pydantic)
- endpoints (routers de FastAPI)
- crud (cliente para consumir la API)
- database (configuración de conexión a la base de datos)

## Configuración de base de datos

El proyecto utiliza PostgreSQL en Neon mediante variables de entorno definidas en el archivo .env.

## Ejecución del proyecto

Para crear las tablas manualmente:

```bash
python init_db.py