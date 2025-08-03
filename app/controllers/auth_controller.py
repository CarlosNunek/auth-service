from flask import request, jsonify
from app.models.user_model import crear_usuario
from app.services.auth_service import publicar_usuario_registrado

def registrar_usuario():
    data = request.get_json()

    campos_requeridos = ["cedula", "nombres", "apellidos", "fecha_nacimiento", "email", "password"]
    if not all(campo in data and data[campo] for campo in campos_requeridos):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    res, code = crear_usuario(data)

    if code == 201:
        publicar_usuario_registrado(data["cedula"])

    return jsonify(res), code
