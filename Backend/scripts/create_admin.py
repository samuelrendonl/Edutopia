"""Crea o promociona una cuenta administradora de Edutopia.

Uso:
    python Backend/scripts/create_admin.py --name "Administrador" \
        --email admin@edutopia.local

La contraseña se solicita de forma interactiva si no se entrega con
``--password``. Ejecuta primero la migración 002_roles_and_permissions.sql.
"""

import argparse
import getpass
import os
import sys

from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
import mysql.connector


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "edutopia"),
}


def main():
    parser = argparse.ArgumentParser(description="Crear administrador de Edutopia")
    parser.add_argument("--name", required=True, help="Nombre visible del administrador")
    parser.add_argument("--email", required=True, help="Correo para iniciar sesión")
    parser.add_argument("--password", help="Contraseña; si se omite se solicita de forma segura")
    args = parser.parse_args()

    password = args.password or getpass.getpass("Contraseña del administrador: ")
    if len(password) < 6:
        parser.error("La contraseña debe tener al menos 6 caracteres.")

    connection = mysql.connector.connect(**DB_CONFIG)
    try:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO parents (name, email, password_hash, role)
               VALUES (%s, %s, %s, 'admin')
               ON DUPLICATE KEY UPDATE
                 name = VALUES(name), password_hash = VALUES(password_hash), role = 'admin'""",
            (args.name.strip(), args.email.strip().lower(), generate_password_hash(password)),
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    print(f"Administrador listo: {args.email.strip().lower()}")


if __name__ == "__main__":
    try:
        main()
    except mysql.connector.Error as error:
        print(f"No se pudo crear el administrador: {error}", file=sys.stderr)
        raise SystemExit(1)
