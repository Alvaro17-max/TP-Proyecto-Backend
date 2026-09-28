def existe_solapamiento_db(cursor, id_cancha, inicio_str, fin_str):
    sql = """
        SELECT id FROM reservas 
        WHERE id_cancha = %s 
          AND estado != 'cancelada'
          AND STR_TO_DATE(fecha_hora_inicio, '%%Y-%%m-%%d %%H:%%i:%%s') < STR_TO_DATE(%s, '%%Y-%%m-%%d %%H:%%i:%%s')
          AND STR_TO_DATE(fecha_hora_fin, '%%Y-%%m-%%d %%H:%%i:%%s') > STR_TO_DATE(%s, '%%Y-%%m-%%d %%H:%%i:%%s')
        LIMIT 1;
    """
    cursor.execute(sql, (id_cancha, fin_str, inicio_str))
    return cursor.fetchone() is not None

def existe_solapamiento_socio_db(cursor, id_socio, inicio_str, fin_str):
    sql = """
        SELECT id FROM reservas 
        WHERE id_socio = %s 
          AND estado != 'cancelada'
          AND STR_TO_DATE(fecha_hora_inicio, '%%Y-%%m-%%d %%H:%%i:%%s') < STR_TO_DATE(%s, '%%Y-%%m-%%d %%H:%%i:%%s')
          AND STR_TO_DATE(fecha_hora_fin, '%%Y-%%m-%%d %%H:%%i:%%s') > STR_TO_DATE(%s, '%%Y-%%m-%%d %%H:%%i:%%s')
        LIMIT 1;
    """
    cursor.execute(sql, (id_socio, fin_str, inicio_str))
    return cursor.fetchone() is not None

def insertar_reserva_db(cursor, id_socio, id_cancha, inicio, fin, tarifa, total):
    sql = """
        INSERT INTO reservas 
        (id_socio, id_cancha, fecha_hora_inicio, fecha_hora_fin, tarifa_historica, total, estado) 
        VALUES (%s, %s, %s, %s, %s, %s, 'confirmada');
    """
    cursor.execute(sql, (id_socio, id_cancha, inicio, fin, tarifa, total))
    return cursor.lastrowid

def obtener_reservas_db(cursor, id_socio=None, id_cancha=None):
    query = "SELECT * FROM reservas WHERE 1=1"
    params = []
    if id_socio is not None:
        query += " AND id_socio = %s"
        params.append(id_socio)
    if id_cancha is not None:
        query += " AND id_cancha = %s"
        params.append(id_cancha)
    cursor.execute(query, tuple(params))
    return cursor.fetchall()

def obtener_reserva_por_id_db(cursor, id_reserva):
    cursor.execute("SELECT id, estado FROM reservas WHERE id = %s", (id_reserva,))
    return cursor.fetchone()

def cancelar_reserva_db(cursor, id_reserva):
    cursor.execute("UPDATE reservas SET estado = 'cancelada' WHERE id = %s", (id_reserva,))