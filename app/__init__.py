# app/__init__.py  se encarga de inicializar Flask, MongoDB, Redis y registrar las rutas.

from flask import Flask
from flask_pymongo import PyMongo
from redis import Redis
from dotenv import load_dotenv
from flask_cors import CORS
import os

mongo = PyMongo()
redis_client = None

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Configuración desde variables de entorno
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    # Inicializar extensiones
    mongo.init_app(app)
    CORS(app)

    # Registrar rutas
    from app.routes.routes import routes_bp        #aqui debi cambiar .routes.routes porq esta dentro de una carpeta 
    app.register_blueprint(routes_bp)

    return app

def create_redis_client():
    return Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True
    )

redis_client = create_redis_client()