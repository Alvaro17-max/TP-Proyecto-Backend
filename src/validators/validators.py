import re
from datetime import datetime

EMAIL_REGEX = re.compile(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$")

def validar_campos_requeridos(payload, campos_requeridos):
    if not isinstance(payload, dict):
        raise ValueError("El cuerpo JSON debe ser un objeto")
    faltantes = [campo for campo in campos_requeridos if campo not in payload]
    if faltantes:
        raise ValueError(f"Faltan campos obligatorios: {', '.join(faltantes)}")

def validar_texto(valor, nombre_campo="campo"):
    if not isinstance(valor, str):
        raise ValueError(f"El campo '{nombre_campo}' debe ser texto")
    limpio = valor.strip()
    if not limpio:
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacio")
    return limpio

def validar_email(email_str):
    limpio = validar_texto(email_str, "email").lower()
    if not EMAIL_REGEX.match(limpio):
        raise ValueError("El formato del email es invalido")
    return limpio

def validar_entero_positivo(valor, nombre_campo="campo"):
    if isinstance(valor, bool) or not isinstance(valor, int):
        raise ValueError(f"El campo '{nombre_campo}' debe ser un numero entero")
    if valor <= 0:
        raise ValueError(f"El campo '{nombre_campo}' debe ser mayor a cero")
    return valor

def validar_booleano_estricto(valor, nombre_campo="campo", permitir_none=False):
    if valor is None and permitir_none:
        return None
    if isinstance(valor, bool):
        return valor
    if isinstance(valor, str):
        val = valor.strip().lower()
        if val == "true":
            return True
        if val == "false":
            return False
    raise ValueError(f"El campo '{nombre_campo}' debe ser booleano (true/false)")

def validar_fechas(inicio_str, fin_str):
    formato = "%Y-%m-%d %H:%M:%S"
    try:
        dt_inicio = datetime.strptime(inicio_str, formato)
        dt_fin = datetime.strptime(fin_str, formato)
    except (ValueError, TypeError):
        raise ValueError("Formato de fecha invalido. Use 'YYYY-MM-DD HH:MM:SS'")

    if dt_inicio >= dt_fin:
        raise ValueError("La fecha de inicio debe ser anterior a la de fin")

    if dt_inicio < datetime.now():
        raise ValueError("No se pueden crear reservas en fechas u horarios pasados")

    horas = (dt_fin - dt_inicio).total_seconds() / 3600.0
    if horas <= 0:
        raise ValueError("La duracion de la reserva debe ser de al menos una hora")

    return int(horas)