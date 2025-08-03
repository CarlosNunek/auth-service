# Auth Service – Registro de Usuarios con Flask y MongoDB

Este microservicio permite registrar usuarios mediante una API REST con Flask, y almacena los datos en MongoDB con contraseña del usuario encriptada. También publica un evento en Redis cuando un usuario se registra exitosamente.

## 📦 Estructura

- `app/` – Lógica principal del microservicio (controladores, modelos, rutas y servicios). Arquitectura MVC
- `run.py` – Archivo principal para ejecutar el servidor Flask.
- `.env` – Configuración de variables de entorno (MongoDB y Redis).
- `Dockerfile` – Imagen Docker para contenerizar el servicio.
- `tests/` – Pruebas automatizadas con `pytest`.

## 🚀 Endpoints

- `POST /register` – Registra un nuevo usuario.
  ```json
  {
    "cedula": "1234567890",
    "nombres": "Carlos",
    "apellidos": "Nuñez",
    "fecha_nacimiento": "2000-01-01",
    "email": "carlos@example.com",
    "password": "securepassword"
  }
  ```

## ✅ Pruebas

Para correr las pruebas:
```bash
pytest tests/
```

## 🐳 Docker

Para construir y correr el contenedor:
```bash
docker build -t auth-service .
docker run -d --name auth-service -p 6000:6000 --env-file .env auth-service
```
