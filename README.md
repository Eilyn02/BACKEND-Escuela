SISTEMA DE INFORMACIÓN PARA ESCUELA
===================================

Descripción
-----------
Este proyecto consiste en una API REST desarrollada con FastAPI para la gestión de una escuela.
Incluye autenticación con JWT, validaciones de datos, manejo
centralizado de errores y un pipeline CI/CD automatizado.

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
- Pydantic
- Pytest
- Ruff
- JWT (python-jose)
- bcrypt

Estructura del proyecto
-----------------------

- entities → modelos de base de datos
- endpoints → rutas de la API
- crud → cliente HTTP para consumir la API
- database → configuración de conexión a la base de datos
- core → manejo de errores y seguridad (JWT)
- schemas → validaciones de entrada y salida


Ejecución del proyecto
----------------------

1. Instalar dependencias:

pip install -r requirements.txt

2.  Ejecutar migraciones: 
python migrate_db.py

3.  Ejecutar seed:
python seed_db.py

4. Ejecutar la API:
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

Autenticación (JWT)
-------------------

Usuario por defecto: 
correo: admin@escuela.com 
password: Admin123*

Login: 
POST /auth/login

Usar token: 
Authorization: Bearer

Configuración CORS
------------------

Orígenes permitidos: 
- http://localhost:3000 
- http://127.0.0.1:3000 
- http://127.0.0.1:5500 
- http://localhost:5500

Funcionalidades
---------------
- CRUD completo
-  Autenticación JWT
-  Protección de endpoints
-  Validaciones
-  Manejo de errores


Examen 2

-   Migraciones
-   Seeder
-   Core
-   Validaciones
-   CI/CD

Pipeline CI/CD

.github/workflows/ci.yml

Prueba básica

tests/test_app.py

Video:
https://youtu.be/j2pTZtoDEhY


Autores
-------
Luis Miguel Cardona Meneses
Eilyn Esther Alvarino Diaz
