from flask import Blueprint
from app.controllers.auth_controller import registrar_usuario

routes_bp = Blueprint('routes_bp', __name__)
routes_bp.route('/register', methods=['POST'])(registrar_usuario)
