"""Ejecuta la aplicación Flask para desarrollo y producción."""

import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "Backend"

for path in (str(BACKEND), str(ROOT)):
    if path not in sys.path:
        sys.path.insert(0, path)

# Carga Backend/app.py por ruta para evitar el choque app.py vs carpeta app/
spec = importlib.util.spec_from_file_location("backend_app", BACKEND / "app.py")
backend_app = importlib.util.module_from_spec(spec)
sys.modules["backend_app"] = backend_app
spec.loader.exec_module(backend_app)

app = backend_app.app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))