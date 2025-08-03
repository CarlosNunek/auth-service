from pymongo import MongoClient
import bcrypt

from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_database()
usuarios = db.usuarios

def crear_usuario(data):
    if usuarios.find_one({"cedula": data["cedula"]}):
        return {"error": "Usuario ya existe"}, 409

    usuario = {
        "cedula": data["cedula"],
        "nombres": data["nombres"],
        "apellidos": data["apellidos"],
        "fecha_nacimiento": data["fecha_nacimiento"],
        "email": data["email"],
        "password": bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    }

    usuarios.insert_one(usuario)
    return {"mensaje": "Usuario registrado correctamente"}, 201
