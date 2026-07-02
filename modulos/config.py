from pathlib import Path

# ============================
# RUTAS DEL PROYECTO
# ============================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "satbot.db"

ASSETS_DIR = BASE_DIR / "assets"

ICONOS_DIR = BASE_DIR / "iconos"

EXPEDIENTES_DIR = BASE_DIR / "Expedientes"

LOGS_DIR = BASE_DIR / "logs"

CLIENTES_TXT = Path(r"C:\SATBOT\clientes.txt")