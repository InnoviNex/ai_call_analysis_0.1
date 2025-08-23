import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config.settings import (
    CREDENCIALES_GOOGLE,
    SPREADSHEET_ID,
    NOMBRE_HOJA_LICENCIAS,
    NOMBRE_HOJA_REGISTRO,
)


def obtener_cliente_id():
    """Lee el identificador del cliente desde el archivo de licencia."""
    with open("data/licencia/cliente_id.txt", "r", encoding="utf-8") as f:
        return f.read().strip()


def validar_licencia_online(cliente_id: str):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENCIALES_GOOGLE, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(NOMBRE_HOJA_LICENCIAS)

        registros = sheet.get_all_records(expected_headers=["cliente_id", "estado", "vencimiento"])

        for row in registros:
            if row["cliente_id"] == cliente_id:
                if row["estado"].lower() != "activo":
                    return False, "Licencia inactiva"
                vencimiento = datetime.strptime(row["vencimiento"], "%Y-%m-%d").date()
                if vencimiento < datetime.now().date():
                    return False, "Licencia vencida"
                return True, "Licencia válida"

        return False, "Cliente no registrado"
    except Exception as e:
        return False, f"Error al validar licencia: {e}"


def registrar_uso_en_hoja(cliente_id, estado_licencia, archivo_audio):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENCIALES_GOOGLE, scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(NOMBRE_HOJA_REGISTRO)

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_fila = [cliente_id, estado_licencia, now, archivo_audio]
        sheet.append_row(nueva_fila)
    except Exception as e:
        print(f"⚠️ No se pudo registrar el uso en el Sheet: {e}")
