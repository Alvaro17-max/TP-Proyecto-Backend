def obtener_deportes_db(cursor):
    cursor.execute("SELECT * FROM deportes;")
    return cursor.fetchall()

def verificar_deporte_db(cursor, id_deporte):
    cursor.execute("SELECT id FROM deportes WHERE id = %s;", (id_deporte,))
    return cursor.fetchone() is not None

def insertar_cancha_db(cursor, nombre, id_deporte, precio_hora, techada, activa):
    sql = """
        INSERT INTO canchas (nombre, id_deporte, precio_hora, techada, activa)
        VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(sql, (nombre, id_deporte, precio_hora, techada, activa))
    return cursor.lastrowid

def obtener_canchas_db(cursor, id_deporte=None):
    query = "SELECT * FROM canchas WHERE 1=1"
    params = []
    if id_deporte is not None:
        query += " AND id_deporte = %s"
        params.append(id_deporte)
    cursor.execute(query, tuple(params))
    return cursor.fetchall()

def obtener_cancha_por_id_db(cursor, id_cancha):
    cursor.execute("SELECT * FROM canchas WHERE id = %s;", (id_cancha,))
    return cursor.fetchone()