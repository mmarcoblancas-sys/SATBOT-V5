from modulos.database import conectar


class ClienteDAO:

    def obtener_clientes(self):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            SELECT
                id,
                rfc,
                nombre

            FROM clientes

            WHERE activo = 1

            ORDER BY nombre

        """)

        clientes = cursor.fetchall()

        conexion.close()

        return clientes

    def buscar(self, texto):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            SELECT
                id,
                rfc,
                nombre

            FROM clientes

            WHERE activo = 1

            AND
            (
                nombre LIKE ?
                OR
                rfc LIKE ?
            )

            ORDER BY nombre

        """, (

            f"%{texto}%",
            f"%{texto}%"

        ))

        clientes = cursor.fetchall()

        conexion.close()

        return clientes


# ===============================
# PRUEBA
# ===============================

if __name__ == "__main__":

    dao = ClienteDAO()

    clientes = dao.obtener_clientes()

    print("\nCLIENTES")
    print("----------------------")

    for cliente in clientes:
        print(cliente)