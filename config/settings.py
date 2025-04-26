CREDENCIALES_GOOGLE = "credenciales.json"
SPREADSHEET_ID = "1IbwEn_59WEsLl6kYIc5C-V5AKOUYo0LJ26sYr7IbRqY"
NOMBRE_HOJA_LICENCIAS = "licencias"
NOMBRE_HOJA_REGISTRO = "APi_Licencias"

from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")