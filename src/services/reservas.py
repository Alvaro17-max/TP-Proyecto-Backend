from src.db import obtener_conexion
from src.repositories.reservas import (
    existe_solapamiento_db,
    existe_solapamiento_socio_db,
    insertar_reserva_db,
    obtener_reservas_db,
    obtener_reserva_por_id_db,
    cancelar_reserva_db
)
from src.repositories.canchas import obtener_cancha_por_id_db
from src.repositories.socios import buscar_socio_por_id_db
from src.validators.validators import (
    validar_campos_requeridos,
    validar_entero_positivo,
    validar_fechas
)
from src.services.exceptions import NotFoundError, ConflictError

def crear_reserva_service(datos):
    validar_campos_requeridos(datos, ["id_socio", "id_cancha", "fecha_hora_inicio", "fecha_hora_fin"])
    
    id_socio = validar_entero_positivo(datos["id_socio"], "id_socio")
    id_cancha = validar_entero_positivo(datos["id_cancha"], "id_cancha")
    inicio_str = datos["fecha_hora_inicio"]
    fin_str = datos["fecha_hora_fin"]
    
    horas = validar_fechas(inicio_str, fin_str)

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        socio = buscar_socio_por_id_db(cursor, id_socio)
        if not socio:
            raise NotFoundError(f"No existe el socio con id {id_socio}")
        if not socio["activo"]:
            raise ConflictError("El socio se encuentra inactivo")

        cancha = obtener_cancha_por_id_db(cursor, id_cancha)
        if not cancha:
            raise NotFoundError(f"No existe la cancha con id {id_cancha}")
        if not cancha["activa"]:
            raise ConflictError("La cancha se encuentra inactiva")

        if existe_solapamiento_db(cursor, id_cancha, inicio_str, fin_str):
            raise ConflictError("La cancha ya esta reservada en ese horario")  

        if existe_solapamiento_socio_db(cursor, id_socio, inicio_str, fin_str):
            raise ConflictError("El socio ya tiene otra reserva en ese mismo horario")

        tarifa = cancha["precio_hora"]
        total = tarifa * horas
        nuevo_id = insertar_reserva_db(cursor, id_socio, id_cancha, inicio_str, fin_str, tarifa, total)
        conexion.commit()

        return {
            "id": nuevo_id,
            "id_socio": id_socio,
            "id_cancha": id_cancha,
            "fecha_hora_inicio": inicio_str,
            "fecha_hora_fin": fin_str,
            "tarifa_historica": tarifa,
            "total": total,
            "estado": "confirmada"
        }
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()

def listar_reservas_service(id_socio=None, id_cancha=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        return obtener_reservas_db(cursor, id_socio, id_cancha)
    finally:
        cursor.close()
        conexion.close()

def cancelar_reserva_service(id_reserva):
    id_valido = validar_entero_positivo(id_reserva, "id_reserva")
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        reserva = obtener_reserva_por_id_db(cursor, id_valido)
        if not reserva:
            raise NotFoundError(f"No existe la reserva con id {id_valido}")
        if reserva["estado"] == "cancelada":
            raise ConflictError("La reserva ya se encuentra cancelada")

        cancelar_reserva_db(cursor, id_valido)
        conexion.commit()
        return {"mensaje": f"Reserva {id_valido} cancelada exitosamente"}
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()