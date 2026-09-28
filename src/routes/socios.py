from flask import Blueprint, request, jsonify
from src.services.socios import (
    crear_socio_service,
    listar_socios_service,
    dar_baja_socio_service
)
from src.services.exceptions import ConflictError, NotFoundError

socios_bp = Blueprint("socios_bp", __name__, url_prefix="/socios")

@socios_bp.route("", methods=["POST"])
def post_socio():
    try:
        resultado = crear_socio_service(request.get_json())
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except ConflictError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500

@socios_bp.route("", methods=["GET"])
def get_socios():
    activo = request.args.get("activo")
    try:
        resultado = listar_socios_service(activo)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@socios_bp.route("/<int:id_socio>", methods=["DELETE"])
def delete_socio(id_socio):
    try:
        resultado = dar_baja_socio_service(id_socio)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ConflictError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"}), 500