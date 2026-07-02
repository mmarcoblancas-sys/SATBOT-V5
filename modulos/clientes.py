import os


RUTA_CLIENTES = r"C:\SATBOT\clientes.txt"


def obtener_clientes():

    clientes = []

    if not os.path.exists(RUTA_CLIENTES):
        return clientes

    with open(
        RUTA_CLIENTES,
        "r",
        encoding="utf-8"
    ) as archivo:

        for linea in archivo:

            linea = linea.strip()

            if "|" in linea:

                rfc, nombre = linea.split("|", 1)

                clientes.append(
                    {
                        "rfc": rfc,
                        "nombre": nombre
                    }
                )

    return clientes