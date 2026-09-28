from ..db import obtener_conexion
from ..repositories.socios import (
    buscar_socio_por_email_db,
    insertar_socio_db,
    obtener_socios_db,
    buscar_socio_por_id_db,
    dar_baja_socio_db
)
from ..validators.validators import (
    validar_campos_requeridos,
    validar_texto,
    validar_email,
    validar_entero_positivo
)
from .exceptions import NotFoundError, ConflictError

def crear_socio_service(datos):
    validar_campos_requeridos(datos, ["nombre", "email"])
    
    nombre = validar_texto(datos["nombre"], "nombre")
    email = validar_email(datos["email"])

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            if buscar_socio_por_email_db(cursor, email):
                raise ConflictError(f"Ya existe un socio registrado con el email {email}")

            nuevo_id = insertar_socio_db(cursor, nombre, email)
            conexion.commit()
            return {
                "id": nuevo_id,
                "nombre": nombre,
                "email": email,
                "activo": True
            }
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()

def listar_socios_service(activo=None):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            return obtener_socios_db(cursor, activo)
    finally:
        conexion.close()

def dar_baja_socio_service(id_socio):
    id_valido = validar_entero_positivo(id_socio, "id_socio")
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            socio = buscar_socio_por_id_db(cursor, id_valido)
            if not socio:
                raise NotFoundError(f"No existe el socio con id {id_valido}")
            if not socio["activo"]:
                raise ConflictError("El socio ya esta dado de baja")

            dar_baja_socio_db(cursor, id_valido)
            conexion.commit()
            return {"mensaje": f"Socio {id_valido} dado de baja exitosamente"}
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()