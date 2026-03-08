SISTEMA DE INFORMACIÓN PARA ESCUELA
===================================

Descripción
-----------
Este proyecto consiste en una API REST desarrollada con FastAPI para la gestión de una escuela.

Permite administrar:
- Profesores
- Estudiantes
- Materias
- Grados
- Periodos
- Notas

La API utiliza PostgreSQL (Neon) como base de datos y SQLAlchemy como ORM.

Tecnologías utilizadas
----------------------
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- Uvicorn
- httpx

Estructura del proyecto
-----------------------

- entities → modelos de base de datos
- endpoints → rutas de la API
- crud → cliente HTTP para consumir la API
- database → configuración de conexión a la base de datos


Ejecución del proyecto
----------------------

1. Instalar dependencias:

pip install -r requirements.txt

2. Ejecutar la API:

uvicorn src.app:app --reload


Documentación de la API
-----------------------

La documentación interactiva de la API está disponible en:

http://127.0.0.1:8000/docs


Menú por consola
----------------

El sistema incluye un menú interactivo que permite gestionar las entidades del sistema consumiendo la API mediante httpx.

Ejecutar con:

python main.py


Funcionalidades
---------------
- CRUD de profesores
- CRUD de estudiantes
- CRUD de materias
- CRUD de grados
- CRUD de periodos
- CRUD de notas


Autores
-------
Luis Miguel Cardona Meneses
Eilyn Alvarino
