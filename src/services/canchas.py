from ..db import obtener_conexion
from ..repositories.canchas import (
    obtener_deportes_db,
    verificar_deporte_db,
    insertar_cancha_db,
    obtener_canchas_db
)
from ..validators.validators import (
    validar_campos_requeridos,
    validar_texto,
    validar_entero_positivo,
    validar_booleano_estricto
)
from .exceptions import NotFoundError

def listar_deportes_service():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            return obtener_deportes_db(cursor)
    finally:
        conexion.close()

def crear_cancha_service(datos):
    validar_campos_requeridos(datos, ["nombre", "id_deporte", "precio_hora"])
    
    nombre = validar_texto(datos["nombre"], "nombre")
    id_deporte = validar_entero_positivo(datos["id_deporte"], "id_deporte")
    precio_hora = validar_entero_positivo(datos["precio_hora"], "precio_hora")
    
    techada = validar_booleano_estricto(datos.get("techada", False), "techada")
    activa = validar_booleano_estricto(datos.get("activa", True), "activa")

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            if not verificar_deporte_db(cursor, id_deporte):
                raise NotFoundError(f"No existe el deporte con id {id_deporte}")

            nuevo_id = insertar_cancha_db(cursor, nombre, id_deporte, precio_hora, techada, activa)
            conexion.commit()
            return {
                "id": nuevo_id,
                "nombre": nombre,
                "id_deporte": id_deporte,
                "precio_hora": precio_hora,
                "techada": techada,
                "activa": activa
            }
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()

def listar_canchas_service(id_deporte=None):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            return obtener_canchas_db(cursor, id_deporte)
    finally:
        conexion.close()