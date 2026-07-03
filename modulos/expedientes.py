from pathlib import Path
import os


RUTA_BASE = Path("C:/SATBOT/Expedientes")


def abrir_expediente(rfc):

    carpeta = RUTA_BASE / rfc

    carpeta.mkdir(parents=True, exist_ok=True)

    os.startfile(carpeta)