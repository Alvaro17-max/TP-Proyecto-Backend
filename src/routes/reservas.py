import traceback
from flask import Blueprint, request, jsonify
from src.services.reservas import (
    crear_reserva_service,
    listar_reservas_service,
    cancelar_reserva_service
)
from src.services.exceptions import ConflictError, NotFoundError

reservas_bp = Blueprint("reservas_bp", __name__, url_prefix="/reservas")

@reservas_bp.route("", methods=["POST"])
def post_reserva():
    try:
        resultado = crear_reserva_service(request.get_json())
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ConflictError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@reservas_bp.route("", methods=["GET"])
def get_reservas():
    id_socio = request.args.get("id_socio", type=int)
    id_cancha = request.args.get("id_cancha", type=int)
    try:
        res = listar_reservas_service(id_socio, id_cancha)
        return jsonify(res), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@reservas_bp.route("/<int:id_reserva>", methods=["DELETE"])
def delete_reserva(id_reserva):
    try:
        resultado = cancelar_reserva_service(id_reserva)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except ConflictError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"Error interno: {str(e)}"}), 500