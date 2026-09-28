from flask import Blueprint, request, jsonify
from src.services.canchas import (
    crear_cancha_service,
    listar_canchas_service,
    listar_deportes_service
)
from src.services.exceptions import NotFoundError, ConflictError

canchas_bp = Blueprint("canchas_bp", __name__, url_prefix="/canchas")
deportes_bp = Blueprint("deportes_bp", __name__, url_prefix="/deportes")

@canchas_bp.route("", methods=["POST"])
def post_cancha():
    try:
        resultado = crear_cancha_service(request.get_json())
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ConflictError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@canchas_bp.route("", methods=["GET"])
def get_canchas():
    id_deporte = request.args.get("id_deporte", type=int)
    try:
        resultado = listar_canchas_service(id_deporte)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@deportes_bp.route("", methods=["GET"])
def get_deportes():
    try:
        resultado = listar_deportes_service()
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500