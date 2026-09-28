def buscar_socio_por_email_db(cursor, email):
    cursor.execute("SELECT id FROM socios WHERE email = %s", (email,))
    return cursor.fetchone()

def insertar_socio_db(cursor, nombre, email):
    cursor.execute(
        "INSERT INTO socios (nombre, email, activo) VALUES (%s, %s, TRUE)",
        (nombre, email)
    )
    return cursor.lastrowid

def obtener_socios_db(cursor, activo=None):
    if activo is not None:
        cursor.execute("SELECT * FROM socios WHERE activo = %s", (activo,))
    else:
        cursor.execute("SELECT * FROM socios")
    return cursor.fetchall()

def buscar_socio_por_id_db(cursor, id_socio):
    cursor.execute("SELECT id, activo FROM socios WHERE id = %s", (id_socio,))
    return cursor.fetchone()

def dar_baja_socio_db(cursor, id_socio):
    cursor.execute("UPDATE socios SET activo = FALSE WHERE id = %s", (id_socio,))