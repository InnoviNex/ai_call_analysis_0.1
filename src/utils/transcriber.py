from openai import OpenAI
from config.settings import OPENAI_API_KEY
from utils.logger import log_info, log_error

client = OpenAI(api_key=OPENAI_API_KEY)

def transcribir_audio(ruta_audio):
    try:
        with open(ruta_audio, "rb") as audio:
            log_info("🎙️ Transcribiendo audio con Whisper...")
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio
            )
        texto = response.text
        log_info("✅ Transcripción completada.")
        return texto
    except Exception as e:
        log_error(f"❌ Error al transcribir: {e}")
        return None