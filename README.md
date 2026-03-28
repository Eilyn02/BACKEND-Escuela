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

---
Examen 2
--------

Para esta segunda entrega se implementaron los siguientes requerimientos:

1. Migraciones de base de datos  
Se creó un sistema de migraciones mediante scripts SQL y el archivo migrate_db.py para crear y actualizar las tablas.

Se añadió el campo telefono en la entidad Profesor.

2. Seeder inicial  
Se implementó el archivo seed_db.py para insertar datos iniciales de forma controlada, evitando duplicados.

3. Carpeta core  
Se creó la carpeta src/core para centralizar:

- Manejo de errores personalizados  
- Respuestas estandarizadas  
- Excepciones propias del sistema  

4. Validaciones  
Se agregaron validaciones en los schemas usando:

- Field(..., min_length=1) para evitar campos vacíos  
- EmailStr para validar correos  
- Validaciones numéricas en algunos campos  

5. Pipeline CI/CD  
Se configuró un pipeline en GitHub Actions que se ejecuta sobre la rama dev.

El pipeline realiza:

- Instalación de dependencias  
- Ejecución de migraciones  
- Ejecución de seed  
- Revisión de código con Ruff  
- Prueba básica con pytest  

---

Pipeline CI/CD
--------------

El archivo del pipeline se encuentra en:

.github/workflows/ci.yml

Se ejecuta automáticamente en:

- push a la rama dev  
- pull request hacia dev  

---

Prueba básica
-------------

Se creó una prueba en:

tests/test_app.py

Esta prueba verifica que la API responda correctamente en el endpoint principal.

