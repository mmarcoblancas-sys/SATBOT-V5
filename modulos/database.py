import sqlite3

from modulos.config import DB_PATH


def conectar():
    """Devuelve una conexión a la base de datos."""

    return sqlite3.connect(DB_PATH)


def crear_base():

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS clientes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            rfc TEXT UNIQUE NOT NULL,

            nombre TEXT NOT NULL,

            activo INTEGER DEFAULT 1

        )

    """)

    conexion.commit()

    conexion.close()


if __name__ == "__main__":

    crear_base()

    print("Base de datos lista.")