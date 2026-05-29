```txt
SISTEMA DE INFORMACIÓN PARA ESCUELA
==================================

Descripción
-----------
Este proyecto consiste en una API REST desarrollada con FastAPI para la gestión de una escuela.
Incluye autenticación JWT, validaciones de datos, manejo centralizado de errores,
testing automatizado y despliegue continuo (CI/CD).

La API permite administrar:

- Profesores
- Estudiantes
- Materias
- Grados
- Periodos
- Notas

La base de datos utilizada es PostgreSQL alojada en Neon y el proyecto
se encuentra desplegado en Render.

Tecnologías utilizadas
----------------------
- Python 3.10
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)
- Uvicorn
- Pydantic
- JWT (python-jose)
- bcrypt
- httpx
- Pytest
- Ruff
- GitHub Actions
- Render

Arquitectura del proyecto
-------------------------

src/
│
├── core/
│   ├── security.py
│   ├── config.py
│   └── exceptions.py
│
├── crud/
│
├── database/
│   ├── connection.py
│   └── base.py
│
├── endpoints/
│
├── entities/
│
├── schemas/
│
├── app.py
│
tests/
│
.github/workflows/
│
requirements.txt

Funcionalidades principales
---------------------------
- CRUD completo
- Autenticación JWT
- Protección de endpoints
- Validaciones con Pydantic
- Manejo centralizado de errores
- Integración con PostgreSQL
- Testing automatizado
- Pipeline CI/CD
- Deploy automático en Render

Autenticación JWT
-----------------

Login:
POST /auth/login

Usuario administrador por defecto:

correo:
admin@escuela.com

password:
Admin123*

Uso del token:

Authorization: Bearer <token>

Endpoints protegidos
--------------------

Profesores:
- Crear profesor
- Actualizar profesor
- Eliminar profesor

Estudiantes:
- Crear estudiante
- Actualizar estudiante
- Eliminar estudiante

Base de datos
--------------
Proveedor:
Neon PostgreSQL

Variables de entorno utilizadas:

DATABASE_URL=
JWT_SECRET_KEY=
JWT_ALGORITHM=
JWT_EXPIRE_MINUTES=

Instalación del proyecto
------------------------

1. Clonar repositorio

git clone <url-del-repo>

2. Crear entorno virtual

Windows:
python -m venv venv

Activar entorno:
venv\Scripts\activate

3. Instalar dependencias

pip install -r requirements.txt

4. Configurar variables de entorno

Crear archivo .env con:

DATABASE_URL=tu_url
JWT_SECRET_KEY=tu_clave
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60

5. Ejecutar migraciones

python migrate_db.py

6. Ejecutar seed

python seed_db.py

7. Ejecutar servidor

uvicorn src.app:app --reload

Servidor local:
http://127.0.0.1:8000

Documentación Swagger
---------------------

Disponible en:

http://127.0.0.1:8000/docs

Deploy en producción
--------------------

Backend desplegado en Render:

https://backend-escuela-neag.onrender.com

Pipeline CI/CD
---------------

El proyecto utiliza GitHub Actions para:

- Ejecutar tests automáticamente
- Validar código
- Verificar dependencias
- Automatizar integración continua

Archivo:

.github/workflows/ci.yml

Testing
-------

Ejecutar pruebas:

pytest -v

Resultado esperado:
8 passed

Linting
-------

Ejecutar Ruff:

ruff check .

Menú interactivo
----------------

El proyecto incluye un menú por consola que consume la API mediante httpx.

Ejecutar:

python main.py

Configuración CORS
------------------

Orígenes permitidos:

- http://localhost:3000
- http://127.0.0.1:3000
- http://localhost:5500
- http://127.0.0.1:5500

Estado actual del proyecto
--------------------------

Backend finalizado con:

- API funcional
- JWT implementado
- Endpoints protegidos
- Base de datos conectada
- Deploy funcionando
- CI/CD funcionando
- Tests aprobados
- Swagger operativo

Próximos pasos
--------------

- Desarrollo del frontend
- Integración completa frontend-backend
- Firebase Hosting
- Mejoras visuales
- Roles y permisos
- Dashboard administrativo



Video:
https://youtu.be/j2pTZtoDEhY

Autores
--------

Luis Miguel Cardona Meneses
Eilyn Esther Alvarino Diaz
```






