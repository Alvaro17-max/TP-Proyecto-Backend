import pymysql
from pymysql.cursors import DictCursor

def obtener_conexion():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root_password",
        database="club_deportivo",                     
        charset="utf8mb4",
        cursorclass=DictCursor,
        autocommit=True
    )

